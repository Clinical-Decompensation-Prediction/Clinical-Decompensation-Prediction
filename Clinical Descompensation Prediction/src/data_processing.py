"""Data loading and feature construction utilities.
Follows PEP8 and keeps side-effect free functions for reuse.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from typing import Dict, Tuple

def load_dataset(path: str) -> pd.DataFrame:
    """Load CSV dataset and ensure a multiclass target is present.

    If 'target' is missing, derive it from ('diabetes', 'hypertension'):
        -1: no disease
         0: diabetes
         1: hypertension
         2: comorbidity (diabetes + hypertension)

    Args:
        path: Path to CSV.

    Returns:
        DataFrame with consistent sorting and 'target' column.
    """
    df = pd.read_csv(path)
    if "target" not in df.columns:
        if {"diabetes", "hypertension"}.issubset(df.columns):
            tmp = df["diabetes"].astype(int) + 2 * df["hypertension"].astype(int)
            df["target"] = tmp.map({0: -1, 1: 0, 2: 1, 3: 2})
        else:
            raise ValueError("El dataset no tiene 'target' ni ('diabetes','hypertension').")

    if "patient_id" in df.columns:
        df["patient_id"] = df["patient_id"].astype(int)

    if "visit" in df.columns and "patient_id" in df.columns:
        df = df.sort_values(["patient_id", "visit"])
    elif "patient_id" in df.columns:
        df = df.sort_values(["patient_id"])

    df.reset_index(drop=True, inplace=True)
    return df

def build_feature_table(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series, Dict[str, Tuple[float, float]]]:
    """Select robust clinical features and compute bounds.

    Required columns: age, blood_glucose_level, HbA1c_level, systolic_bp, diastolic_bp, bmi, target.

    Returns:
        X: Feature matrix
        y: Target series (int)
        bounds: Percentile (1,99) ranges per feature for UI inputs
    """
    cols_needed = ["age", "blood_glucose_level", "HbA1c_level",
                   "systolic_bp", "diastolic_bp", "bmi", "target"]
    missing = [c for c in cols_needed if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {missing}")

    df = df.copy()
    df["pulse_pressure"] = df["systolic_bp"] - df["diastolic_bp"]

    feature_cols = [
        "age", "blood_glucose_level", "HbA1c_level",
        "systolic_bp", "diastolic_bp", "bmi", "pulse_pressure"
    ]
    X = df[feature_cols].copy()
    y = df["target"].round().astype(int).copy()

    bounds = {}
    for c in feature_cols:
        lo = float(np.nanpercentile(X[c], 1))
        hi = float(np.nanpercentile(X[c], 99))
        bounds[c] = (lo, hi)

    return X, y, bounds
