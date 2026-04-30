# 🩺 Diabetes Data Explorer — Streamlit App

## Descripción
Aplicación web interactiva para explorar el dataset de diabetes de Pima Indians. Permite filtrar datos y visualizar patrones clave asociados al diagnóstico de diabetes mediante 5 tipos de visualizaciones interactivas.

## Dataset
- **Fuente**: UCI Machine Learning Repository / Kaggle
- **URL**: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
- **Descripción**: 768 registros de pacientes femeninas de origen Pima (≥21 años) con 8 variables clínicas y diagnóstico de diabetes.
- **Variables**: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome

## Hallazgos Principales
1. **Glucosa es el predictor más fuerte**: Correlación r=0.47 con el diagnóstico. Pacientes diabéticas tienen glucosa media ~40 mg/dL más alta.
2. **Prevalencia sube con la edad**: Pasa del ~24% en 21-30 años a más del 50% en mayores de 50.
3. **BMI elevado potencia el riesgo**: El cluster de alto riesgo se concentra con Glucosa >126 mg/dL + BMI >30.
4. **Función de pedigrí discrimina**: DiabetesPedigreeFunction refleja historial familiar y diferencia significativamente entre grupos.
5. **35% de prevalencia global**: 268 de 768 pacientes tienen diagnóstico positivo; la distribución es desbalanceada.

## Visualizaciones Implementadas
1. **Box plot + barras agrupadas**: Comparación de variables clínicas por diagnóstico y grupo etario.
2. **Histograma + KDE + rug plot**: Distribución de cualquier variable numérica con umbral clínico de referencia.
3. **Scatter plot con regresión OLS**: Relación entre dos variables seleccionables, coloreado por diagnóstico.
4. **Donut chart + barras de prevalencia**: Composición global y prevalencia por grupo etario.
5. **Heatmap de correlación + barras de correlación con Outcome**: Todas las relaciones entre variables.

## Buenas Prácticas Aplicadas
- **Accesibilidad**: Paleta IBM Color Blind Safe (azul `#0072B2` / naranja `#E69F00`) — segura para todos los tipos de daltonismo.
- **Data-ink ratio alto**: Sin bordes innecesarios, grillas mínimas, sin 3D.
- **Títulos con insight**: Cada gráfico comunica el hallazgo, no solo el tipo.
- **Preprocesamiento ético**: Zeros imposibles tratados como NaN y documentados.
- **Interactividad**: Sidebar con filtros por edad, diagnóstico y embarazos.

## Tecnologías Utilizadas
- **Framework**: Streamlit 1.35
- **Lenguaje**: Python 3.11
- **Bibliotecas**: Plotly, Pandas, NumPy, Statsmodels

## Instalación y Ejecución Local

### Requisitos Previos
- Python 3.9+
- pip

### Instrucciones
```bash
git clone https://github.com/usuario/diabetes-streamlit.git
cd diabetes-streamlit
pip install -r requirements.txt
streamlit run app.py
```

## Despliegue
URL en producción: [Por definir — Streamlit Community Cloud]

## Autores
- Fabian Vasquez
- Maria Paula Riveros
