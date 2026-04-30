---

# Diabetes data explorer

¡Bienvenido! Este proyecto nace de la curiosidad por entender cómo diferentes factores clínicos influyen en el diagnóstico de la diabetes. Utilizando el dataset de **Pima Indians**, hemos construido una herramienta interactiva que no solo muestra datos, sino que cuenta la historia detrás de ellos.

 **Ver la App en vivo:** [fabianpaulapp.streamlit.app](https://fabianpaulapp.streamlit.app/)

---

## ¿Qué buscamos con este análisis?
A través de esta plataforma, exploramos patrones críticos. No nos limitamos a graficar; buscamos hallazgos que tengan sentido clínico, como:
* **El poder de la Glucosa:** Confirmamos que es el predictor más fuerte, con una diferencia clara de ~40 mg/dL entre pacientes.
* **El factor edad:** Observamos cómo la prevalencia se duplica al pasar de los 20 a los 50 años.
* **Riesgos combinados:** Identificamos que la combinación de Glucosa >126 y BMI >30 marca un punto de inflexión importante.

## Una experiencia visual e incluyente
Diseñamos esta app pensando en la claridad y la accesibilidad:
* **Para todos:** Usamos la paleta **IBM Color Blind Safe**, garantizando que las visualizaciones sean comprensibles para personas con daltonismo.
* **Interactividad total:** Tú decides qué ver. Filtra por edad, historial de embarazos o diagnóstico desde la barra lateral.
* **Cinco niveles de análisis:** Desde mapas de calor para ver correlaciones hasta gráficos de dispersión con regresión estadística.

## Detrás de escena (Tecnologías)
Para este desarrollo utilizamos un stack moderno y eficiente:
* **Cerebro:** Python 3.11.
* **Interfaz:** Streamlit.
* **Visualización Dinámica:** Plotly (Express & Graph Objects).
* **Análisis:** Pandas, NumPy y Statsmodels.

## Cómo probarlo en tu máquina
Si quieres explorar el código o mejorarlo, sigue estos pasos:

1. **Clona el proyecto:**
   ```bash
   git clone https://github.com/FabianVCha/an-lisis-de-datos-.git
   cd an-lisis-de-datos-
   ```
2. **Prepara tu entorno:**
   ```bash
   pip install -r requirements.txt
   ```
3. **¡Lánzalo!**
   ```bash
   streamlit run app.py
   ```

---

## 👥 El Equipo
Este proyecto fue desarrollado con pasión por:
* **Fabian Vasquez** — [GitHub](https://github.com/FabianVCha)
* **Maria Paula Riveros**

---

### Notas de actualización
* **Abril 2026:** Migración exitosa a Python 3.11 para mejorar la estabilidad en el despliegue de Streamlit Cloud.

