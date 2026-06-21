"""Merge Kaggle datasets from ``last/`` into one backend training CSV.

Output schema stays compatible with ``backend.dataset_cleaner``:
``content`` contains raw text and ``is_fake`` is a boolean label.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT_DIR = PROJECT_ROOT / "last"
DEFAULT_OUTPUT = PROJECT_ROOT / "backend/data/merged_fake_news_dataset.csv"

STANDARD_COLUMNS = [
    "id",
    "title",
    "url",
    "source",
    "summary",
    "content",
    "published_at",
    "crawled_at",
    "is_fake",
    "dataset_name",
    "original_file",
]


def _normalize_text(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split()).strip()


def _make_frame(
    *,
    df: pd.DataFrame,
    dataset_name: str,
    original_file: Path,
    text_col: str,
    is_fake,
    title_col: str | None = None,
    url_col: str | None = None,
    source_col: str | None = None,
    summary_col: str | None = None,
    published_col: str | None = None,
) -> pd.DataFrame:
    out = pd.DataFrame()
    out["title"] = df[title_col].fillna("").astype(str) if title_col in df.columns else ""
    out["url"] = df[url_col].fillna("").astype(str) if url_col in df.columns else ""
    if source_col in df.columns:
        out["source"] = df[source_col].fillna("").astype(str)
    else:
        out["source"] = dataset_name
    out["summary"] = df[summary_col].fillna("").astype(str) if summary_col in df.columns else ""
    out["content"] = df[text_col].map(_normalize_text)
    out["published_at"] = (
        df[published_col].fillna("").astype(str) if published_col in df.columns else ""
    )
    out["crawled_at"] = ""
    out["is_fake"] = is_fake(df) if callable(is_fake) else bool(is_fake)
    out["dataset_name"] = dataset_name
    out["original_file"] = str(original_file.relative_to(PROJECT_ROOT))
    return out


def _load_phngnguynthu(root: Path) -> list[pd.DataFrame]:
    """Dataset with real-news CSV files whose internal label convention differs."""
    dataset_dir = root / "Vietnamese_fake_news_dataset"
    frames: list[pd.DataFrame] = []
    for path in sorted(dataset_dir.glob("*.csv")):
        df = pd.read_csv(path)
        if "content" not in df.columns:
            continue

        name = path.name.lower()
        if "real" in name:
            label = False
        elif "fake" in name:
            label = True
        else:
            raise ValueError(f"Cannot infer label from file name: {path}")

        frames.append(
            _make_frame(
                df=df,
                dataset_name="phngnguynthu1803/vietnamese-fake-news-dataset",
                original_file=path,
                text_col="content",
                is_fake=label,
                title_col="title",
                url_col="url",
                source_col="source",
                published_col="date",
            )
        )
    return frames


def _load_chuynvinquc(root: Path) -> list[pd.DataFrame]:
    dataset_dir = root / "Fake News Vietnamese Dataset"
    frames: list[pd.DataFrame] = []

    files = list(sorted(dataset_dir.glob("*.csv"))) + list(sorted(dataset_dir.glob("*.xlsx")))
    for path in files:
        if path.suffix.lower() == ".xlsx":
            df = pd.read_excel(path)
        else:
            df = pd.read_csv(path)
        if "post_message" not in df.columns or "label" not in df.columns:
            continue

        frames.append(
            _make_frame(
                df=df,
                dataset_name="chuynvinquc/fakenewvn",
                original_file=path,
                text_col="post_message",
                is_fake=lambda d: d["label"].astype(int).eq(1),
                source_col=None,
                published_col="timestamp_post",
            )
        )
    return frames


def _load_pbl7(root: Path) -> list[pd.DataFrame]:
    dataset_dir = root / "Vietnamese Fake-News-Dataset-PBL7"
    frames: list[pd.DataFrame] = []
    for path in sorted(dataset_dir.rglob("*.csv")):
        df = pd.read_csv(path)
        if "Maintext" not in df.columns or "Label" not in df.columns:
            continue

        frames.append(
            _make_frame(
                df=df,
                dataset_name="goumanguyen/vietnamese-fake-news-dataset-pbl7",
                original_file=path,
                text_col="Maintext",
                is_fake=lambda d: d["Label"].astype(int).eq(1),
            )
        )
    return frames


def _load_medical(root: Path) -> list[pd.DataFrame]:
    dataset_dir = root / "Vietnamese medical fake news dataset"
    path = dataset_dir / "full_dataset.csv"
    if not path.exists():
        return []

    df = pd.read_csv(path)
    return [
        _make_frame(
            df=df,
            dataset_name="leviettrieu369/vietnamese-medical-fake-news-dataset",
            original_file=path,
            text_col="content",
            is_fake=lambda d: d["is_fake"].astype(bool),
            title_col="title",
            url_col="url",
            source_col="source",
            summary_col="summary",
            published_col="published_at",
        )
    ]


def merge_datasets(input_dir: Path = DEFAULT_INPUT_DIR, min_chars: int = 20) -> pd.DataFrame:
    loaders = [_load_phngnguynthu, _load_chuynvinquc, _load_pbl7, _load_medical]
    frames: list[pd.DataFrame] = []
    for loader in loaders:
        frames.extend(loader(input_dir))

    if not frames:
        raise FileNotFoundError(f"No supported dataset files found under {input_dir}")

    df = pd.concat(frames, ignore_index=True)
    df["content"] = df["content"].map(_normalize_text)
    df = df[df["content"].str.len() > min_chars].copy()

    df["_dedup_key"] = df["content"].str.casefold()
    label_counts = df.groupby("_dedup_key")["is_fake"].nunique()
    conflicting_keys = set(label_counts[label_counts > 1].index)
    if conflicting_keys:
        df = df[~df["_dedup_key"].isin(conflicting_keys)].copy()

    df = df.drop_duplicates(subset=["_dedup_key"], keep="first").reset_index(drop=True)
    df = df.drop(columns=["_dedup_key"])
    df.insert(0, "id", range(1, len(df) + 1))

    return df[STANDARD_COLUMNS]


def save_merged_dataset(
    input_dir: Path = DEFAULT_INPUT_DIR,
    output_path: Path = DEFAULT_OUTPUT,
    min_chars: int = 20,
) -> pd.DataFrame:
    df = merge_datasets(input_dir=input_dir, min_chars=min_chars)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"[merge_last_datasets] Saved: {output_path}")
    print(f"[merge_last_datasets] Rows: {len(df)}")
    print("[merge_last_datasets] Label counts:")
    print(df["is_fake"].value_counts().rename(index={False: "real", True: "fake"}))
    print("[merge_last_datasets] Dataset counts:")
    print(pd.crosstab(df["dataset_name"], df["is_fake"], margins=True))
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge Kaggle datasets from last/")
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--min-chars", type=int, default=20)
    args = parser.parse_args()

    save_merged_dataset(args.input_dir, args.output, args.min_chars)


if __name__ == "__main__":
    main()
