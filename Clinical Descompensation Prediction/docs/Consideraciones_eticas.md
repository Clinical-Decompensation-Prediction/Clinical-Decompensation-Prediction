# 🧭 CliniCareAI — Consideraciones Éticas  

---

## 1. Análisis de Sesgos  

**¿El dataset tiene sesgos demográficos, culturales o de otro tipo?**  
Sí. Aunque se aplicó *data augmentation* y balanceo mediante **SMOTE-ENN**, el dataset presenta ligera **subrepresentación de mujeres** y **adultos mayores** en comparación con hombres de mediana edad. No existen sesgos culturales o raciales explícitos.

**¿Cómo podrían afectar estos sesgos las predicciones?**  
Pueden generar **menor precisión o recall** en grupos poco representados, afectando la equidad de alertas tempranas y aumentando el riesgo de falsos negativos en pacientes mayores o mujeres.  

**¿Qué grupos podrían ser perjudicados?**  
Adultos mayores y mujeres con diabetes o hipertensión, cuyos patrones fisiológicos podrían diferir del promedio del conjunto de entrenamiento.  


---

## 2. Equidad y Fairness  

**¿El modelo trata a todos los grupos de forma equitativa?**  
En general, sí. Los resultados muestran una variación inferior al ±2 % en métricas por género y edad, gracias al uso de ponderación balanceada y entrenamiento estratificado.  

**Métricas de fairness evaluadas:**  
- *Equal Opportunity Difference*  
- *Demographic Parity Difference*  
- Comparación de F1 y Recall por subgrupo  

**Estrategias implementadas para mitigar inequidades:**  
1. Reentrenamiento con datos balanceados.  
2. Uso de **`class_weight='balanced'`** en el modelo Random Forest.  
3. Inclusión progresiva de datos clínicos rurales y de adultos mayores.  

---

## 3. Privacidad  

**¿Se utilizan datos personales o sensibles?**  
Sí, se emplean variables clínicas sensibles como **glucosa**, **hemoglobina**, **presión arterial** e **IMC**, pero sin incluir nombres, direcciones ni identificadores directos que puedan dar con informaciòn sensible de los pacientes.  

**¿Cómo se protege la privacidad de los usuarios?**  
- Anonimización completa mediante **hash de patient_id**.    
- Control de acceso por roles para evitar manipulación de datos.  
- Eliminación periódica de registros temporales usados para entrenamiento.  

**Cumplimiento con regulaciones:**  
- **LOPDP (Ecuador, 2021):** Cumplimiento total.  
- **GDPR (UE):** Parcial, con incorporación futura del derecho al olvido.  
- **AI Act (UE, 2024):** En progreso (clasificación de sistema de alto riesgo, con revisión humana obligatoria).  


---

## 4. Transparencia y Explicabilidad  

**¿El modelo es interpretable?**  
Sí. Se priorizó la transparencia clínica mediante visualizaciones interactivas y técnicas de explicabilidad.  

**¿Los usuarios entienden cómo funciona?**  
Los médicos pueden revisar el impacto de cada variable en la predicción gracias a paneles visuales desarrollados en **Streamlit** y documentación explicativa integrada al igual que los pacientes.  

**Técnicas implementadas:**  
- **SHAPE (SHapley Additive Explanations):** Muestra la contribución individual de cada variable en la predicción.    
- **Feature Importance:** Ranking de variables relevantes (hemoglobina, glucosa, presión sistólica y diastólica).  

---

## 5. Impacto Social  

**¿Qué impacto positivo puede tener el proyecto?**  
- Mejora la **detección temprana de descompensaciones clínicas**, lo que puede salvar vidas.  
- Fortalece la **toma de decisiones médicas** basada en evidencia.  
- Optimiza la gestión hospitalaria mediante priorización de casos.  
- Facilita el **acceso remoto a monitoreo clínico** en zonas rurales.  

