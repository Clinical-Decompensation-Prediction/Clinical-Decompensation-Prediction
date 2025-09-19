
# Clinical Decompensation Prediction

📌 **Objetivo del proyecto**  
Diseñar, implementar y evaluar un sistema inteligente basado en modelos de aprendizaje automático supervisado y análisis de series de tiempo, capaz de predecir **descompensaciones clínicas** en pacientes con enfermedades crónicas (diabetes tipo 2 e hipertensión), utilizando datos de monitoreo con el fin de generar **alertas preventivas y recomendaciones personalizadas**.

---

## 📂 Estructura del repositorio
Clinical-Decompensation-Prediction/
│
├── README.md # Documentación del proyecto
├── Samples/ # Subconjuntos de datasets para pruebas
│ ├── diabetes_sample.csv
│ ├── blood_pressure_sample.csv
│ └── brfss_sample.csv
├── data/ # (opcional) datasets completos - no subir grandes
│ ├── raw/ # datasets originales
│ ├── processed/ # datasets preprocesados
│ └── samples/ # muestras pequeñas
├── notebooks/ # Notebooks Jupyter
├── src/ # Código fuente en Python
│ ├── preprocesamiento.py
│ ├── modelos.py
│ └── series.py
├── results/ # Métricas y resultados del modelo
│ ├── metricas/
│ ├── figuras/
│ └── reportes/
└── docs/ # Documentación y diagramas

## 📊 Datasets

1. **Diabetes 130-US Hospitals (UCI)**  
   - 🔗 [Dataset completo](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)  
   - 📂 Ejemplo reducido en `Samples/diabetes_sample.csv`  

2. **Blood Pressure Dataset (Kaggle)**  
   - 🔗 [Dataset completo](https://www.kaggle.com/datasets/pavanbodanki/blood-press)  
   - 📂 Ejemplo reducido en `Samples/blood_pressure_sample.csv`  

3. **Diabetes Health Indicators (BRFSS 2015, CDC/Kaggle)**  
   - 🔗 [Dataset completo](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)  
   - 📂 Ejemplo reducido en `Samples/brfss_sample.csv`  

---

## ⚙️ Pseudocódigo inicial

```python
# Pseudocódigo del pipeline

# 1. Cargar datos
diabetes, presion, brfss = cargar_datasets()

# 2. Preprocesar datos
datos = preprocesar(diabetes, presion, brfss)

# 3. Entrenar modelos
baseline_LR = LogisticRegression().fit(datos.train)
modelo_RF   = RandomForest().fit(datos.train)
modelo_GB   = GradientBoosting().fit(datos.train)

# 4. Evaluar
for modelo in [baseline_LR, modelo_RF, modelo_GB]:
    evaluar(modelo, datos.test)
    calcular_métricas(modelo, ["AUROC", "F1", "Recall", "Precision"])

# 5. Guardar resultados
guardar_metricas()
guardar_graficas()
