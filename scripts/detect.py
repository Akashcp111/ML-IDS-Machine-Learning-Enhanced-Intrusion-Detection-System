# detect.py
import pandas as pd
import joblib
import numpy as np

# === Step 1: Load Trained Model ===
try:
    model = joblib.load('../models/rf_model.joblib')
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    exit()

# === Step 2: Load Sample Data to Predict ===
try:
    new_data = pd.read_csv('../datasets/X.csv').sample(5)  # Change this as needed
    print(f"✅ Loaded {new_data.shape[0]} new data rows.")
except Exception as e:
    print(f"❌ Failed to load input data: {e}")
    exit()

# === Step 3: Clean Input ===
new_data.replace([np.inf, -np.inf], np.nan, inplace=True)
new_data.dropna(inplace=True)

# === Step 4: Predict ===
try:
    predictions = model.predict(new_data)
    print("🔍 Predictions:")
    print(predictions)

    # Optional: Map 0 → BENIGN, 1 → ATTACK
    label_map = {0: 'BENIGN', 1: 'ATTACK'}
    readable = [label_map.get(p, 'Unknown') for p in predictions]
    print("🧾 Interpreted Output:", readable)
except Exception as e:
    print(f"❌ Prediction failed: {e}")
