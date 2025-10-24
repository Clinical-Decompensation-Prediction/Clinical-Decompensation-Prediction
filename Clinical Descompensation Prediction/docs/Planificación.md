# 🧠 CliniCareAI - Planificación del proyecto

**Sistema Inteligente para la Predicción de Descompensaciones Clínicas en pacientes con Diabetes Tipo 2, Hipertensión o Comorbilidad**

## 📌 Definición del Problema y Objetivos  

Las enfermedades crónicas como la **diabetes tipo 2** y la **hipertensión arterial** representan una de las principales causas de hospitalización y mortalidad en Ecuador y Latinoamérica. La falta de monitoreo continuo y detección temprana de descompensaciones clínicas retrasa la intervención médica y aumenta los costos sanitarios.

---

**CliniCare AI** busca anticipar estas descompensaciones mediante un modelo de *Machine Learning supervisado* y análisis de *series de tiempo fisiológicas*, utilizando variables como:
- Glucosa en sangre  
- Hemoglobina 
- Presión arterial sistólica y diastólica  
- Índice de masa corporal (IMC)  
- Historial clínico y visitas médicas simuladas mediante imputación de datos generados por reglas médico-realistas, basadas en el comportamiento clínico esperado en pacientes con enfermedades crónicas.

---

### 🎯 Objetivo General  
Diseñar e implementar un sistema inteligente que **prediga descompensaciones clínicas** en pacientes con enfermedades crónicas o comorbilidad, integrando IA, análisis de datos médicos y visualización interactiva.

---

### 🎯 Objetivos Específicos  
1. Construir un dataset médico-realista con imputación controlada y series temporales simuladas.  
2. Entrenar y optimizar un modelo de clasificación (Random Forest) capaz de identificar riesgo individual de descompensación.  
3. Implementar un *pipeline* automatizado de preprocesamiento y balanceo de datos.  
4. Evaluar el modelo con métricas F1, Precision y Recall, asegurando generalización clínica.  
5. Desarrollar una interfaz en **Streamlit** para visualización de predicciones y métricas.

---

## 💡 Justificación de la relevancia del Proyecto  

El sistema aborda un **problema de salud pública** de alta prevalencia y permite:
- **Predicción temprana de eventos críticos** (hiperglucemia, crisis hipertensiva entre otras).  
- **Apoyo a la decisión clínica**, reduciendo tiempos de diagnóstico.  
- **Integración futura en plataformas de monitoreo hospitalario** en Ecuador.  

Además, el enfoque ético y técnico del proyecto se alinea con los principios de **IA responsable de la IEEE** y la **Ley Orgánica de Protección de Datos Personales (LOPDP 2021)**, garantizando transparencia y privacidad en los datos clínicos.

---

## 🚀 Alcance del Proyecto  

**Incluye:**
- Desarrollo del modelo predictivo basado en Random Forest.  
- Implementación del pipeline completo de datos (limpieza, imputación, balanceo SMOTE, feature engineering).  
- Análisis de sensibilidad e hiperparámetros.  
- Interfaz visual con **Streamlit** para uso médico simulado.  

---

**No incluye (en esta fase):**
- Conexión en tiempo real con sistemas hospitalarios.  
- Validación con datos clínicos reales de pacientes.  
- Integración con dispositivos médicos IoT (fase futura).

---

## 🕒 Cronograma de Desarrollo  

| Fase | Actividad | Planificado | Real |
|------|-----------|-------------|------|
| 1 | Diseño del dataset sintético y simulación médica | Semana 1–2 | Semana 1–3 |
| 2 | Entrenamiento del modelo base (Random Forest) | Semana 3–4 | Semana 4 |
| 3 | Optimización de hiperparámetros | Semana 5 | Semana 5 |
| 4 | Implementación del pipeline y Streamlit | Semana 6–7 | Semana 6 |
| 5 | Evaluación y documentación final | Semana 8 | Semana 6 |

---

## ⚙️ Recursos Necesarios  

