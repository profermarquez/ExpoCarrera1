import streamlit as st
import pandas as pd

# Título del cuestionario
st.markdown('<a name="top"></a>', unsafe_allow_html=True)
st.title("Cuestionario: Habilidades Blandas")
def disable_enter_submit():
    # Prevent the default form submission behavior
    pass

# Preguntas
preguntas = {
    'expresar_ideas': "¿Qué tan cómodo te sientes al expresar tus ideas en grupo?",
    'buen_oyente': "¿Consideras que eres un buen oyente cuando otros comparten sus ideas?",
    'trabajo_equipo': "¿Cómo te sientes al trabajar en equipo en proyectos escolares o extracurriculares?",
    'rol_equipo': "¿Qué rol prefieres asumir cuando trabajas en equipo?",
    'importancia_colaboracion': "¿Qué tan importante consideras que es la colaboración para el éxito de un proyecto?",
    'reaccion_problemas': "¿Cómo reaccionas cuando te enfrentas a un problema difícil en tus estudios?",
    'nuevas_soluciones': "¿Qué tan frecuentemente buscas nuevas maneras de resolver problemas?",
    'adaptacion': "¿Qué tan fácil te resulta adaptarte a nuevas situaciones o cambios?",
    'aprender_nuevas_herramientas': "¿Cómo te sientes al aprender nuevas herramientas o métodos de estudio?",
    'manejo_tiempo': "¿Cómo manejas tu tiempo al realizar tareas o estudiar para exámenes?",
    'efectividad_tiempo': "¿Qué tan efectivo consideras que es tu manejo del tiempo?",
    'cuestionar_informacion': "¿Con qué frecuencia cuestionas la información que recibes antes de aceptarla?",
    'evaluar_puntos_vista': "¿Qué tan cómodo te sientes al evaluar diferentes puntos de vista antes de tomar una decisión?"
}

opciones = {
    'expresar_ideas': ['Muy cómodo', 'Cómodo', 'Poco cómodo', 'Incomodo'],
    'buen_oyente': ['Sí, siempre', 'Generalmente sí', 'A veces', 'No, me cuesta prestar atención'],
    'trabajo_equipo': ['Muy cómodo', 'Cómodo', 'Poco cómodo', 'Incomodo'],
    'rol_equipo': ['Líder', 'Facilitador', 'Seguidor', 'No tengo una preferencia clara'],
    'importancia_colaboracion': ['Muy importante', 'Importante', 'Poco importante', 'No es importante'],
    'reaccion_problemas': ['Busco soluciones inmediatamente', 'Pido ayuda', 'Me siento frustrado pero lo intento', 'Me rindo fácilmente'],
    'nuevas_soluciones': ['Muy frecuentemente', 'Frecuentemente', 'Ocasionalmente', 'Raramente'],
    'adaptacion': ['Muy fácil', 'Fácil', 'Difícil', 'Muy difícil'],
    'aprender_nuevas_herramientas': ['Entusiasmado', 'Interesado', 'Neutral', 'Incomodo'],
    'manejo_tiempo': ['Planifico con antelación y sigo mi plan', 'Intento planificar, pero a veces me retraso', 'Trabajo sin mucha planificación', 'Suelo procrastinar y hacer todo al último momento'],
    'efectividad_tiempo': ['Muy efectivo', 'Efectivo', 'Poco efectivo', 'Ineficiente'],
    'cuestionar_informacion': ['Siempre', 'Frecuentemente', 'Algunas veces', 'Raramente'],
    'evaluar_puntos_vista': ['Muy cómodo', 'Cómodo', 'Poco cómodo', 'Incomodo']
}

respuestas = {}

for key, pregunta in preguntas.items():
    respuestas[key] = st.radio(pregunta, opciones[key], key=key)

p13 = correo = st.text_input("Introduce tu dirección de correo electrónico:", key='correo', value='noreply@isfdyt.com',help="",on_change=disable_enter_submit,)
st.markdown("""
<style>
div.stTextInput > div.st-my-1 > div:nth-child(2) {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

use_email = st.checkbox("Utilizar este correo electrónico como información de contacto")

if not use_email:
    p13 = 'noreply@isfdyt.com'

def enviar():
    # Crear un DataFrame y guardar en un archivo CSV
    df = pd.DataFrame([respuestas])
    df.to_csv('cuestionario_habilidades_blandas.csv', mode='a', header=not pd.io.common.file_exists('cuestionario_habilidades_blandas.csv'), index=False)

    # Reiniciar todas las respuestas
    for key in respuestas:
        st.session_state[key] = opciones[key][-1]
    st.session_state.correo = "" if use_email else "noreply@isfdyt.com"

    js_scroll_top = """
    <script>
    alert("Gracias por responder!")
    window.location.href = '#top';

    
    </script>
    """
    st.components.v1.html(js_scroll_top, height=0)

st.button('Enviar', on_click=enviar)
st.markdown('[Ir al inicio](#top)')
