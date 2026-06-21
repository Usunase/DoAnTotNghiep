# Kaggle PhoBERT fine-tuning notebook code
#
# Copy this file into a Kaggle notebook cell-by-cell, or paste it into one cell.
# It expects the four Kaggle datasets to be attached under /kaggle/input.

# %% [markdown]
# # PhoBERT Fake News Fine-tuning
#
# Label convention:
#
# ```text
# 0 = REAL
# 1 = FAKE
# ```

# %%
!pip -q install pyvi openpyxl accelerate transformers scikit-learn

# %%
from __future__ import annotations

import json
import os
import random
import re
import shutil
import string
import inspect
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from pyvi import ViTokenizer
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight
from torch import nn
from torch.utils.data import Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

SEED = 42
MODEL_NAME = "vinai/phobert-base"
MAX_LEN = 256
TEST_SIZE = 0.12
VAL_SIZE = 0.12
OUTPUT_DIR = Path("/kaggle/working/phobert-fakenews-final")
MERGED_CSV = Path("/kaggle/working/merged_fake_news_dataset.csv")

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device:", device)
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
else:
    print("WARNING: GPU is not enabled. Turn on Kaggle Notebook > Accelerator > GPU.")


# %%
INPUT_ROOT = Path("/kaggle/input")


def find_one(filename: str) -> Path:
    matches = sorted(INPUT_ROOT.rglob(filename))
    if not matches:
        raise FileNotFoundError(f"Cannot find {filename} under {INPUT_ROOT}")
    return matches[0]


def find_all(filename: str) -> list[Path]:
    return sorted(INPUT_ROOT.rglob(filename))


def normalize_text(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split()).strip()


def make_frame(
    df: pd.DataFrame,
    *,
    text_col: str,
    label,
    dataset_name: str,
    original_file: Path,
    title_col: str | None = None,
    url_col: str | None = None,
    source_col: str | None = None,
) -> pd.DataFrame:
    out = pd.DataFrame()
    out["text"] = df[text_col].map(normalize_text)
    out["label"] = label(df) if callable(label) else int(label)
    out["title"] = df[title_col].fillna("").astype(str) if title_col in df.columns else ""
    out["url"] = df[url_col].fillna("").astype(str) if url_col in df.columns else ""
    out["source"] = df[source_col].fillna("").astype(str) if source_col in df.columns else dataset_name
    out["dataset_name"] = dataset_name
    out["original_file"] = str(original_file.relative_to(INPUT_ROOT))
    return out


frames: list[pd.DataFrame] = []

# Dataset 1: phngnguynthu1803/vietnamese-fake-news-dataset
# These files are real-news files. Their internal label column is not reused.
for name in ["real_news.csv", "real_news_5500_balanced.csv"]:
    path = find_one(name)
    df_raw = pd.read_csv(path)
    frames.append(
        make_frame(
            df_raw,
            text_col="content",
            label=0,
            dataset_name="phngnguynthu1803/vietnamese-fake-news-dataset",
            original_file=path,
            title_col="title",
            url_col="url",
            source_col="source",
        )
    )
    print("Loaded", path, df_raw.shape)

# Dataset 2: chuynvinquc/fakenewvn
path = find_one("public_train.csv")
df_raw = pd.read_csv(path)
frames.append(
    make_frame(
        df_raw,
        text_col="post_message",
        label=lambda d: d["label"].astype(int),
        dataset_name="chuynvinquc/fakenewvn",
        original_file=path,
    )
)
print("Loaded", path, df_raw.shape)

path = find_one("warmup_training_dataset.xlsx")
df_raw = pd.read_excel(path)
frames.append(
    make_frame(
        df_raw,
        text_col="post_message",
        label=lambda d: d["label"].astype(int),
        dataset_name="chuynvinquc/fakenewvn",
        original_file=path,
    )
)
print("Loaded", path, df_raw.shape)