| Recurso | Descripción |
|----------|--------------|
| **Datos** | Dataset médico-realista con 900 000 registros (balanceado). |
| **Hardware** | CPU de 8 núcleos, 16 GB RAM (Google Colab / Workstation local). |
| **Software** | Python ≥ 3.8, scikit-learn, pandas, matplotlib, seaborn, Streamlit. |
| **Librerías adicionales** | imbalanced-learn, numpy, shap, lime, joblib. |
| **Entorno de despliegue** | Streamlit + GitHub + Colab. |

---

## ⚠️ Riesgos Identificados y Estrategias de Mitigación  

El desarrollo de CliniCareAI implicó la identificación y gestión de riesgos éticos, técnicos y clínicos asociados al uso de inteligencia artificial en salud.  
A continuación, se detallan los principales riesgos detectados y las estrategias aplicadas para su mitigación:

| Riesgo | Descripción | Estrategia de Mitigación | Tipo | Implementación | Responsable | Efectividad |
|--------|--------------|--------------------------|------|----------------|--------------|--------------|
| **Sesgo algorítmico y Fairness** | Riesgo de subrepresentar mujeres o adultos mayores, generando desigualdad en las predicciones clínicas. | Reentrenar el modelo con más datos (series de tiempo) y aplicar métricas de *equal opportunity* por género y edad. | Técnica | 1️⃣ Evaluar sesgos con **Fairlearn**.<br>2️⃣ Ajustar pesos de clase y umbrales de decisión.<br>3️⃣ Monitorear métricas de equidad periódicamente. | Desarrolladores y equipo de ciencia de datos | Alta |
| **Privacidad y reidentificación** | Exposición de información médica sensible o correlaciones indirectas que permitan identificar pacientes. | Anonimizar identificadores y cifrar datos conforme a la **Ley Orgánica de Protección de Datos Personales (LOPDP)**. | Técnica / Política | 1️⃣ Hash de `patient_id`.<br>2️⃣ Cifrado TLS.<br>3️⃣ Auditorías periódicas de seguridad. | Desarrolladores y equipo de ciencia de datos | Alta |
| **Transparencia y explicabilidad** | Riesgo de falta de comprensión de los resultados por parte de médicos o pacientes. | Incorporar reportes interpretables con **SHAP** y documentación técnica visible para usuarios médicos. | Técnica / Diseño | 1️⃣ Visualizar impacto de variables.<br>2️⃣ Documentar confianza y límites del modelo. | Desarrolladores y equipo de ciencia de datos | Media-Alta |
| **Supervisión médica y autonomía** | Riesgo de dependencia excesiva en predicciones automáticas sin validación clínica. | Mantener revisión médica obligatoria y capacitar al personal en uso responsable de IA. | Educación / Política | 1️⃣ Validación doble (IA + médico).<br>2️⃣ Talleres de capacitación clínica. | Comité clínico y científicos de datos | Media |
| **Seguridad y accountability** | Fallos de predicción podrían inducir decisiones clínicas inadecuadas. | Establecer trazabilidad de decisiones y protocolo ante errores. | Política / Técnica | 1️⃣ Registro de logs automáticos.<br>2️⃣ Revisión médica de casos fallidos.<br>3️⃣ Auditorías clínicas. | Desarrolladores y comité clínico | Alta |

Estas medidas combinan acciones **técnicas, médicas y éticas** para garantizar la **equidad, privacidad, transparencia y seguridad** del sistema, en concordancia con las directrices de la **IEEE Global Initiative on Ethics of Autonomous and Intelligent Systems (IEEE 7000-2021)** y la **LOPDP de Ecuador**.

---

📘 **Referencia interna:** Documento técnico *CliniCareAI — Impacto Social y Responsabilidad en Proyecto de IA (2025)*.  


---

📘 **Autores:**  
- María Fernanda Bolaños Escandón.  
- Fernando Xavier Montaño Cárdenas.  

🗓️ **Última actualización:** Octubre 2025  
🏥 **Proyecto:** *CliniCAreAI — IA aplicada al monitoreo clínico inteligente.*

---
