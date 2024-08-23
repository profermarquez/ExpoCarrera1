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

# Función para manejar la captura del valor del input
def obtener_valor_html():
    components.html(
        """
        <style>
            #myInput {
                width: 100%;
                padding: 12px 20px;
                margin: 8px 0;
                box-sizing: border-box;
                border: 2px solid #ccc;
                border-radius: 4px;
            }
            #sendButton {
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
            }
            #sendButton:hover {
                background-color: #007B9A;
            }
        </style>
        <input type="text" id="myInput" placeholder="Escribe algo aquí">
        <button id="sendButton" onclick="window.parent.postMessage(document.getElementById('myInput').value, '*')">Enviar valor</button>
        <script>
            window.addEventListener('message', (event) => {
                const value = event.data;
                const iframe = window.frameElement;
                iframe.contentWindow.parent.postMessage(value, '*');
            });
        </script>
        """,
        height=150
    )

# Título de la aplicación
st.title("Input Personalizado")

# Mostrar el input HTML y capturar el valor
obtener_valor_html()

# Variable para almacenar el valor enviado
if 'html_input_value' not in st.session_state:
    st.session_state['html_input_value'] = ''

# Botón para verificar el valor
if st.button('Verificar valor'):
    st.markdown(f"<div class='output-text'>Valor ingresado: {st.session_state['html_input_value']}</div>", unsafe_allow_html=True)

# Captura el valor recibido desde el componente HTML
components.html(
    """
    <script>
        window.addEventListener('message', function(event) {
            const value = event.data;
            window.parent.postMessage({type: 'st-session-state', value: value}, '*');
        });
    </script>
    """,
    height=0
)

# Escuchar mensajes de la ventana principal y actualizar session_state
query_params = st.query_params
st.session_state['html_input_value'] = query_params.get('st-session-state', [''])[0]