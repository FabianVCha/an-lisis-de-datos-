import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configuración de página
st.set_page_config(page_title="Análisis Clínico de Diabetes", layout="wide")

# --- Gestión de Tema y Estilos ---
with st.sidebar:
    st.title("Configuración")
    dark_mode = st.toggle("Modo Oscuro", value=False)
    st.divider()

# Definición de paleta profesional
# No Diabetes: Azul profundo | Diabetes: Coral/Naranja vibrante
COLOR_MAP = {"No Diabetes": "#1F77B4", "Diabetes": "#E63946"}
THEME_TEMPLATE = "plotly_dark" if dark_mode else "plotly_white"
BG_COLOR = "#0E1117" if dark_mode else "#FFFFFF"
TEXT_COLOR = "#E0E0E0" if dark_mode else "#262730"

# --- Carga de Datos ---
@st.cache_data
def load_and_clean_data():
    # Asegúrate de que el archivo diabetes.csv esté en el mismo directorio
    df = pd.read_csv("diabetes.csv")
    cols_to_fix = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    df[cols_to_fix] = df[cols_to_fix].replace(0, np.nan)
    df["Diagnosis"] = df["Outcome"].map({0: "No Diabetes", 1: "Diabetes"})
    
    bins = [20, 35, 50, 65, 100]
    labels = ["Adulto Joven", "Adulto", "Adulto Mayor", "Senectud"]
    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)
    return df

try:
    df_raw = load_and_clean_data()
except FileNotFoundError:
    st.error("Error: No se encontró el archivo 'diabetes.csv'.")
    st.stop()

# --- Filtros ---
with st.sidebar:
    st.header("Filtros de Datos")
    age_range = st.slider("Rango de Edad", int(df_raw.Age.min()), int(df_raw.Age.max()), (21, 81))
    selected_diag = st.multiselect("Categoría de Diagnóstico", 
                                   ["No Diabetes", "Diabetes"], 
                                   default=["No Diabetes", "Diabetes"])
    
    df = df_raw[
        (df_raw.Age.between(*age_range)) & 
        (df_raw.Diagnosis.isin(selected_diag))
    ].copy()

# --- Encabezado ---
st.title("Dashboard de indicadores clínicos: Diabetes")
st.markdown(f"""
    **Análisis de población Pima Indians** | Muestras procesadas: {len(df)} 
    *Los valores nulos (codificados como 0 en el dataset original) han sido excluidos para mantener la integridad estadística.*
""")

# KPIs
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Total Pacientes", len(df))
with c2:
    prev = (df["Outcome"].mean() * 100)
    st.metric("Prevalencia", f"{prev:.1f}%")
with c3:
    avg_glucose = df[df.Outcome == 1]["Glucose"].mean()
    st.metric("Promedio Glucosa (Positivos)", f"{avg_glucose:.1f} mg/dL")
with c4:
    avg_bmi = df[df.Outcome == 1]["BMI"].mean()
    st.metric("Promedio BMI (Positivos)", f"{avg_bmi:.1f}")

st.divider()

# --- Layout de Gráficas ---
tab1, tab2, tab3 = st.tabs(["Análisis de Distribución", "Correlaciones", "Relaciones Multivariadas"])

# TAB 1: Boxplots e Histogramas
with tab1:
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Distribución por Variable (Boxplot)")
        var_to_plot = st.selectbox("Seleccione variable:", ["Glucose", "BMI", "Insulin", "BloodPressure", "Age"])
        
        fig_box = px.box(
            df.dropna(subset=[var_to_plot]),
            x="Diagnosis", y=var_to_plot,
            color="Diagnosis",
            color_discrete_map=COLOR_MAP,
            template=THEME_TEMPLATE,
            points="outliers",
            notched=True
        )
        fig_box.update_layout(showlegend=False, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_box, use_container_width=True)

    with col_right:
        st.subheader("Frecuencia y Densidad (Histograma)")
        fig_hist = px.histogram(
            df.dropna(subset=[var_to_plot]),
            x=var_to_plot, color="Diagnosis",
            color_discrete_map=COLOR_MAP,
            template=THEME_TEMPLATE,
            barmode="overlay",
            marginal="rug"
        )
        fig_hist.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_hist, use_container_width=True)

# TAB 2: Mapas de Calor y Barras
with tab2:
    col_corr, col_bar = st.columns([1.2, 1])
    
    with col_corr:
        st.subheader("Matriz de Correlación de Pearson")
        numeric_cols = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "Age", "Outcome"]
        corr_matrix = df[numeric_cols].corr()
        
        fig_heat = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale="RdBu",
            zmin=-1, zmax=1,
            text=np.round(corr_matrix.values, 2),
            texttemplate="%{text}",
        ))
        fig_heat.update_layout(template=THEME_TEMPLATE, height=450)
        st.plotly_chart(fig_heat, use_container_width=True)
        
    with col_bar:
        st.subheader("Prevalencia por Grupo Etario")
        age_data = df.groupby("AgeGroup", observed=True)["Outcome"].mean().reset_index()
        age_data["Outcome"] *= 100
        
        fig_bar = px.bar(
            age_data, x="AgeGroup", y="Outcome",
            labels={"Outcome": "Porcentaje con Diabetes (%)", "AgeGroup": "Rango de Edad"},
            template=THEME_TEMPLATE,
            color_discrete_sequence=[COLOR_MAP["Diabetes"]]
        )
        fig_bar.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_bar, use_container_width=True)

# TAB 3: Diagramas de Dispersión
with tab3:
    st.subheader("Interacción entre Factores de Riesgo (Dispersión)")
    
    c_x, c_y, c_size = st.columns(3)
    var_x = c_x.selectbox("Eje X", ["Glucose", "BMI", "Age"], index=0)
    var_y = c_y.selectbox("Eje Y", ["BMI", "Glucose", "Insulin"], index=1)
    var_s = c_size.selectbox("Tamaño del punto (opcional)", ["None", "Age", "Pregnancies"], index=0)

    scatter_args = {
        "data_frame": df.dropna(subset=[var_x, var_y]),
        "x": var_x, "y": var_y,
        "color": "Diagnosis",
        "color_discrete_map": COLOR_MAP,
        "template": THEME_TEMPLATE,
        "opacity": 0.6,
        "trendline": "ols" # Requiere statsmodels: pip install statsmodels
    }
    
    if var_s != "None":
        scatter_args["size"] = var_s

    try:
        fig_scatter = px.scatter(**scatter_args)
        fig_scatter.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_scatter, use_container_width=True)
    except Exception:
        # Fallback si statsmodels no está instalado para la línea de tendencia
        del scatter_args["trendline"]
        fig_scatter = px.scatter(**scatter_args)
        st.plotly_chart(fig_scatter, use_container_width=True)

# --- Pie de Página ---
st.markdown("---")
st.caption("Uso exclusivo académico y profesional. Los datos presentados son de carácter informativo.")