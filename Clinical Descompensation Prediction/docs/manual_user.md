## 2️⃣ Guía paso a paso para usar la interfaz  

La aplicación fue desarrollada en **Streamlit** y cuenta con un entorno simple e interactivo que facilita el análisis clínico predictivo.  
A continuación, se describen los pasos principales para el uso correcto del sistema:

1. **Inicio:**  
   - Ejecuta el comando `streamlit run app.py` para abrir la interfaz en el navegador.  
   - Espera unos segundos mientras se carga el modelo y los datos clínicos.  

2. **Visualización general:**  
   - En el menú lateral o superior, selecciona la pestaña que desees analizar.  
   - Cada pestaña contiene opciones y gráficas específicas para el tipo de análisis que se quiera realizar.

3. **Análisis individual:**  
   - En la pestaña *Explorador por Paciente*, selecciona el ID del paciente y revisa la evolución de sus métricas fisiológicas.

4. **Simulación de próxima visita:**  
   - En la pestaña *Simulación (Próxima visita)*, introduce nuevos valores o modifica las variables del paciente para predecir su posible estado futuro.

5. **Revisión de resultados:**  
   - Observa los gráficos, métricas y tablas generadas para interpretar los posibles diagnósticos o riesgos clínicos.

📸 *(Aquí se colocarán las imágenes que acompañen cada paso del proceso, mostrando el menú principal y las pestañas de la interfaz.)*

---

## 3️⃣ Capturas de pantalla anotadas  

En esta sección se insertarán capturas reales de la interfaz con anotaciones que describan las funciones principales:
  
- **Explorador por paciente:** ejemplo de evolución de variables.  
- **Simulación:** visualización de resultados al cambiar valores.  
- **Acerca de:** parámetros, clases y distribución de datos.

📍 *(Cada imagen incluirá notas explicativas o flechas indicando los botones y gráficos más relevantes.)*

---

## 4️⃣ Explicación de funcionalidades  

Al ingresar al sistema, el usuario encontrará un menú con las siguientes secciones principales:

| Pestaña | Descripción |
|----------|-------------|
| 👤 **Explorador por Paciente** | Permite analizar individualmente la evolución de las métricas fisiológicas de cada paciente, comparando sus variables en el tiempo. |
| 🔮 **Simulación (Próxima visita)** | Permite seleccionar el ID de un paciente, modificar los valores de las variables y observar cómo cambia la predicción del modelo. |
| 📘 **Acerca de:** | Presenta la información técnica del modelo, las clases utilizadas, la distribución de datos y los parámetros empleados en el entrenamiento. |

---

## 5️⃣ Troubleshooting (Problemas comunes y soluciones)  

| Problema | Posible causa | Solución |
|-----------|----------------|-----------|
| La aplicación tarda en cargar el dataset. | El archivo contiene casi un millón de registros. | Esperar unos segundos hasta que se complete la carga. Puede optimizarse usando muestreo o una versión reducida del dataset. |
| El gráfico no se actualiza al cambiar parámetros. | Error de actualización del navegador o del caché de Streamlit. | Presionar `Ctrl + F5` o reiniciar la app con `streamlit run app.py`. |
| No se muestra la predicción. | Campos incompletos o variables fuera de rango. | Verificar que todos los valores estén dentro de los límites fisiológicos esperados. |
| Error al cargar datos. | Falta el archivo `dataset_balanceado_SMOTEENN.csv`. | Confirmar que el archivo esté en el mismo directorio del proyecto. |

---

## 6️⃣ FAQ (Preguntas Frecuentes)  

**1. ¿Puedo usar mis propios datos de pacientes?**  
Sí. Puede reemplazar el archivo `dataset_balanceado_SMOTEENN.csv` por otro con la misma estructura de columnas.  

**2. ¿El modelo realiza diagnósticos médicos?**  
No. Este sistema **no reemplaza la valoración médica profesional**. Las predicciones sirven únicamente como apoyo para la toma de decisiones clínicas.  

**3. ¿Por qué las métricas cambian entre ejecuciones?**  
Debido a la división aleatoria de los datos de entrenamiento y prueba en cada ejecución.  

**4. ¿Cómo puedo exportar los resultados?**  
Puedes tomar capturas o exportar tablas desde el navegador (clic derecho → *Guardar como CSV* si Streamlit lo permite).  

---

## 7️⃣ Información de contacto  

Para soporte técnico o consultas sobre el sistema:

**Desarrolladores:**  
- **Fernando Xavier Montaño Cárdenas**
- **María Fernanda Bolaños**

📧 **Correo de contacto:** soporte.prediccionclinica@gmail.com  
🌐 **Repositorio oficial:** [GitHub - prediccion_clinica](https://github.com/Clinical-Decompensation-Prediction/Clinical-Decompensation-Prediction.git)