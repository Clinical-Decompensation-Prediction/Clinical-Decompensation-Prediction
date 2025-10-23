# 📊 Descripción  de los datos

---
El conjunto de datos incluye **Aprox. 1 millón de registros** y **24 variables** fisiológicas, derivadas y temporales.  
Se emplea para un problema de **clasificación multiclase supervisada**, donde la variable objetivo es `target`.

### 🔍 Información general

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
| **Transformadas** | `glucose_log`, `bmi_sqrt`, `hba1c_squared` | Transformaciones para estabilizar la varianza. |
| **Temporales (series)** | `glucose_lag1`, `glucose_diff`, `glucose_roll3`, `hba1c_lag1`, `hba1c_diff`, `hba1c_last`, `glucose_patient_mean` | Capturan variaciones históricas entre visitas médicas. |
| **Categóricas** | `diabetes`, `hypertension`, `target` | Indicadores binarios y variable de salida. |

💡 **Nota:** La estructura permite modelar tanto el estado actual como la evolución temporal de cada paciente, fortaleciendo la capacidad predictiva del sistema.

---

## 2️⃣ Estadísticas Descriptivas

| Variable | Media | Mediana | Desv. Est. | Mínimo | Máximo |
|-----------|--------|----------|-------------|---------|---------|
| `age` | 52.4 | 51 | 12.8 | 18 | 90 |
| `blood_glucose_level` | 138.6 | 135 | 41.3 | 70 | 300 |
| `HbA1c_level` | 6.8 | 6.5 | 1.4 | 4.0 | 12.3 |
| `bmi` | 28.7 | 27.9 | 4.8 | 17.0 | 43.2 |
| `systolic_bp` | 132.5 | 130 | 15.6 | 90 | 200 |
| `diastolic_bp` | 82.1 | 81 | 9.7 | 55 | 110 |

📈 **Interpretación:**  
Las distribuciones son coherentes con poblaciones adultas con enfermedades metabólicas y cardiovasculares. La variabilidad es controlada y no se observan sesgos extremos.

---

## 3️⃣ Visualizaciones del EDA

Durante la exploración se generaron **6 visualizaciones clave** para comprender la estructura del dataset:

| Nº | Gráfico | Objetivo |
|----|----------|----------|
| 1️⃣ | Histograma de `age` | Distribución etaria de la muestra. |
| 2️⃣ | Boxplot de `blood_glucose_level` por `target` | Diferencias de glucosa entre clases. |
| 3️⃣ | Heatmap de correlaciones numéricas | Evaluar relaciones fisiológicas. |
| 4️⃣ | Dispersión `bmi` vs `blood_glucose_level` coloreada por `target` | Patrones metabólicos entre grupos clínicos. |
| 5️⃣ | KDE de `pulse_pressure` | Comparar distribución de presión arterial. |
| 6️⃣ | Countplot de `target` | Visualizar equilibrio de clases tras SMOTE-ENN. |

📁 **Ubicación de resultados:**  
`results/figures/`  
📓 **Notebook asociado:** `notebooks/01_exploracion.ipynb`

---

## 4️⃣ Patrones, Correlaciones y Outliers

### 🔹 Patrones detectados
- `blood_glucose_level` y `HbA1c_level` altos → **Diabetes tipo 2**  
- `pulse_pressure` elevado → **Hipertensión**  
- Altos valores combinados → **Comorbilidad (Diabetes + Hipertensión)**

### 🔹 Correlaciones destacadas
| Relación | Coef. (r) | Tipo |
|-----------|------------|------|
| `blood_glucose_level` ↔ `HbA1c_level` | 0.84 | Alta positiva |
| `systolic_bp` ↔ `diastolic_bp` | 0.65 | Moderada positiva |
| `age` ↔ `bmi_age_interaction` | -0.23 | Leve negativa |

### 🔹 Outliers
- `blood_glucose_level > 250 mg/dL` → Casos de diabetes severa  
- `bmi > 40` → Obesidad tipo III  
➡️ **Se conservaron**, ya que reflejan condiciones clínicas reales.

---

## 5️⃣ Decisiones de Preprocesamiento

| Proceso | Descripción | Justificación |
|----------|-------------|----------------|
| **Imputación de valores faltantes** | Reemplazo por la mediana. | Evita sesgos y mantiene la distribución. |
| **Ingeniería de variables** | Creación de derivadas, transformadas y temporales. | Mejora la explicabilidad y precisión. |
| **Eliminación de columnas irrelevantes** | Variables con varianza nula o redundantes. | Reduce ruido y complejidad. |
| **Balanceo de clases (SMOTE-ENN)** | Sobremuestreo + limpieza de ruido. | Asegura representatividad equitativa. |
| **Sin escalado global** | Conserva unidades originales. | Random Forest no requiere estandarización completa. |

---

## 6️⃣ Manejo de Datos Faltantes y Desbalanceados

- **Datos faltantes (<3 %)** → imputación por mediana.  
- **Desbalance original:**  
  - Clase `-1` ≈ 86 %  
  - Clases `0`, `1`, `2` ≈ 14 %

### ⚖️ Distribución final tras SMOTE-ENN:

| Clase | Descripción | Casos | Proporción (%) |
|--------|--------------|--------|----------------|
| -1 | Sin enfermedad | 225,125 | 22.63 % |
| 0 | Diabetes tipo 2 | 256,539 | 25.78 % |
| 1 | Hipertensión | 255,444 | 25.67 % |
| 2 | Comorbilidad | 257,808 | 25.91 % |

📈 **Resultado:** Conjunto balanceado (~25 % por clase), mejora la sensibilidad del modelo ante clases minoritarias.

---

## 🧠 Nota

1. Dataset **completo, coherente y clínicamente válido**.  
2. Las variables derivadas y temporales aportan **valor predictivo adicional**.  
3. No se detectaron errores estructurales ni sesgos extremos.  
4. Los outliers representan **casos clínicos reales**, no errores.  
5. El uso de **SMOTE-ENN** corrigió el desbalance original.  
6. El dataset está **listo para modelado supervisado** con alta calidad y equilibrio.


