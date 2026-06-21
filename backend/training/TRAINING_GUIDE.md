# Huong dan train lai model PhoBERT

Pipeline hien tai dung toan bo du lieu trong thu muc `last/`, chuan hoa ve mot file CSV chung, sau do train model backend theo kien truc:

```text
PhoBERT frozen embedding -> StandardScaler -> MLPClassifier
```

Backend inference hien tai van dung hai artifact:

```text
backend/models/phobert_mlp_model.joblib
backend/models/phobert_scaler.joblib
```

## 1. Chuan bi moi truong

Tu thu muc root project:

```bash
cd /home/phanvantai/DoAnTotNghiep
pip install -r requirements.txt
```

Neu dung Jupyter Notebook, hay dam bao kernel dang chay dung Python environment da cai dependencies tren.

## 2. Kiem tra du lieu dau vao

Thu muc `last/` can co cac dataset Kaggle:

```text
last/Fake News Vietnamese Dataset/
last/Vietnamese Fake-News-Dataset-PBL7/
last/Vietnamese_fake_news_dataset/
last/Vietnamese medical fake news dataset/
```

Co the chay lenh merge rieng de kiem tra schema va phan bo nhan:

```bash
python3 -m backend.training.merge_last_datasets
```

Lenh nay tao file:

```text
backend/data/merged_fake_news_dataset.csv
```

Quy uoc nhan trong file merged:

```text
is_fake = False -> tin that
is_fake = True  -> tin gia
```

## 3. Chay notebook train

Mo notebook:

```text
backend/training/train_phobert_model.ipynb
```

Chay tu dau den cuoi.

Lan dau train voi dataset merged, dat:

```python
REBUILD_MERGED_DATASET = True
REGENERATE_EMBEDDINGS = True
RUN_EXPERIMENTS = True
```

Sau khi da co embedding cache va chi muon train lai MLP nhanh, co the dat:

```python
REBUILD_MERGED_DATASET = False
REGENERATE_EMBEDDINGS = False
RUN_EXPERIMENTS = True
```

## 4. Artifact duoc tao ra

Embedding cache moi:

```text
backend/models/phobert_merged_features.npy
backend/models/phobert_merged_labels.npy
```

Model backend se dung khi inference:

```text
backend/models/phobert_mlp_model.joblib
backend/models/phobert_scaler.joblib
```

Ket qua danh gia:

```text
backend/experiments/figures/experimental/metrics_summary.csv
backend/experiments/figures/experimental/cv_summary.csv
backend/experiments/figures/experimental/confusion_matrix_text_only.png
backend/experiments/figures/experimental/roc_curves.png
```

## 5. Luu y quan trong

Neu thay loi:

```text
Embedding cache khong khop dataset hien tai
```

hay dat:

```python
REGENERATE_EMBEDDINGS = True
```

Neu thay loi thieu `pyvi`, cai lai dependencies:

```bash
pip install -r requirements.txt
```

Dataset merged hien van lech nhan ve tin that nhieu hon tin gia. Notebook da dung `sample_weight='balanced'` cho MLP de giam thien lech nay, nhung metric random split chua du de ket luan model tot tren du lieu thuc te. Khi danh gia nghiem tuc, nen test them theo `source` hoac `dataset_name`.

