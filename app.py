import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lubrirepuestos", layout="wide")

# Título principal
st.title("📦 Lubrirepuestos - Inventario")

# Subir archivo Excel
archivo = st.file_uploader("📁 Sube el archivo Excel del inventario", type=["xlsx"])

if archivo is not None:
    try:
        excel = pd.ExcelFile(archivo)
        hojas = excel.sheet_names

        pestaña = st.selectbox("Selecciona la hoja que deseas analizar:", hojas)
        df = pd.read_excel(archivo, sheet_name=pestaña)

        st.subheader(f"📋 Inventario: {pestaña}")
        st.dataframe(df, use_container_width=True)

        if "CANTIDAD" in df.columns:
            total_productos = df["CANTIDAD"].sum()
            st.info(f"🔢 Total de productos registrados en esta hoja: **{total_productos}**")

        if "ESTADO DE VENTA" in df.columns:
            vendidos = df["ESTADO DE VENTA"].value_counts()
            st.success("📊 Estado de ventas:")
            st.write(vendidos)

        if "GANANCIA Q" in df.columns:
            total_ganancia = df["GANANCIA Q"].sum()
            st.warning(f"💰 Ganancia total estimada: **Q{total_ganancia:.2f}**")

    except Exception as e:
        st.error(f"❌ Error al procesar el archivo: {e}")
else:
    st.warning("📎 Por favor, sube tu archivo Excel para empezar.")