# Dataset 3: goumanguyen/vietnamese-fake-news-dataset-pbl7
# Load all PBL7 CSVs, then exact-text dedup will remove duplicated origin/update rows.
for filename in ["train_data.csv", "val_data.csv", "fix_test_data.csv", "update_train_data.csv", "update_val_data.csv"]:
    for path in find_all(filename):
        if "pbl7" not in str(path).lower() and "fake-news-dataset-pbl7" not in str(path).lower():
            continue
        df_raw = pd.read_csv(path)
        if {"Maintext", "Label"}.issubset(df_raw.columns):
            frames.append(
                make_frame(
                    df_raw,
                    text_col="Maintext",
                    label=lambda d: d["Label"].astype(int),
                    dataset_name="goumanguyen/vietnamese-fake-news-dataset-pbl7",
                    original_file=path,
                )
            )
            print("Loaded", path, df_raw.shape)

# Dataset 4: leviettrieu369/vietnamese-medical-fake-news-dataset
# Use raw content, not normalized_content, then apply one consistent PhoBERT preprocessing step.
path = find_one("full_dataset.csv")
df_raw = pd.read_csv(path)
frames.append(
    make_frame(
        df_raw,
        text_col="content",
        label=lambda d: d["is_fake"].astype(bool).astype(int),
        dataset_name="leviettrieu369/vietnamese-medical-fake-news-dataset",
        original_file=path,
        title_col="title",
        url_col="url",
        source_col="source",
    )
)
print("Loaded", path, df_raw.shape)

df = pd.concat(frames, ignore_index=True)
df["text"] = df["text"].map(normalize_text)
df = df[df["text"].str.len() > 20].copy()

# Remove exact duplicates. If the same text has conflicting labels, drop it.
df["_dedup_key"] = df["text"].str.casefold()
label_nunique = df.groupby("_dedup_key")["label"].nunique()
conflicting_keys = set(label_nunique[label_nunique > 1].index)
if conflicting_keys:
    print("Dropping conflicting duplicate texts:", len(conflicting_keys))
    df = df[~df["_dedup_key"].isin(conflicting_keys)].copy()

before = len(df)
df = df.drop_duplicates(subset=["_dedup_key"], keep="first").drop(columns=["_dedup_key"])
df = df.sample(frac=1, random_state=SEED).reset_index(drop=True)

print("Removed exact duplicates:", before - len(df))
print("Final shape:", df.shape)
print("Label counts:")
print(df["label"].value_counts().sort_index().rename(index={0: "REAL", 1: "FAKE"}))
print("Dataset x label:")
display(pd.crosstab(df["dataset_name"], df["label"], margins=True))

df.to_csv(MERGED_CSV, index=False, encoding="utf-8-sig")
print("Saved merged CSV:", MERGED_CSV)


# %%
URL_PATTERN = re.compile(r"http[s]?://\S+", re.IGNORECASE)
MULTISPACE_PATTERN = re.compile(r"\s+")


def clean_and_segment(text: str) -> str:
    text = str(text).lower()
    text = URL_PATTERN.sub(" ", text)
    # Keep digits and punctuation mostly intact. PhoBERT can handle punctuation,
    # and removing all punctuation can damage abbreviations and pre-segmented tokens.
    text = MULTISPACE_PATTERN.sub(" ", text).strip()
    if not text:
        return ""
    return ViTokenizer.tokenize(text)


print("Segmenting text with PyVi...")
df["text_processed"] = df["text"].map(clean_and_segment)
df = df[df["text_processed"].str.len() > 0].reset_index(drop=True)
print("After segmentation:", df.shape)


# %%
# Stratified split: train / validation / test.
train_df, temp_df = train_test_split(
    df,
    test_size=TEST_SIZE + VAL_SIZE,
    random_state=SEED,
    stratify=df["label"],
)

relative_test_size = TEST_SIZE / (TEST_SIZE + VAL_SIZE)
val_df, test_df = train_test_split(
    temp_df,
    test_size=relative_test_size,
    random_state=SEED,
    stratify=temp_df["label"],
)

train_df = train_df.reset_index(drop=True)
val_df = val_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)

print("Train:", train_df.shape, train_df["label"].value_counts().to_dict())
print("Val  :", val_df.shape, val_df["label"].value_counts().to_dict())
print("Test :", test_df.shape, test_df["label"].value_counts().to_dict())

