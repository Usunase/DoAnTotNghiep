"""
Làm sạch và chuẩn bị bộ dữ liệu trước khi train (PhoBERT + MLP).

Gom logic từ notebook `train_phobert_model.ipynb` (Phần 1 + tách từ Phần 2).

Chạy độc lập:
    python -m backend.dataset_cleaner
    python -m backend.dataset_cleaner --input backend/data/full_dataset.csv --output backend/data/full_dataset_cleaned.csv
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from backend.text_utils import preprocess_text

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = PROJECT_ROOT / "backend/data/full_dataset.csv"
DEFAULT_OUTPUT = PROJECT_ROOT / "backend/data/full_dataset_cleaned.csv"


def load_raw_dataset(csv_path: Path | str = DEFAULT_INPUT) -> pd.DataFrame:
    """Đọc file CSV gốc."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Không tìm thấy dataset: {path}")
    return pd.read_csv(path)


def filter_dataset(df: pd.DataFrame, min_words: int = 5) -> pd.DataFrame:
    """
    Lọc dữ liệu thô:
    - Bỏ dòng thiếu content
    - Bỏ bài quá ngắn (< min_words từ)
    - Bỏ trùng nội dung
    """
    out = df.copy()
    out = out.dropna(subset=["content"])
    out = out[out["content"].astype(str).str.split().str.len() > min_words]
    out = out.drop_duplicates(subset=["content"])
    return out.reset_index(drop=True)


def fill_missing_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Điền title/content rỗng bằng chuỗi trống."""
    out = df.copy()
    if "title" in out.columns:
        out["title"] = out["title"].fillna("")
    out["content"] = out["content"].fillna("")
    return out


def segment_text(text: str) -> str:
    """Alias tương thích — gọi `preprocess_text` trong text_utils."""
    return preprocess_text(text)


def add_segmented_column(
    df: pd.DataFrame,
    source_col: str = "content",
    target_col: str = "content_segmented",
) -> pd.DataFrame:
    """Thêm cột văn bản đã tách từ."""
    out = df.copy()
    out[target_col] = out[source_col].apply(segment_text)
    # Bỏ dòng rỗng sau khi làm sạch
    out = out[out[target_col].str.len() > 0].reset_index(drop=True)
    return out


def prepare_training_dataset(
    csv_path: Path | str = DEFAULT_INPUT,
    min_words: int = 5,
    add_segmented: bool = True,
) -> pd.DataFrame:
    """
    Pipeline đầy đủ: nạp → lọc → fillna → (tùy chọn) tách từ.
  """
    df = load_raw_dataset(csv_path)
    n_raw = len(df)

    df = filter_dataset(df, min_words=min_words)
    df = fill_missing_text_columns(df)

    if add_segmented:
        df = add_segmented_column(df)

    print(f"[dataset_cleaner] Gốc: {n_raw} dòng → sau lọc: {len(df)} dòng")
    return df


def save_cleaned_dataset(
    df: pd.DataFrame,
    output_path: Path | str = DEFAULT_OUTPUT,
) -> Path:
    """Lưu CSV đã làm sạch."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print(f"[dataset_cleaner] Đã lưu: {path}")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Làm sạch full_dataset.csv trước khi train")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="CSV đầu vào")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="CSV đầu ra")
    parser.add_argument("--min-words", type=int, default=5, help="Số từ tối thiểu mỗi bài")
    parser.add_argument(
        "--no-segment",
        action="store_true",
        help="Chỉ lọc, không tạo cột content_segmented",
    )
    args = parser.parse_args()

    df = prepare_training_dataset(
        csv_path=args.input,
        min_words=args.min_words,
        add_segmented=not args.no_segment,
    )
    save_cleaned_dataset(df, args.output)

    if "content_segmented" in df.columns:
        sample = df[["content", "content_segmented"]].head(2)
        print("\nMẫu sau làm sạch:")
        print(sample.to_string(index=False))


if __name__ == "__main__":
    main()
