# 🧠 CliniCareAI - Aquitectura

## Tipo de Modelo Seleccionado

El modelo principal utilizado en **CliniCareAI** es un **Random Forest Classifier** multiclase.  
Este modelo fue elegido tras evaluar su desempeño frente a alternativas como XGBoost y SVM, debido a su equilibrio entre **precisión**, **interpretabilidad** y **robustez clínica**.

---

**Justificación técnica:**
- Es un modelo de clasificación muticlase que maneja datos clínicos tabulares heterogéneos sin requerir normalización extrema.   
- Tiene baja varianza y resistencia al sobreajuste, ideal para datos médicos generados mediante *data augmentation* con SMOTE-ENN.  
- Presenta rendimiento estable con F1-macro ≈ **0.934**, Precision ≈ **0.938*  y Recall ≈ **0.934**.  

---

**Configuración óptima del modelo:**  
```python
RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features='sqrt',
    criterion='gini',
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)


## 🧩 Arquitectura Detallada del Sistema

El sistema **CliniCareAI** está compuesto por siete módulos principales que conforman una arquitectura modular, trazable y escalable.

| Módulo | Descripción | Tecnologías |
|--------|-------------|-------------|
| **1. Ingesta de datos** | Carga del dataset médico-realista con variables como glucosa, HbA1c(hemoglobina), presión sistólica y diastólica. | `pandas`, `numpy` |
| **2. Preprocesamiento** | Imputación sintética médico-realista y generación de visitas clínicas simuladas (series de tiempo). | `numpy`, `pandas` |
| **3. Limpieza y normalización** | Escalado de variables y codificación one-hot. | `scikit-learn` |
| **4. Balanceo de clases** | Aplicación de SMOTE-ENN para representar adecuadamente las clases de diabetes, hipertensión y comorbilidad. | `imbalanced-learn` |
| **5. Entrenamiento y validación** | Entrenamiento del modelo Random Forest con validación cruzada (`cv=3`) y registro de métricas. | `scikit-learn` |
| **6. Interpretabilidad** | Análisis de importancia de variables y explicabilidad local/global mediante SHAPE. | `shape` |
| **7. Interfaz médica (Frontend)** | Panel interactivo construido en Streamlit que muestra métricas, predicciones y alertas tempranas. | `streamlit` |

---


## 🧱 Arquitectura Lógica

### 🎛️ Frontend – Interfaz Médica (Streamlit)

-
- Panel de diagnóstico visual con métricas **F1**, **Recall** y predicciones individuales.
- Gráficos interactivos con **SHAPE** para interpretación médica personalizada.
- Sistema de **alerta temprana** por tipo de patología (diabetes, hipertensión o comorbilidad).

---

### 🧠 Backend – Motor de Inteligencia Artificial

- Entrenamiento, predicción y **actualización periódica del modelo**.
- **Serialización** de versiones de modelo (`v1.0`, `v1.1`, ...).
- **Logging de decisiones clínicas** con histórico de predicciones y resultados.

### 🔐 Módulo de Seguridad y Compliance

- Hash de identificadores (`patient_id`) para anonimización.
- **Cifrado TLS** y cumplimiento con la **LOPDP**  
  *(Ley Orgánica de Protección de Datos Personales – Ecuador)*.
- Registro de **auditorías automáticas** para trazabilidad legal y clínica.

---

## 🔄 Diagrama de Flujo del Sistema
       ┌─────────────────────────────┐
       │     Datos Clínicos Base     │
       │ (glucosa, HbA1c, presión)   │
       └──────────────┬──────────────┘
                      │
                      ▼
    ┌─────────────────────────────┐
    │  Imputación Médico-Realista │
    │   (variación controlada)    │
    └──────────────┬──────────────┘
                      │
                      ▼
    ┌─────────────────────────────┐
    │ Balanceo de Clases (SMOTE-ENN)  │
    │     y Normalización         │
    └──────────────┬──────────────┘
                      │
                      ▼
    ┌─────────────────────────────┐
    │ Entrenamiento del Modelo    │
    │       (Random Forest)       │
    └──────────────┬──────────────┘
                      │
                      ▼
    ┌─────────────────────────────┐
    │ Optimización de Parámetros  │
    │   (RandomizedSearchCV)      │
    └──────────────┬──────────────┘
                      │
                      ▼
    ┌─────────────────────────────┐
    │ Interpretabilidad (SHAPE)│
    └──────────────┬──────────────┘
                      │
                      ▼
    ┌─────────────────────────────┐
    │ Interfaz Médica (Streamlit) │
    │   Visualización y Alertas   │
    └─────────────────────────────┘

---
## 🧮 Pipeline de Datos

El pipeline automatiza todas las etapas del procesamiento y asegura coherencia clínica desde el ingreso hasta la predicción final.

| Etapa | Descripción | Función Principal |
|-------|-------------|-------------------|
| **1. Input clínico** | Lectura del dataset (CSV/Parquet) con 900,000 registros balanceados. | `pandas.read_csv()` |
| **2. Imputación** | Relleno sintético con reglas clínicas (diabetes → glucosa ↑; hipertensión → presión ↑). | Imputación condicional controlada |
| **3. Feature Engineering** | Creación de variables derivadas (`glucose_hba1c_ratio`, `pulse_pressure`). | `numpy`, `pandas` |
| **4. Escalado y codificación** | Normalización (Z-score) y codificación one-hot. | `StandardScaler`, `OneHotEncoder` |
| **5. Balanceo de clases** | Aplicación de SMOTE-ENN. | `imbalanced-learn` |
| **6. Entrenamiento y validación** | Modelo con validación cruzada (`cv=3`). | `scikit-learn` |
| **7. Exportación del modelo** | Serialización del modelo final (.pkl) para la interfaz. | `joblib` |
| **8. Output** | Predicción multiclase (-1, 0, 1, 2) y visualización. | `Streamlit UI` |

---

## ⚙️ Tecnologías y Librerías Utilizadas

| Categoría | Herramienta | Versión | Descripción |
|----------|-------------|---------|-------------|
| **Lenguaje base** | Python | 3.8 | Entorno principal del sistema |
| **Modelado IA** | `scikit-learn` | 1.3.0 | Entrenamiento, CV y optimización |
| **Balanceo de clases** | `imbalanced-learn` | 0.11.0 | Técnicas de balanceo (SMOTE-ENN) |
| **Visualización** | `matplotlib`, `seaborn` | 3.8.0, 0.12.2 | Gráficos de métricas y tendencias |
| **Preprocesamiento** | `pandas`, `numpy` | 2.1.0, 1.25.0 | Limpieza, imputación y transformación |
| **Explicabilidad** | `SHAPE` | 0.44.0, 0.2.0 | Interpretación global y local |
| **Despliegue web** | `Streamlit` | 1.32.0 | Interfaz clínica y dashboards |
| **Seguridad de datos** | `hashlib`, `ssl` | Integrado | Cifrado y anonimización |
| **Control de versiones** | Git / GitHub | — | Versionado del código y documentación |

---

