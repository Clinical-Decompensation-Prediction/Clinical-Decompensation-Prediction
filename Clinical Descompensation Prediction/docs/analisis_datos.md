# 📊 Análisis de Datos (EDA) — Sistema de Predicción de Descompensaciones Clínicas

---

## 1️⃣ Descripción Detallada del Dataset

El dataset utilizado corresponde a un conjunto **balanceado mediante la técnica SMOTE-ENN**, empleado para predecir descompensaciones clínicas en pacientes con enfermedades crónicas.  
Contiene **994,916 registros** y **24 variables** fisiológicas, derivadas y temporales, todas anonimizadas y procesadas exclusivamente con fines académicos.

### 🔍 Características generales

- **Tipo de problema:** Clasificación multiclase supervisada  
- **Variable objetivo:** `target`  
- **Clases:**
  - `-1`: Sin enfermedad  
  - `0`: Diabetes tipo 2  
  - `1`: Hipertensión  
  - `2`: Comorbilidad (Diabetes + Hipertensión)  
- **Número de variables:** 24  
- **Número de observaciones:** 994,916  
- **Formato:** CSV  
- **Fuente:** Dataset sintético basado en monitoreo fisiológico de pacientes crónicos.

### 🧩 Variables principales

| Tipo | Variables | Descripción |
|------|------------|-------------|
| **Clínicas Base** | `age`, `bmi`, `blood_glucose_level`, `HbA1c_level`, `systolic_bp`, `diastolic_bp` | Mediciones fisiológicas fundamentales. |
| **Derivadas** | `glucose_hba1c_ratio`, `bmi_age_interaction`, `pulse_pressure` | Combinaciones de indicadores metabólicos y de presión arterial. |
| **Transformadas** | `glucose_log`, `bmi_sqrt`, `hba1c_squared` | Transformaciones logarítmicas, cuadradas y raíz cuadrada para estabilizar varianza. |
| **Temporales (series)** | `glucose_lag1`, `glucose_diff`, `glucose_roll3`, `hba1c_lag1`, `hba1c_diff`, `hba1c_last`, `glucose_patient_mean` | Capturan variaciones históricas en visitas médicas. |
| **Categóricas** | `diabetes`, `hypertension`, `target` | Indicadores binarios y variable de salida. |

💡 La estructura del dataset permite modelar tanto las condiciones actuales como la evolución temporal de cada paciente, fortaleciendo la capacidad predictiva del sistema.

---

## 2️⃣ Estadísticas Descriptivas

A continuación se presentan estadísticas resumidas de las principales variables fisiológicas y metabólicas del conjunto balanceado:

| Variable | Media | Mediana | Desv. Est. | Mínimo | Máximo |
|-----------|--------|----------|-------------|---------|---------|
| `age` | 52.4 | 51 | 12.8 | 18 | 90 |
| `blood_glucose_level` | 138.6 | 135 | 41.3 | 70 | 300 |
| `HbA1c_level` | 6.8 | 6.5 | 1.4 | 4.0 | 12.3 |
| `bmi` | 28.7 | 27.9 | 4.8 | 17.0 | 43.2 |
| `systolic_bp` | 132.5 | 130 | 15.6 | 90 | 200 |
| `diastolic_bp` | 82.1 | 81 | 9.7 | 55 | 110 |

📈 **Interpretación:**  
Las distribuciones presentan valores coherentes con poblaciones adultas con enfermedades metabólicas y cardiovasculares.  
La desviación estándar es moderada, lo que indica variabilidad controlada y ausencia de sesgo extremo.

---

## 3️⃣ Visualizaciones del EDA (Exploratory Data Analysis)

Durante el análisis exploratorio se generaron las siguientes **6 visualizaciones clave**, que permiten comprender la estructura y distribución del dataset:

| Nº | Gráfico | Objetivo |
|----|----------|----------|
| 1️⃣ | Histograma de `age` | Examinar la distribución etaria de la muestra. |
| 2️⃣ | Boxplot de `blood_glucose_level` por `target` | Observar diferencias de glucosa entre clases. |
| 3️⃣ | Heatmap de correlaciones numéricas | Evaluar relaciones entre variables fisiológicas. |
| 4️⃣ | Dispersión `bmi` vs `blood_glucose_level` coloreada por `target` | Analizar patrones metabólicos entre grupos clínicos. |
| 5️⃣ | KDE de `pulse_pressure` | Comparar distribución de presión arterial entre clases. |
| 6️⃣ | Countplot de `target` | Visualizar el equilibrio de clases obtenido tras SMOTE-ENN. |

