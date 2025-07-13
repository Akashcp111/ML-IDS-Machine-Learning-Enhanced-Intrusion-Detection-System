import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import numpy as np
import os

# === Step 1: Load preprocessed data ===
try:
    X = pd.read_csv('../datasets/X.csv')
    y = pd.read_csv('../datasets/y.csv').squeeze()

    print(f"✅ Loaded features: {X.shape}, labels: {y.shape}")

    # === Step 2: Clean Data ===
    # Replace inf, -inf with NaN
    X.replace([np.inf, -np.inf], np.nan, inplace=True)
    # Drop rows with NaN
    X.dropna(inplace=True)
    y = y[X.index]  # keep labels in sync
    print("✅ Removed inf and NaN values.")

    # === Step 3: Split Dataset ===
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    print("✅ Split into train and test sets.")

    # === Step 4: Train Model ===
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("✅ Model trained successfully.")

    # === Step 5: Evaluate ===
    y_pred = model.predict(X_test)
    print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))
    print("📉 Accuracy Score:", accuracy_score(y_test, y_pred))

    # === Step 6: Save Model ===
    os.makedirs('../models', exist_ok=True)
    joblib.dump(model, '../models/rf_model.joblib')
    print("✅ Model saved to ../models/rf_model.joblib")

except Exception as e:
    print(f"❌ Error: {e}")
