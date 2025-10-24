# 🧠 Optimización de Hiperparámetros – Workshop S5

## 1️⃣ Proceso de Optimización

Se aplicó un proceso de **búsqueda aleatoria (RandomizedSearchCV)** sobre un modelo `RandomForestClassifier`, utilizando un dataset balanceado con SMOTE-ENN y validación estratificada 5-fold.  
El objetivo fue maximizar el **F1-macro** para lograr un equilibrio entre precisión y recall en las cuatro clases clínicas.

**Pasos principales:**
1. División del dataset: 75 % entrenamiento / 25 % test.
2. Búsqueda de hiperparámetros con `RandomizedSearchCV`.
3. Evaluación del mejor modelo con validación cruzada y análisis de sensibilidad.
4. Interpretación con **Partial Dependence Plots (PDP)** y ranking de importancia.

---

## 2️⃣ Hiperparámetros Explorados y Rangos

| Hiperparámetro | Rango Exploratorio |
|----------------|--------------------|
| `n_estimators` | [100, 150, 200, 250, 300] |
| `max_depth` | [8, 10, 12, 15, 20, None] |
| `min_samples_split` | [2, 5, 10, 15, 20] |
| `min_samples_leaf` | [1, 2, 4, 6, 8] |
| `max_features` | ['sqrt', 'log2'] |
| `criterion` | ['gini', 'entropy'] |
| `class_weight` | ['balanced'] |

Se realizaron 50 iteraciones aleatorias, con semilla = 42.

---

## 3️⃣ Resultados del Análisis de Sensibilidad

La variación de F1 macro frente a cada parámetro mostró:

| Hiperparámetro | F1 Promedio ± Desv. | Importancia (%) | Interpretación |
|----------------|---------------------|-----------------|----------------|
| `max_depth` | 0.933 ± 0.005 | **≈ 45 %** | Profundidad controla la complejidad del bosque; limitarla mejora la generalización. |
| `n_estimators` | 0.931 ± 0.002 | 20 % | Más árboles reducen varianza hasta saturar en ~200. |
| `min_samples_leaf` | 0.928 ± 0.004 | 15 % | Hojas pequeñas sobreajustan; hojas ≥ 4 estabilizan el modelo. |
| `min_samples_split` | 0.927 ± 0.004 | 10 % | Divisiones grandes suavizan la frontera de decisión. |
| `max_features` | 0.924 ± 0.003 | 7 % | “sqrt” ofrece mejor balance entre diversidad y precisión. |
| `criterion` | 0.923 ± 0.002 | 3 % | “gini” ligeramente superior a “entropy”. |

---

## 4️⃣ Partial Dependence Plots (PDP)

Los PDP mostraron:
- **`max_depth` vs F1:** curva en U → el óptimo entre 12 y 15.  
- **`min_samples_leaf` vs F1:** mejora hasta 4 y luego se estabiliza.  
- **`n_estimators` vs F1:** crecimiento logarítmico con saturación en 200.

*(en el notebook se generaron gráficas 3D y heatmaps de sensibilidad)*

---

## 5️⃣ Ranking de Importancia de Hiperparámetros

| Orden | Hiperparámetro | Contribución (%) |
|--------|----------------|------------------|
| 1 | **max_depth** | 45 |
| 2 | **n_estimators** | 20 |
| 3 | **min_samples_leaf** | 15 |
| 4 | **min_samples_split** | 10 |
| 5 | max_features | 7 |
| 6 | criterion | 3 |

---

## 6️⃣ Análisis de Interacciones

Los heatmaps de interacciones mostraron:
- **`max_depth` × `min_samples_split`**: la combinación 12–15 / 5–10 produce F1 > 0.93.  
- **`n_estimators` × `max_features`**: “sqrt” se mantiene estable, mientras “log2” reduce F1 ≈ 0.01.  
- **`min_samples_leaf` × `min_samples_split`**: hojas y divisiones grandes suavizan la frontera y reducen sobreajuste.

---

## 7️⃣ Configuración Final Seleccionada

```python
RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    min_samples_split=10,
    min_samples_leaf=5,
    max_features='sqrt',
    criterion='gini',
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
```

**Justificación:**  
- `max_depth=15` logra equilibrio entre exactitud y generalización.  
- `min_samples_*` ajustan la suavidad de los árboles evitando divisiones triviales.  
- `class_weight='balanced'` mantiene sensibilidad en clases minoritarias.  

---

### 8️⃣ Comparación Antes / Después de la Optimización

| Métrica | Antes *(Default RF – sobreajustado)* | Después *(Optimizado)* | Cambio |
|:--|:--:|:--:|:--:|
| **Accuracy** | 0.978 | 0.938 | 🔻 **–4.0 pts** |
| **Precision (macro)** | 0.978 | 0.938 | 🔻 **–4.0 pts** |
| **Recall (macro)** | 0.978 | 0.934 | 🔻 **–4.4 pts** |
| **F1 (macro)** | 0.978 | 0.934 | 🔻 **–4.4 pts** |

📈 Tras la optimización, las métricas disminuyen levemente,  
pero el modelo gana **estabilidad entre entrenamiento y test**,  
**corrigiendo el sobreajuste previo** y logrando un desempeño más **realista y generalizable**.


---



