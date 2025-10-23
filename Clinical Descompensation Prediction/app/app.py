import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import os
import time
import numpy as np
import pandas as pd
import streamlit as st

from src.data_processing import load_dataset, build_feature_table
from src.model import create_model
from src.train import train_model
from src.utils import generar_reporte_pdf

st.set_page_config(page_title="Predicción Clínica", page_icon="🩺", layout="wide")
st.title("🧠 Sistema de Predicción Clínica")
st.caption("Modelo RandomForest balanceado | Entrenamiento y simulación clínica")


DATA_PATH = "dataset_balanceado_SMOTEENN.csv"

with st.status("Cargando datos y entrenando el modelo...", expanded=True) as status:
    st.write("📥 Cargando dataset…")
    df = load_dataset(DATA_PATH)
    st.write(f"✔️ Dataset cargado: {df.shape[0]:,} filas, {df.shape[1]} columnas")

    st.write("🧱 Construyendo tabla de features…")
    X, y, bounds = build_feature_table(df)

    st.write("🧠 Entrenando modelo (RandomForest)…")
    start = time.time()
    model, imputer = create_model()
    model, imputer, metrics, importances, sets = train_model(model, imputer, X, y)
    elapsed = time.time() - start
    st.write(f"✔️ Modelo entrenado en {elapsed:.2f}s")
    status.update(label="Listo ✅", state="complete")

st.subheader("📊 Métricas del modelo")
st.write({k: v for k, v in metrics.items() if k != "report"})

col1, col2 = st.columns(2)
with col1:
    if st.button("📄 Generar reporte PDF"):
        path = generar_reporte_pdf(metrics, output_path="results/reports/reporte_modelo.pdf")
        with open(path, "rb") as f:
            st.download_button("Descargar reporte", f, file_name="reporte_modelo.pdf")

st.info("Asegúrate de colocar `dataset_balanceado_SMOTEENN.csv` en la raíz del proyecto.")
