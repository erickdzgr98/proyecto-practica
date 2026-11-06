import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
import plotly.express as px

st.set_page_config(page_title="Dashboard Canino", page_icon="🐾", layout="wide")

st.title("🐾 Analítica y Gestión de Perros")
st.markdown("Visualización en tiempo real conectada a PostgreSQL.")

# Conexión con PostgreSQL usando variables de entorno de docker-compose
db_user = os.getenv("DB_USER", "admin")
db_password = os.getenv("DB_PASSWORD", "securepassword")
db_host = os.getenv("DB_HOST", "db")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME", "perros_db")

db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

@st.cache_data(ttl=30)
def get_data():
    return pd.read_sql("SELECT * FROM perritos;", engine)

try:
    df = get_data()

    # Métricas principales
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total de Perros Registrados", len(df))
    kpi2.metric("En Espera de Adopción", len(df[df["estado_adopcion"] == "Disponible"]))
    kpi3.metric("Edad Media (meses)", round(df["edad_meses"].mean(), 1))

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribución por Estado de Adopción")
        fig_pie = px.pie(
            df,
            names="estado_adopcion",
            title="Proporción de Estado Actual",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("Población por Tamaño")
        conteo_tam = df["tamanio"].value_counts().reset_index()
        conteo_tam.columns = ["Tamaño", "Cantidad"]
        fig_bar = px.bar(
            conteo_tam,
            x="Tamaño",
            y="Cantidad",
            title="Perros según Tamaño",
            color="Tamaño",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with st.expander("Ver tabla completa de datos"):
        st.dataframe(df, use_container_width=True)

except Exception as err:
    st.error(f"Error al conectar con la base de datos: {err}")
