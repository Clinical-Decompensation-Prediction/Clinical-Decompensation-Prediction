
# Clinical Decompensation Prediction

## 📑 Tabla de Contenidos
- [Objetivo del proyecto](#-objetivo-del-proyecto)
- [Estructura del repositorio](#-estructura-del-repositorio)
- [Datasets](#-datasets)
- [Pseudocódigo inicial](#-pseudocódigo-inicial)
- [Licencias y permisos](#-licencias-y-permisos)
- [Métricas a cumplir](#-métricas-a-cumplir)
- [Autor](#-autor)

---

## 📌 Objetivo del proyecto
Diseñar, implementar y evaluar un sistema inteligente basado en modelos de aprendizaje automático supervisado y análisis de series de tiempo, capaz de predecir **descompensaciones clínicas** en pacientes con enfermedades crónicas (diabetes tipo 2 e hipertensión), utilizando datos de monitoreo con el fin de generar **alertas preventivas y recomendaciones personalizadas**.

---

## 📂 Estructura del repositorio
```Clinical-Decompensation-Prediction/
├── README.md
├── Samples/
│ ├── Blood Pressure Data for disease Prediction/
│ │ ├── diabetes_012_health_indicators_BRFSS2015.csv
│ │ ├── diabetes_binary_5050split_health_indicators_BRFSS2015.csv
│ │ └── diabetes_binary_health_indicators_BRFSS2015.csv
│ ├── Diabetes 130-US Hospitals for Years 1999-2008/
│ │ ├── IDS_mapping.csv
│ │ └── diabetic_data.csv
│ └── Diabetes Health Indicators Dataset/
│ └── data.csv
```


---

## 📊 Datasets

1. **Diabetes 130-US Hospitals (UCI)**  
   - 🔗 [Dataset completo](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)  
   - Incluye `diabetic_data.csv` y `IDS_mapping.csv`.  

2. **Blood Pressure Dataset (Kaggle)**  
   - 🔗 [Dataset completo](https://www.kaggle.com/datasets/pavanbodanki/blood-press)  
   - Ejemplos en `Samples/Blood Pressure Data for disease Prediction/`.  

3. **Diabetes Health Indicators (BRFSS 2015, CDC/Kaggle)**  
   - 🔗 [Dataset completo](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)  
   - Ejemplo en `Samples/Diabetes Health Indicators Dataset/data.csv`.  

⚠️ Los datasets completos son demasiado grandes para GitHub. En este repositorio se incluyen **subconjuntos de muestra** para pruebas rápidas, junto con los enlaces oficiales a los datasets completos.

---

## ⚙️ Pseudocódigo inicial

```python
# 1. Cargar datasets
diabetes, presion, brfss = cargar_datasets()

# 2. Preprocesar
datos = preprocesar(diabetes, presion, brfss)

# 3. Modelos supervisados
baseline_LR = LogisticRegression().fit(datos.train)
modelo_RF   = RandomForest().fit(datos.train)
modelo_GB   = GradientBoosting().fit(datos.train)

# 4. Evaluar modelos
for modelo in [baseline_LR, modelo_RF, modelo_GB]:
    pred = modelo.predict(datos.test)
    calcular_metricas(pred, datos.test)

# 5. Guardar métricas y gráficas
guardar_metricas()
guardar_graficas()
