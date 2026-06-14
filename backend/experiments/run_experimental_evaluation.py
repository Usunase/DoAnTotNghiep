"""
Chương kết quả thực nghiệm: confusion matrix, text-only vs hybrid, ablation,
ROC/AUC và 5-fold cross-validation.
Chạy: python run_experimental_evaluation.py
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from backend.feature_extraction import ALL_META_COLS, add_metadata_features

PROJECT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PROJECT_DIR.parent.parent
MODELS_DIR = PROJECT_ROOT / "backend/models"
FIG_DIR = PROJECT_DIR / "figures" / "experimental"
DATA_PATH = PROJECT_ROOT / "backend/data/full_dataset.csv"
RANDOM_STATE = 42
TEST_SIZE = 0.3
CV_N_SPLITS = 5

# Mô hình dùng cho ROC/AUC và biểu đồ CV chính
PRIMARY_MODELS = [
    "1. Chỉ văn bản (PhoBERT)",
    "2. Hybrid đầy đủ (PhoBERT + 10 meta)",
]

MLP_KWARGS = dict(
    hidden_layer_sizes=(128, 64),
    activation="relu",
    solver="adam",
    max_iter=500,
    alpha=0.1,
    early_stopping=True,
    random_state=RANDOM_STATE,
)


def load_dataset():
    from backend.dataset_cleaner import fill_missing_text_columns, filter_dataset, load_raw_dataset

    df = filter_dataset(load_raw_dataset(DATA_PATH))
    df = fill_missing_text_columns(df)
    df = add_metadata_features(df, random_state=RANDOM_STATE)

    X_phobert = np.load(MODELS_DIR / "phobert_base_features.npy")
    y = np.load(MODELS_DIR / "phobert_base_labels.npy")
    meta = df[ALL_META_COLS].values.astype(np.float64)
    assert len(meta) == len(X_phobert) == len(y), "Số dòng không khớp giữa CSV và PhoBERT"
    return X_phobert, meta, y


def build_feature_sets(X_phobert: np.ndarray, meta: np.ndarray) -> dict[str, np.ndarray]:
    scaler_meta = StandardScaler()
    meta_scaled = scaler_meta.fit_transform(meta)
    user_scaled = scaler_meta.fit_transform(meta[:, :5])
    text_scaled = scaler_meta.fit_transform(meta[:, 5:])

    return {
        "1. Chỉ văn bản (PhoBERT)": X_phobert,
        "2. Hybrid đầy đủ (PhoBERT + 10 meta)": np.hstack((X_phobert, meta_scaled)),
        "3. PhoBERT + Metadata người dùng (5)": np.hstack((X_phobert, user_scaled)),
        "4. PhoBERT + Thống kê văn bản (5)": np.hstack((X_phobert, text_scaled)),
        "5. Chỉ metadata (10) — không PhoBERT": meta_scaled,
        "6. Chỉ metadata người dùng (5)": user_scaled,
        "7. Chỉ thống kê văn bản (5)": text_scaled,
    }


def make_pipeline() -> Pipeline:
    return Pipeline(
        [
            ("scaler", StandardScaler()),
            ("mlp", MLPClassifier(**MLP_KWARGS)),
        ]
    )


def train_and_evaluate(X: np.ndarray, y: np.ndarray) -> dict:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    pipe = make_pipeline()
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    y_proba = pipe.predict_proba(X_test)[:, 1]

    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1": f1_score(y_test, y_pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, y_proba),
        "y_test": y_test,
        "y_pred": y_pred,
        "y_proba": y_proba,
        "report": classification_report(y_test, y_pred, zero_division=0),
        "cm": confusion_matrix(y_test, y_pred),
        "fpr": None,
        "tpr": None,
    }


def add_roc_curve(res: dict) -> dict:
    fpr, tpr, _ = roc_curve(res["y_test"], res["y_proba"], pos_label=True)
    res["fpr"] = fpr
    res["tpr"] = tpr
    return res


def cross_validate_model(X: np.ndarray, y: np.ndarray) -> dict:
    """5-fold stratified CV; scaler fit trong từng fold (qua Pipeline)."""
    cv = StratifiedKFold(
        n_splits=CV_N_SPLITS, shuffle=True, random_state=RANDOM_STATE
    )
    scoring = {
        "accuracy": "accuracy",
        "precision": "precision",
        "recall": "recall",
        "f1": "f1",
        "roc_auc": "roc_auc",
    }
    pipe = make_pipeline()
    scores = cross_validate(
        pipe,
        X,
        y,
        cv=cv,
        scoring=scoring,
        n_jobs=1,
    )
    out = {}
    for metric in scoring:
        key = f"test_{metric}"
        vals = scores[key]
        out[f"{metric}_mean"] = float(np.mean(vals))
        out[f"{metric}_std"] = float(np.std(vals))
        out[f"{metric}_folds"] = vals.tolist()
    return out


def plot_confusion_matrix(cm, title: str, path: Path):
    fig, ax = plt.subplots(figsize=(5.5, 4.5))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Tin thật", "Tin giả"],
        yticklabels=["Tin thật", "Tin giả"],
        ax=ax,
        cbar_kws={"label": "Số mẫu"},
    )
    ax.set_xlabel("Dự đoán")
    ax.set_ylabel("Thực tế")
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_comparison_bars(df_metrics: pd.DataFrame, path: Path):
    main = df_metrics[df_metrics["model"].isin(
        ["1. Chỉ văn bản (PhoBERT)", "2. Hybrid đầy đủ (PhoBERT + 10 meta)"]
    )].copy()
    metrics = ["accuracy", "precision", "recall", "f1"]
    labels_vn = ["Accuracy", "Precision", "Recall", "F1-score"]
    x = np.arange(len(metrics))
    width = 0.35

    fig, ax = plt.subplots(figsize=(9, 5))
    for i, (_, row) in enumerate(main.iterrows()):
        vals = [row[m] for m in metrics]
        offset = (i - 0.5) * width
        bars = ax.bar(x + offset, vals, width, label=row["model"])
        for bar, v in zip(bars, vals):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.005,
                f"{v:.3f}",
                ha="center",
                va="bottom",
                fontsize=9,
            )

    ax.set_xticks(x)
    ax.set_xticklabels(labels_vn)
    ax.set_ylim(0, 1.08)
    ax.set_ylabel("Điểm số")
    ax.set_title("So sánh mô hình: Chỉ văn bản (PhoBERT) vs Hybrid")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_ablation(df_metrics: pd.DataFrame, path: Path):
    ablation_models = [
        "2. Hybrid đầy đủ (PhoBERT + 10 meta)",
        "3. PhoBERT + Metadata người dùng (5)",
        "4. PhoBERT + Thống kê văn bản (5)",
        "1. Chỉ văn bản (PhoBERT)",
        "5. Chỉ metadata (10) — không PhoBERT",
    ]
    sub = df_metrics[df_metrics["model"].isin(ablation_models)].copy()
    sub = sub.set_index("model").loc[ablation_models]
    short_names = [
        "Hybrid\n(đầy đủ)",
        "PhoBERT +\nUser meta",
        "PhoBERT +\nText stats",
        "Chỉ\nPhoBERT",
        "Chỉ\nmetadata",
    ]

    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = np.arange(len(sub))
    width = 0.2
    for i, metric in enumerate(["accuracy", "precision", "recall", "f1"]):
        ax.bar(x + (i - 1.5) * width, sub[metric], width, label=metric.capitalize())

    ax.set_xticks(x)
    ax.set_xticklabels(short_names, fontsize=9)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Điểm số")
    ax.set_title("Ablation study: vai trò từng nhóm đặc trưng metadata")
    ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(0.5, 1.12), fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_roc_curves(roc_data: list[tuple[str, dict]], path: Path):
    fig, ax = plt.subplots(figsize=(7, 6))
    colors = ["#2563eb", "#dc2626", "#16a34a", "#d97706"]

    for i, (name, res) in enumerate(roc_data):
        short = "PhoBERT" if "Chỉ văn bản" in name else "Hybrid"
        ax.plot(
            res["fpr"],
            res["tpr"],
            linewidth=2,
            color=colors[i % len(colors)],
            label=f"{short} (AUC = {res['roc_auc']:.4f})",
        )

    ax.plot([0, 1], [0, 1], "k--", linewidth=1, label="Ngẫu nhiên (AUC = 0.5)")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("Đường cong ROC — Tập kiểm thử (30%)")
    ax.legend(loc="lower right")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_cv_comparison(df_cv: pd.DataFrame, path: Path):
    sub = df_cv[df_cv["model"].isin(PRIMARY_MODELS)].copy()
    metrics = ["accuracy", "precision", "recall", "f1", "roc_auc"]
    labels_vn = ["Accuracy", "Precision", "Recall", "F1", "ROC-AUC"]
    x = np.arange(len(metrics))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 5.5))
    for i, (_, row) in enumerate(sub.iterrows()):
        means = [row[f"{m}_mean"] for m in metrics]
        stds = [row[f"{m}_std"] for m in metrics]
        offset = (i - 0.5) * width
        short = "PhoBERT" if "Chỉ văn bản" in row["model"] else "Hybrid"
        ax.bar(
            x + offset,
            means,
            width,
            yerr=stds,
            capsize=4,
            label=f"{short} (5-fold CV)",
        )

    ax.set_xticks(x)
    ax.set_xticklabels(labels_vn)
    ax.set_ylim(0, 1.12)
    ax.set_ylabel("Điểm số (mean ± std)")
    ax.set_title(f"5-fold Stratified Cross-Validation (k={CV_N_SPLITS})")
    ax.legend(loc="lower right")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_ablation_delta(df_metrics: pd.DataFrame, path: Path):
    text_only = df_metrics.loc[
        df_metrics["model"] == "1. Chỉ văn bản (PhoBERT)", "f1"
    ].values[0]
    hybrid = df_metrics.loc[
        df_metrics["model"] == "2. Hybrid đầy đủ (PhoBERT + 10 meta)", "f1"
    ].values[0]
    rows = [
        ("Hybrid đầy đủ", hybrid - text_only),
        ("Bỏ user meta → PhoBERT+text", 0),  # filled below
        ("Bỏ text stats → PhoBERT+user", 0),
    ]
    f1_p3 = df_metrics.loc[
        df_metrics["model"] == "3. PhoBERT + Metadata người dùng (5)", "f1"
    ].values[0]
    f1_p4 = df_metrics.loc[
        df_metrics["model"] == "4. PhoBERT + Thống kê văn bản (5)", "f1"
    ].values[0]
    rows[1] = ("PhoBERT + user meta (5)", f1_p3 - text_only)
    rows[2] = ("PhoBERT + text stats (5)", f1_p4 - text_only)

    names = [r[0] for r in rows]
    deltas = [r[1] for r in rows]
    colors = ["#2563eb" if d >= 0 else "#dc2626" for d in deltas]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.barh(names, deltas, color=colors)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.axvline(hybrid - text_only, color="#16a34a", linestyle="--", alpha=0.5, label="Δ F1 Hybrid vs Text-only")
    ax.set_xlabel("Δ F1-score so với baseline PhoBERT")
    ax.set_title("Đóng góp metadata vào F1 (so với chỉ PhoBERT)")
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid", font_scale=1.05)

    X_phobert, meta, y = load_dataset()
    feature_sets = build_feature_sets(X_phobert, meta)

    rows = []
    roc_store = []
    cv_rows = []

    print("=" * 60)
    print("CHƯƠNG KẾT QUẢ THỰC NGHIỆM")
    print(f"Tập test: {TEST_SIZE*100:.0f}% | random_state={RANDOM_STATE}")
    print(f"Cross-validation: {CV_N_SPLITS}-fold stratified")
    print("=" * 60)

    for name, X in feature_sets.items():
        print(f"\n>>> {name}")
        res = add_roc_curve(train_and_evaluate(X, y))
        rows.append(
            {
                "model": name,
                "n_features": X.shape[1],
                "accuracy": res["accuracy"],
                "precision": res["precision"],
                "recall": res["recall"],
                "f1": res["f1"],
                "roc_auc": res["roc_auc"],
            }
        )
        print(res["report"])
        print(f"ROC-AUC (hold-out): {res['roc_auc']:.4f}")

        if name in PRIMARY_MODELS:
            roc_store.append((name, res))

        if name in (
            "1. Chỉ văn bản (PhoBERT)",
            "2. Hybrid đầy đủ (PhoBERT + 10 meta)",
        ):
            safe = "text_only" if "Chỉ văn bản" in name else "hybrid_full"
            plot_confusion_matrix(
                res["cm"],
                f"Confusion Matrix — {name}",
                FIG_DIR / f"confusion_matrix_{safe}.png",
            )

    df_metrics = pd.DataFrame(rows)
    df_metrics.to_csv(FIG_DIR / "metrics_summary.csv", index=False)
    with open(FIG_DIR / "metrics_summary.json", "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    plot_comparison_bars(df_metrics, FIG_DIR / "comparison_text_vs_hybrid.png")
    plot_ablation(df_metrics, FIG_DIR / "ablation_metadata_groups.png")
    plot_ablation_delta(df_metrics, FIG_DIR / "ablation_f1_delta.png")
    plot_roc_curves(roc_store, FIG_DIR / "roc_curves.png")

    # --- 5-fold Cross-Validation (toàn bộ mô hình) ---
    print("\n" + "=" * 60)
    print(f"5-FOLD CROSS-VALIDATION (k={CV_N_SPLITS})")
    print("=" * 60)

    for name, X in feature_sets.items():
        print(f"\n>>> CV: {name}")
        cv_res = cross_validate_model(X, y)
        row = {"model": name, "n_features": X.shape[1], **cv_res}
        cv_rows.append(row)
        print(
            f"  Accuracy : {cv_res['accuracy_mean']:.4f} ± {cv_res['accuracy_std']:.4f}\n"
            f"  F1       : {cv_res['f1_mean']:.4f} ± {cv_res['f1_std']:.4f}\n"
            f"  ROC-AUC  : {cv_res['roc_auc_mean']:.4f} ± {cv_res['roc_auc_std']:.4f}"
        )

    df_cv = pd.DataFrame(cv_rows)
    df_cv.to_csv(FIG_DIR / "cv_summary.csv", index=False)
    with open(FIG_DIR / "cv_summary.json", "w", encoding="utf-8") as f:
        json.dump(cv_rows, f, indent=2, ensure_ascii=False)
    plot_cv_comparison(df_cv, FIG_DIR / "cv_5fold_comparison.png")

    # Bảng markdown in ra console
    print("\n" + "=" * 60)
    print("BẢNG TỔNG HỢP (HOLD-OUT 30%)")
    print("=" * 60)
    print(df_metrics.to_string(index=False, float_format=lambda x: f"{x:.4f}"))
    print("\n" + "=" * 60)
    print("BẢNG CV (MEAN ± STD)")
    print("=" * 60)
    cv_display = df_cv[
        ["model", "accuracy_mean", "accuracy_std", "f1_mean", "f1_std", "roc_auc_mean", "roc_auc_std"]
    ]
    print(cv_display.to_string(index=False, float_format=lambda x: f"{x:.4f}"))
    print(f"\n[+] Đã lưu biểu đồ tại: {FIG_DIR}")
    print("[+] metrics_summary.csv / cv_summary.csv / roc_curves.png")


if __name__ == "__main__":
    main()
