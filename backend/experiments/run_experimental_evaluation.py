"""
Đánh giá mô hình PhoBERT + MLP (text-only):
- Hold-out 30%
- ROC/AUC
- 5-fold cross-validation
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
from sklearn.utils.class_weight import compute_sample_weight

PROJECT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PROJECT_DIR.parent.parent
MODELS_DIR = PROJECT_ROOT / "backend/models"
FIG_DIR = PROJECT_DIR / "figures" / "experimental"
FEATURES_PATH = MODELS_DIR / "phobert_merged_features.npy"
LABELS_PATH = MODELS_DIR / "phobert_merged_labels.npy"
RANDOM_STATE = 42
TEST_SIZE = 0.3
CV_N_SPLITS = 5

MLP_KWARGS = dict(
    hidden_layer_sizes=(128, 64),
    activation="relu",
    solver="adam",
    max_iter=500,
    alpha=0.1,
    early_stopping=True,
    random_state=RANDOM_STATE,
)


def load_dataset() -> tuple[np.ndarray, np.ndarray]:
    X = np.load(FEATURES_PATH)
    y = np.load(LABELS_PATH)
    return X, y


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
    sample_weights = compute_sample_weight(class_weight="balanced", y=y_train)
    try:
        pipe.fit(X_train, y_train, mlp__sample_weight=sample_weights)
    except TypeError:
        pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    y_proba = pipe.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_proba, pos_label=True)

    return {
        "model": "PhoBERT text-only",
        "n_features": int(X.shape[1]),
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, zero_division=0)),
        "f1": float(f1_score(y_test, y_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_test, y_proba)),
        "report": classification_report(y_test, y_pred, zero_division=0),
        "cm": confusion_matrix(y_test, y_pred),
        "fpr": fpr,
        "tpr": tpr,
    }


def cross_validate_model(X: np.ndarray, y: np.ndarray) -> dict:
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
    scores = cross_validate(
        make_pipeline(),
        X,
        y,
        cv=cv,
        scoring=scoring,
        n_jobs=1,
    )
    out = {}
    for metric in scoring:
        vals = scores[f"test_{metric}"]
        out[f"{metric}_mean"] = float(np.mean(vals))
        out[f"{metric}_std"] = float(np.std(vals))
        out[f"{metric}_folds"] = vals.tolist()
    return out


def plot_confusion_matrix(cm: np.ndarray, path: Path):
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
    ax.set_title("Confusion Matrix — PhoBERT text-only")
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_roc_curve(fpr: np.ndarray, tpr: np.ndarray, roc_auc: float, path: Path):
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.plot(fpr, tpr, linewidth=2, color="#2563eb", label=f"PhoBERT (AUC = {roc_auc:.4f})")
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


def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid", font_scale=1.05)

    X, y = load_dataset()
    holdout = train_and_evaluate(X, y)
    cv = cross_validate_model(X, y)

    metrics_row = {
        k: holdout[k]
        for k in ["model", "n_features", "accuracy", "precision", "recall", "f1", "roc_auc"]
    }
    cv_row = {"model": holdout["model"], "n_features": holdout["n_features"], **cv}

    pd.DataFrame([metrics_row]).to_csv(FIG_DIR / "metrics_summary.csv", index=False)
    pd.DataFrame([cv_row]).to_csv(FIG_DIR / "cv_summary.csv", index=False)

    with open(FIG_DIR / "metrics_summary.json", "w", encoding="utf-8") as f:
        json.dump([metrics_row], f, indent=2, ensure_ascii=False)
    with open(FIG_DIR / "cv_summary.json", "w", encoding="utf-8") as f:
        json.dump([cv_row], f, indent=2, ensure_ascii=False)

    plot_confusion_matrix(holdout["cm"], FIG_DIR / "confusion_matrix_text_only.png")
    plot_roc_curve(holdout["fpr"], holdout["tpr"], holdout["roc_auc"], FIG_DIR / "roc_curves.png")

    print("=" * 60)
    print("ĐÁNH GIÁ MÔ HÌNH PHOBERT TEXT-ONLY")
    print("=" * 60)
    print(holdout["report"])
    print(f"ROC-AUC (hold-out): {holdout['roc_auc']:.4f}")
    print(
        f"CV F1: {cv['f1_mean']:.4f} ± {cv['f1_std']:.4f} | "
        f"CV ROC-AUC: {cv['roc_auc_mean']:.4f} ± {cv['roc_auc_std']:.4f}"
    )
    print(f"[+] Đã lưu biểu đồ tại: {FIG_DIR}")


if __name__ == "__main__":
    main()
