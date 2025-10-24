"""Training utilities and optional CLI to persist models."""
from __future__ import annotations
import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

from .data_processing import load_dataset, build_feature_table
from .model import create_model

def train_model(model, imputer, X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    X_train_imp = imputer.fit_transform(X_train)
    X_test_imp = imputer.transform(X_test)

    model.fit(X_train_imp, y_train)
    y_pred = model.predict(X_test_imp)
    y_proba = model.predict_proba(X_test_imp)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision_macro": precision_score(y_test, y_pred, average="macro"),
        "recall_macro": recall_score(y_test, y_pred, average="macro"),
        "f1_macro": f1_score(y_test, y_pred, average="macro"),
        "report": classification_report(y_test, y_pred, output_dict=True),
        "cm": confusion_matrix(y_test, y_pred, labels=[-1, 0, 1, 2])
    }

    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)

    return model, imputer, metrics, importances, (X_train, X_test, y_train, y_test, y_pred, y_proba)

def save_models(model, imputer, out_dir: str = "models"):
    os.makedirs(out_dir, exist_ok=True)
    joblib.dump(model, os.path.join(out_dir, "best_model.pkl"))
    joblib.dump(model, os.path.join(out_dir, "model_v1.pkl"))
    joblib.dump(imputer, os.path.join(out_dir, "imputer.pkl"))
    return {
        "best_model": os.path.join(out_dir, "best_model.pkl"),
        "model_v1": os.path.join(out_dir, "model_v1.pkl"),
        "imputer": os.path.join(out_dir, "imputer.pkl"),
    }

if __name__ == "__main__":
    # Optional CLI: python -m src.train path/to/dataset.csv
    import argparse
    parser = argparse.ArgumentParser(description="Train and persist RandomForest model.")
    parser.add_argument("--data", type=str, default="dataset_balanceado_SMOTEENN.csv", help="Path to CSV dataset")
    parser.add_argument("--out", type=str, default="models", help="Output models directory")
    args = parser.parse_args()

    df = load_dataset(args.data)
    X, y, _ = build_feature_table(df)
    model, imputer = create_model()
    model, imputer, metrics, importances, _ = train_model(model, imputer, X, y)
    paths = save_models(model, imputer, out_dir=args.out)
    print("Saved:", paths)
    print("Metrics:", {k: float(v) if isinstance(v, (int, float)) else v for k, v in metrics.items() if k != "report"})
