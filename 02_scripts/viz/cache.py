import hashlib
import pandas as pd
from pathlib import Path

def hash_df(df):
    return hashlib.md5(pd.util.hash_pandas_object(df, index=True).values).hexdigest()

def is_cached(df, output_path: Path):
    if not output_path.exists():
        return False
    meta_path = output_path.with_suffix(".meta")
    if not meta_path.exists():
        return False
    with open(meta_path) as f:
        saved_hash = f.read().strip()
    return saved_hash == hash_df(df)

def save_cache(df, output_path: Path):
    meta_path = output_path.with_suffix(".meta")
    meta_path.write_text(hash_df(df))