📁 Los gráficos fueron exportados a la carpeta:  
`results/figures/`  
y documentados en el notebook `01_exploracion.ipynb`.

---

## 4️⃣ Identificación de Patrones, Correlaciones y Outliers

### 🔹 Patrones principales
- Incrementos de `blood_glucose_level` y `HbA1c_level` caracterizan a pacientes con **diabetes tipo 2**.
- Valores elevados de `pulse_pressure` (sistólica – diastólica) son frecuentes en pacientes con **hipertensión**.
- Pacientes con `target = 2` (comorbilidad) presentan simultáneamente altos valores en ambas variables.

### 🔹 Correlaciones
- `blood_glucose_level` ↔ `HbA1c_level` → **r ≈ 0.84 (alta correlación positiva)**  
- `systolic_bp` ↔ `diastolic_bp` → **r ≈ 0.65 (moderada positiva)**  
- `age` ↔ `bmi_age_interaction` → **r ≈ -0.23 (negativa leve)**  
- Variables derivadas como `pulse_pressure` y `glucose_hba1c_ratio` introducen información no redundante.

### 🔹 Outliers
- **Glucosa > 250 mg/dL** → casos de diabetes severa.  
- **BMI > 40** → obesidad tipo III.  
Ambos valores fueron **conservados**, ya que representan condiciones clínicas reales y útiles para el modelo.

---

## 5️⃣ Decisiones de Preprocesamiento Justificadas

| Proceso | Descripción | Justificación |
|----------|-------------|----------------|
| **Imputación de valores faltantes** | Se reemplazaron valores nulos por la mediana. | Evita sesgos y mantiene la distribución original. |
| **Ingeniería de variables** | Se generaron variables derivadas, transformadas y temporales. | Aumenta la explicabilidad y el poder predictivo del modelo. |
| **Eliminación de columnas irrelevantes** | Variables con varianza nula o redundancia fueron descartadas. | Reduce ruido y simplifica el modelo. |
| **Balanceo de clases (SMOTE-ENN)** | Aplicación combinada de sobremuestreo y limpieza de ruido. | Garantiza representatividad equitativa entre clases. |
| **No escalado global** | Mantiene las unidades originales. | Random Forest no requiere estandarización completa. |

📘 El preprocesamiento fue cuidadosamente diseñado para conservar la integridad clínica de los datos y mejorar la robustez del modelo de predicción.

---

## 6️⃣ Manejo de Datos Faltantes y Desbalanceados

- **Datos faltantes:**  
  - Menos del 3 % en variables como `HbA1c_level`, `bmi`, `systolic_bp`.  
  - Tratados con **imputación por mediana** (estrategia robusta ante outliers).  

- **Desbalance original (pre-SMOTE-ENN):**  
  - La clase `-1` (sin enfermedad) representaba ≈86 %.  
  - Las clases clínicas (`0`, `1`, `2`) sumaban solo 14 %.  

- **Tras SMOTE-ENN (balance final):**

| Clase (`target`) | Descripción | Casos | Proporción (%) |
|------------------|-------------|--------|----------------|
| -1 | Sin enfermedad | 225,125 | 22.63 % |
| 0 | Diabetes tipo 2 | 256,539 | 25.78 % |
| 1 | Hipertensión | 255,444 | 25.67 % |
| 2 | Comorbilidad (ambas) | 257,808 | 25.91 % |

📈 El balanceo produjo una representación equitativa (~25 % por clase), reduciendo el sesgo y mejorando la sensibilidad del modelo para las enfermedades menos frecuentes.

---

## 🧠 Conclusiones del EDA

1. El dataset balanceado es **completo, coherente y clínicamente válido**.  
2. Las variables derivadas y temporales aportan **nueva información útil** para la predicción.  
3. No se detectan errores ni inconsistencias estructurales en los datos.  
4. Los outliers son **casos clínicos reales**, no errores de captura.  
5. La aplicación de **SMOTE-ENN** eliminó el desbalance extremo inicial, asegurando un conjunto de datos equilibrado.  
6. El dataset final se considera **listo para el modelado supervisado**, con alta calidad estructural y equilibrio estadístico.

---

📍 **Archivos relacionados:**
- `notebooks/01_exploracion.ipynb` — Exploración y estadísticas descriptivas.  
- `notebooks/02_preprocesamiento.ipynb` — Limpieza e ingeniería de características.  
- `data/processed/dataset_balanceado_SMOTEENN.csv` — Dataset final utilizado para entrenamiento.  

 

