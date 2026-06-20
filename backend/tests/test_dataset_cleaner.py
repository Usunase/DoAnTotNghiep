"""Kiểm thử pipeline lọc dữ liệu trước train."""
import pandas as pd
import pytest

from backend.dataset_cleaner import (
    add_segmented_column,
    filter_dataset,
    fill_missing_text_columns,
)


@pytest.fixture()
def sample_df():
    return pd.DataFrame(
        {
            "title": ["A", "B", "C", "D", "E"],
            "content": [
                "một hai ba bốn năm sáu",  # ok
                "hai ba",  # quá ngắn
                None,  # thiếu content
                "một hai ba bốn năm sáu",  # trùng
                "sáu bảy tám chín mười một",  # ok
            ],
            "is_fake": [False, True, False, True, False],
        }
    )


def test_filter_dataset_removes_short_missing_and_duplicates(sample_df):
    out = filter_dataset(sample_df, min_words=5)
    assert len(out) == 2
    assert out["content"].is_unique


def test_fill_missing_text_columns(sample_df):
    out = fill_missing_text_columns(sample_df)
    assert out["title"].isna().sum() == 0
    assert out["content"].fillna("").eq("").sum() >= 1


def test_add_segmented_column_creates_pyvi_tokens(sample_df):
    filtered = filter_dataset(sample_df)
    out = add_segmented_column(filtered)
    assert "content_segmented" in out.columns
    assert all(len(str(x)) > 0 for x in out["content_segmented"])
