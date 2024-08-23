import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="Input Personalizado", layout="centered")

# Estilos CSS personalizados
st.markdown("""
<style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .output-text {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 4px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Crear un campo de texto en Streamlit para recibir el valor del input HTML
valor_html = st.text_input("Valor del input:", key="html_input_value")

# Función para manejar la captura del valor del input
def obtener_valor_html():
    components.html(
        f"""
        <style>
            #myInput {{
                width: 100%;
                padding: 12px 20px;
                margin: 8px 0;
                box-sizing: border-box;
                border: 2px solid #ccc;
                border-radius: 4px;
            }}
            #sendButton {{
                background-color: #008CBA;
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 4px;
            }}
            #sendButton:hover {{
                background-color: #007B9A;
            }}
        </style>
        <input type="text" id="myInput" placeholder="Escribe algo aquí">
        <button id="sendButton" onclick="document.getElementById('streamlitInput').value = document.getElementById('myInput').value; document.getElementById('streamlitSubmit').click();">Enviar valor</button>
        <input type="hidden" id="streamlitInput" name="streamlitInput" value="{valor_html}">
        <input type="submit" id="streamlitSubmit" style="display:none;">
        """,
        height=150
    )

# Título de la aplicación
st.title("Input Personalizado")

# Mostrar el input HTML y capturar el valor
obtener_valor_html()

# Botón para verificar el valor
if st.button('Verificar valor'):
    st.markdown(f"<div class='output-text'>Valor ingresado: {valor_html}</div>", unsafe_allow_html=True)
