import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("cuestionario_resultados.csv")

# Definir las opciones para cada pregunta
opciones = {
    'interes programación': ['Mucho', 'Algo', 'Poco', 'Ninguno'],
    'lenguajes programación': ['Python', 'JavaScript', 'Java', 'TypeScript', 'Ninguno'],
    'proyecto software': ['Ninguno', 'Sí, por mi cuenta', 'Sí, en un curso o taller', 'No, pero me gustaría', 'No, y no me interesa'],
    'tiempo tecnología': ['Nunca', 'Menos de 2 horas', '2-4 horas', '4-6 horas', 'Más de 6 horas'],
    'comodidad tecnología': ['Muy cómodo', 'Cómodo', 'Poco cómodo', 'Incómodo', 'Ninguno'],
    'dispositivo indispensable': ['Teléfono', 'Computadora', 'Tablet', 'Televisor', 'Ninguno'],
    'conocimiento datos': ['Sí, lo conozco bien', 'Sí, he oído hablar de ello', 'No, pero me gustaría saber más', 'No, y no me interesa'],
    'uso herramientas': ['Sí, frecuentemente', 'Sí, algunas veces', 'No, pero me gustaría aprender', 'No, y no me interesa'],
    'importancia análisis': ['Muy importante', 'Algo importante', 'Poco importante', 'No es importante'],
    'familiaridad ia': ['Muy familiarizado', 'Algo familiarizado', 'Poco familiarizado', 'Nada familiarizado'],
    'utilidad ia': ['Sí, definitivamente', 'Probablemente', 'No estoy seguro', 'No, no lo creo'],
    'aplicaciones ia': ['Asistente virtual Siri', 'Asistente virtual Alexa', 'Recomendaciones personalizadas de Netflix o Spotify', 'Recomendaciones personalizadas de Spotify', 'Automóviles autónomos', 'Chat GPT', 'Gemini', 'Ninguno', 'Asistente virtual Google Assistant']
}

# Función para contar respuestas
def contar_respuestas(df, pregunta):
    return df[pregunta].value_counts().reindex(opciones[pregunta], fill_value=0).tolist()

# Función de la encuesta adaptada
def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig

# Crear los resultados para las preguntas seleccionadas
resultados = {pregunta: contar_respuestas(df, pregunta) for pregunta in opciones}

# Seleccionar una pregunta para graficar
pregunta_seleccionada = st.selectbox("Selecciona una pregunta para graficar:", list(resultados.keys()))

# Generar y mostrar el gráfico
fig = survey({pregunta_seleccionada: resultados[pregunta_seleccionada]}, opciones[pregunta_seleccionada])
st.pyplot(fig)