train_df.to_csv("/kaggle/working/train_split.csv", index=False, encoding="utf-8-sig")
val_df.to_csv("/kaggle/working/val_split.csv", index=False, encoding="utf-8-sig")
test_df.to_csv("/kaggle/working/test_split.csv", index=False, encoding="utf-8-sig")


# %%
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


class FakeNewsDataset(Dataset):
    def __init__(self, texts: list[str], labels: list[int]):
        self.texts = texts
        self.labels = labels

    def __len__(self) -> int:
        return len(self.texts)

    def __getitem__(self, idx: int) -> dict[str, torch.Tensor]:
        enc = tokenizer(
            self.texts[idx],
            max_length=MAX_LEN,
            truncation=True,
            padding="max_length",
            return_tensors="pt",
        )
        return {
            "input_ids": enc["input_ids"].squeeze(0),
            "attention_mask": enc["attention_mask"].squeeze(0),
            "labels": torch.tensor(int(self.labels[idx]), dtype=torch.long),
        }


train_dataset = FakeNewsDataset(train_df["text_processed"].tolist(), train_df["label"].tolist())
val_dataset = FakeNewsDataset(val_df["text_processed"].tolist(), val_df["label"].tolist())
test_dataset = FakeNewsDataset(test_df["text_processed"].tolist(), test_df["label"].tolist())


# %%
class_weights = compute_class_weight(
    class_weight="balanced",
    classes=np.array([0, 1]),
    y=train_df["label"].to_numpy(),
)
class_weights = torch.tensor(class_weights, dtype=torch.float)
print("Class weights [REAL, FAKE]:", class_weights.tolist())


class WeightedTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs.pop("labels")
        outputs = model(**inputs)
        weights = class_weights.to(outputs.logits.device)
        loss = nn.CrossEntropyLoss(weight=weights)(outputs.logits, labels)
        return (loss, outputs) if return_outputs else loss


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "precision": precision_score(labels, preds, zero_division=0),
        "recall": recall_score(labels, preds, zero_division=0),
        "f1": f1_score(labels, preds, zero_division=0),
    }


model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

training_args_kwargs = dict(
    output_dir="/kaggle/working/phobert-checkpoints",
    num_train_epochs=3,
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    warmup_ratio=0.06,
    weight_decay=0.01,
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    greater_is_better=True,
    logging_steps=100,
    save_total_limit=2,
    fp16=torch.cuda.is_available(),
    report_to="none",
    seed=SEED,
)

training_args_signature = inspect.signature(TrainingArguments.__init__).parameters
if "eval_strategy" in training_args_signature:
    training_args_kwargs["eval_strategy"] = "epoch"
else:
    training_args_kwargs["evaluation_strategy"] = "epoch"

training_args = TrainingArguments(**training_args_kwargs)

trainer = WeightedTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

trainer.train()


# %%
print("Validation metrics:")
print(trainer.evaluate(val_dataset))

print("Test metrics:")
test_metrics = trainer.evaluate(test_dataset)
print(test_metrics)

with open("/kaggle/working/test_metrics.json", "w", encoding="utf-8") as f:
    json.dump(test_metrics, f, indent=2, ensure_ascii=False)


# %%
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
trainer.save_model(str(OUTPUT_DIR))
tokenizer.save_pretrained(str(OUTPUT_DIR))

metadata = {
    "model_name": MODEL_NAME,
    "label_map": {"0": "REAL", "1": "FAKE"},
    "max_len": MAX_LEN,
    "seed": SEED,
    "train_rows": len(train_df),
    "val_rows": len(val_df),
    "test_rows": len(test_df),
    "test_metrics": test_metrics,
}
with open(OUTPUT_DIR / "training_metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2, ensure_ascii=False)

zip_base = "/kaggle/working/phobert-fakenews-final"
zip_path = shutil.make_archive(zip_base, "zip", OUTPUT_DIR)

print("Saved model directory:", OUTPUT_DIR)
print("Saved downloadable zip:", zip_path)
