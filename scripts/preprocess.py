import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

# === Step 1: Set dataset path ===
DATA_PATH = '../datasets/cicids2017.csv'

# === Step 2: Load dataset safely ===
try:
    df = pd.read_csv(DATA_PATH, encoding='ISO-8859-1', sep=None, engine='python', on_bad_lines='skip')
    print(f"✅ Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns")

    # === Step 3: Clean column names ===
    df.columns = df.columns.str.strip()
    print("🧾 Columns in dataset:", df.columns.tolist())

    # === Step 4: Drop NA rows ===
    df = df.dropna()
    print(f"✅ After dropping NA, dataset has {df.shape[0]} rows")

    # === Step 5: Check and encode 'Label' ===
    if 'Label' not in df.columns:
        raise ValueError("❌ 'Label' column not found in dataset after cleaning.")

    le = LabelEncoder()
    df['Label'] = le.fit_transform(df['Label'])
    print(f"✅ Encoded labels: {list(le.classes_)}")

    # === Step 6: Split and Save ===
    X = df.drop(columns=['Label'])
    y = df['Label']

    os.makedirs('../datasets', exist_ok=True)
    X.to_csv('../datasets/X.csv', index=False)
    y.to_csv('../datasets/y.csv', index=False)
    print("✅ Preprocessed data saved to ../datasets/X.csv and y.csv")

except Exception as e:
    print(f"❌ Failed to preprocess dataset: {e}")
