import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lubrirepuestos", layout="wide")
st.title("📦 Inventario - Lubrirepuestos")

# Subida de archivo
archivo = st.file_uploader("📤 Sube tu archivo Excel", type=["xlsx"])
streamlit
pandas
openpyxl

if archivo:
    df = pd.read_excel(archivo, sheet_name=None)

    secciones = list(df.keys())
    pestaña = st.selectbox("📂 Selecciona la pestaña a analizar", secciones)

    datos = df[pestaña]

    st.markdown("### 📊 Vista previa")
    st.dataframe(datos)

    if "Estado de venta" in datos.columns:
        conteo = datos["Estado de venta"].value_counts()
        st.markdown("### 📈 Análisis de estado de venta")
        st.bar_chart(conteo)

    st.success("✅ Análisis completado.")
else:
    st.info("Por favor sube el archivo Excel para comenzar.")
