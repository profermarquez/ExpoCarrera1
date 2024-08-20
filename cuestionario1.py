import streamlit as st
import pandas as pd

# Título del cuestionario
st.markdown('<a name="top"></a>', unsafe_allow_html=True)
st.title('Cuestionario: Las ciencias de datos')
#Preguntas

p1=st.radio("¿Cuánto interés tienes en aprender a programar?", 
                                ('Mucho', 'Algo', 'Poco', 'Ninguno'), 
                                key='interes_programacion')
p2=st.radio("¿Qué lenguajes de programación conoces o te gustaría aprender?", 
                                        ('Python', 'JavaScript', 'Java', 'TypeScript','Ninguno'), 
                                        key='lenguajes_programacion')

p3=st.radio("¿Has desarrollado algún proyecto de software o aplicación?", 
                             ('Ninguno','Sí, por mi cuenta', 'Sí, en un curso o taller', 'No, pero me gustaría', 'No, y no me interesa'), 
                             key='proyecto_software')

p4=st.radio("¿Cuánto tiempo al día utilizas dispositivos tecnológicos (teléfono, computadora, tablet, etc.)?", 
                             ('Nunca','Menos de 2 horas', '2-4 horas', '4-6 horas', 'Más de 6 horas'), 
                             key='tiempo_tecnologia')

p5=st.radio("¿Qué tan cómodo te sientes utilizando nuevas tecnologías?", 
                                ('Muy cómodo', 'Cómodo', 'Poco cómodo', 'Incómodo','Ninguno'), 
                                key='comodidad_tecnologia')

p6=st.radio("¿Qué dispositivo tecnológico consideras indispensable en tu día a día?", 
                                     ('Teléfono', 'Computadora', 'Tablet', 'Televisor','Ninguno'), 
                                     key='dispositivo_indispensable')

p7=st.radio("¿Sabes qué es el análisis de datos?", 
                                       ('Sí, lo conozco bien', 'Sí, he oído hablar de ello', 'No, pero me gustaría saber más', 'No, y no me interesa'), 
                                       key='conocimiento_analisis_datos')

p8=st.radio("¿Has utilizado alguna vez herramientas para analizar datos (como Excel, Google Sheets, Power BI)?", 
                                  ('Sí, frecuentemente', 'Sí, algunas veces', 'No, pero me gustaría aprender', 'No, y no me interesa'), 
                                  key='uso_herramientas_datos')
p9=st.radio("¿Qué tan importante crees que es el análisis de datos en la toma de decisiones?", 
                                      ('Muy importante', 'Algo importante', 'Poco importante', 'No es importante'), 
                                      key='importancia_analisis_datos')

p10=st.radio("¿Qué tan familiarizado estás con el concepto de inteligencia artificial (IA)?", 
                           ('Muy familiarizado', 'Algo familiarizado', 'Poco familiarizado', 'Nada familiarizado'), 
                           key='familiaridad_ia')

p11=st.radio("¿Crees que la inteligencia artificial será útil en tu futura carrera profesional?", 
                       ('Sí, definitivamente', 'Probablemente', 'No estoy seguro', 'No, no lo creo'), 
                       key='utilidad_ia')

p12=st.radio("¿Qué aplicaciones de inteligencia artificial te parecen más interesantes?", 
                                 ('Asistente virtual Siri','Asistente virtual Alexa','Recomendaciones personalizadas de Netflix o Spotify','Recomendaciones personalizadas de  Spotify', 
                                  'Automóviles autónomos', 'Chat GPT','Gemini', 'Ninguno','Asistente virtual Google Assistant'), 
                                 key='aplicaciones_ia')




def enviar():
    respuestas = {
        'interes programación': p1,
        'lenguajes programación': p2,
        'proyecto software':p3,
        'tiempo tecnología': p4,
        'comodidad tecnología': p5,
        'dispositivo indispensable': p6,
        'conocimiento datos': p7,
        'uso herramientas': p8,
        'importancia análisis': p9,
        'familiaridad ia': p10,
        'utilidad ia': p11,
        'aplicaciones ia': p12,
    }
    
    # Crear un DataFrame y guardar en un archivo CSV
    df = pd.DataFrame([respuestas])
    df.to_csv('cuestionario_resultados.csv', mode='a', header=not pd.io.common.file_exists('cuestionario_resultados.csv'), index=False)

    st.session_state.interes_programacion = 'Ninguno'
    st.session_state.lenguajes_programacion= 'Ninguno'
    st.session_state.proyecto_software= 'Ninguno'
    st.session_state.tiempo_tecnologia= 'Nunca'
    st.session_state.comodidad_tecnologia= 'Ninguno'
    st.session_state.dispositivo_indispensable= 'Ninguno'
    st.session_state.conocimiento_analisis_datos= 'No, y no me interesa'
    st.session_state.uso_herramientas_datos= 'No, y no me interesa'
    st.session_state.importancia_analisis_datos= 'No es importante'
    st.session_state.familiaridad_ia= 'Nada familiarizado'
    st.session_state.utilidad_ia= 'No, no lo creo'
    st.session_state.aplicaciones_ia= 'Ninguno'
    js_scroll_top = """
    <script>
        window.location.href = '#top';
    </script>
    """
    st.components.v1.html(js_scroll_top, height=0)
    
    

st.button('Enviar', on_click=enviar)
st.markdown('[Ir al inicio](#top)')