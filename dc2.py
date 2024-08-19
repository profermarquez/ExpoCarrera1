import numpy as np
import pandas as pd
import time
import plotly.express as px
import streamlit as st

df = pd.read_csv("cuestionario_resultados.csv")

st.set_page_config(
    page_title='Ciencia de Datos Dashboard',
    page_icon='✅',
    layout='wide'
)

# Título del dashboard
st.title("Ciencia de Datos Science Dashboard")

# Filtro de selección
programming_interest_filter = st.selectbox("Selecciona el lenguaje de programación", pd.unique(df['lenguajes programación']))

# Contenedor de un solo elemento
placeholder = st.empty()

# Filtrar el dataframe
df = df[df['lenguajes programación'] == programming_interest_filter]

# Simulación de feed en tiempo real
for seconds in range(200):
    df['comodidad tecnología nuevo'] = df['comodidad tecnología'].apply(lambda x: np.random.choice(['Cómodo', 'Muy cómodo']))

    # Crear KPIs
    count_lang = df.shape[0]
    count_comfy = df[df['comodidad tecnología nuevo'] == 'Muy cómodo'].shape[0]

    with placeholder.container():
        # Crear dos columnas
        kpi1, kpi2 = st.columns(2)

        # Llenar las dos columnas con las métricas o KPIs respectivos
        kpi1.metric(label=f"Usuarios de {programming_interest_filter}", value=count_lang)
        kpi2.metric(label="Muy Cómodo 💻", value=count_comfy, delta=count_comfy - count_lang//2)

        # Crear dos columnas para los gráficos
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### Distribución de interés en programación")
            fig = px.histogram(data_frame=df, x='interes programación')
            st.write(fig)
        with fig_col2:
            st.markdown("### Comodidad con la tecnología")
            fig2 = px.histogram(data_frame=df, x='comodidad tecnología nuevo')
            st.write(fig2)
        
        st.markdown("### Vista Detallada de los Datos")
        st.dataframe(df)
        
        time.sleep(1)