import numpy as np
import pandas as pd
import time
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
df = pd.read_csv("cuestionario_habilidades_blandas.csv")

st.set_page_config(
    page_title='Habilidades Blandas Dashboard',
    page_icon='🧠',
    layout='wide'
)

# Título del dashboard
st.title("Dashboard de Habilidades Blandas")

# Filtro de selección
rol_equipo_filter = st.selectbox("Selecciona el rol preferido en equipo", pd.unique(df['rol_equipo']))

# Contenedor de un solo elemento
placeholder = st.empty()

# Filtrar el dataframe
df_filtered = df[df['rol_equipo'] == rol_equipo_filter]

# Simulación de feed en tiempo real
for seconds in range(200):
    df_filtered['adaptacion_nuevo'] = df_filtered['adaptacion'].apply(lambda x: np.random.choice(['Muy fácil', 'Fácil', 'Difícil', 'Muy difícil']))

    # Crear KPIs
    count_rol = df_filtered.shape[0]
    count_adaptable = df_filtered[df_filtered['adaptacion_nuevo'].isin(['Muy fácil', 'Fácil'])].shape[0]

    with placeholder.container():
        # Crear dos columnas
        kpi1, kpi2 = st.columns(2)

        # Llenar las dos columnas con las métricas o KPIs respectivos
        kpi1.metric(label=f"Personas con rol {rol_equipo_filter}", value=count_rol)
        kpi2.metric(label="Adaptables 🔄", value=count_adaptable, delta=count_adaptable - count_rol//2)

        # Crear dos columnas para los gráficos
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### Distribución de comodidad al expresar ideas")
            fig = px.histogram(data_frame=df_filtered, x='expresar_ideas')
            st.write(fig)
        with fig_col2:
            st.markdown("### Distribución de adaptabilidad")
            fig2 = px.histogram(data_frame=df_filtered, x='adaptacion_nuevo')
            st.write(fig2)
        
        # Gráfico adicional
        st.markdown("### Importancia de la colaboración vs. Efectividad en el manejo del tiempo")
        fig3 = px.scatter(data_frame=df_filtered, x='importancia_colaboracion', y='efectividad_tiempo')
        st.write(fig3)
        
        st.markdown("### Vista Detallada de los Datos")
        st.dataframe(df_filtered)
        
        time.sleep(1)