**¿Qué impactos negativos podrían surgir?**  
- Dependencia tecnológica del sistema sin supervisión médica.  
- Riesgo de sesgos si los datos no se actualizan periódicamente.  
- Posible pérdida de confianza si ocurre un fallo de predicción.  

**¿Quiénes se benefician y quiénes podrían ser perjudicados?**  
Beneficiarios: pacientes con enfermedades crónicas, sector hospitalario, personal médico, desarrolladores e investigadores de IA.  
Perjudicados potenciales: pacientes de grupos minoritarios o zonas rurales, si no se garantiza representatividad continua en los datos.  

---

## 6. Responsabilidad  

**¿Quién es responsable si el modelo falla?**  
- **Desarrolladores:** del mantenimiento técnico, modelo y seguridad del código.  
- **Científicos de datos:** del control de calidad y sesgo en el entrenamiento.  
- **Product Owner:** ya que es el propietario del servicio 
- **Comité clínico:** de la validación médica antes de aplicar decisiones, en el caso de que el prototipo se llegara a implementar.  
- **Pacientes:** si se hace uso indebido de la plataforma, misma que **no debe ser utilizada como sustituto de atención médica, diagnóstico, tratamiento ni seguimiento clínico profesional**.

**¿Qué mecanismos de accountability existen?**  
- **Model Card** con métricas, versiones y limitaciones.  
- **Registro automatizado de predicciones (logs)** y revisión médica de errores.  
- **Auditorías de sesgo trimestrales**.  
- **Canal de apelación médica** para revisión de casos erróneos.  

**Plan de monitoreo y actualización:**  
- Reentrenamiento trimestral con nuevos datos.  
- Monitoreo continuo de *drift* en glucosa, hemoglobina y presión.  
- Actualización automática del modelo mediante *CI/CD* supervisado, (Continuous Integration / Continuous Deployment).  

---

## 7. Uso Dual y mal uso  

**¿Podría el modelo usarse con fines maliciosos?**  
Sí, de forma hipotética, si terceros lo aplicaran fuera del ámbito clínico (por ejemplo, aseguradoras o empleadores para discriminación sanitaria).  

**¿Qué salvaguardas se han implementado?**  
- Licencia de uso restringido para investigación y diagnóstico asistido.  
- Autenticación obligatoria de usuarios en el entorno Streamlit.  
- Registro de uso (logs de acceso y decisiones).  

**Limitaciones de uso documentadas:**  
> CliniCareAI es un sistema de apoyo clínico.  
> No reemplaza el juicio médico ni debe usarse para diagnóstico automatizado sin supervisión profesional.  

---

## 8. Limitaciones Reconocidas  

**¿En qué casos NO debe usarse el modelo?**  
- Diagnósticos automáticos sin validación médica.  
- Pacientes pediátricos, embarazadas o con patologías no representadas.  
- Contextos donde no se dispone de datos fisiológicos confiables.  

**¿Qué advertencias deben darse a los usuarios?**  
- Las predicciones son **estimaciones probabilísticas**, no diagnósticos definitivos.  
- Requieren revisión por un médico antes de tomar decisiones terapéuticas.  
- El rendimiento del modelo depende de la calidad y actualización de los datos.  

**Casos límite donde el modelo no es confiable:**  
- Datos con valores fuera del rango fisiológico (ej., glucosa > 600 mg/dL).  
- Registros incompletos o alterados por errores de medición.  
- Escenarios de comorbilidades múltiples no presentes en el conjunto de entrenamiento.  


---

## 📚 Referencias  

[1] IEEE Global Initiative on Ethics of Autonomous and Intelligent Systems, *Ethically Aligned Design*, 2021.  
[2] European Commission, *Ethics Guidelines for Trustworthy AI*, 2022.  
[3] Ley Orgánica de Protección de Datos Personales (LOPDP), Ecuador, 2021.  
[4] Lundberg, S. M., & Lee, S. I. (2017). *A Unified Approach to Interpreting Model Predictions*, NeurIPS.  
[5] Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). *“Why Should I Trust You?” Explaining the Predictions of Any Classifier*, KDD.  
