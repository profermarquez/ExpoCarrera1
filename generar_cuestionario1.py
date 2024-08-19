import csv
import random

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

# Crear el archivo CSV
with open('cuestionario_resultados.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Escribir el encabezado
    writer.writerow(opciones.keys())
    
    # Generar y escribir 500 filas de datos aleatorios
    for _ in range(500):
        row = [random.choice(opciones[key]) for key in opciones]
        writer.writerow(row)

print("Archivo 'cuestionario_resultados.csv' generado con éxito.")