import nltk
from nltk.corpus import stopwords
import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')
c = conn.cursor()



# Función para buscar la respuesta a una pregunta en la base de datos
def buscar_respuesta(pregunta):
    # Convertir la pregunta a minúsculas y eliminar las palabras vacías (stop words)
    pregunta = pregunta.lower()
    stop_words = set(stopwords.words('spanish'))
    palabras = nltk.word_tokenize(pregunta)
    palabras = [palabra for palabra in palabras if palabra not in stop_words]
    pregunta = ' '.join(palabras)

    # Buscar la respuesta en la base de datos
    c.execute("SELECT respuesta FROM pregunta WHERE pregunta=?", (pregunta,))
    respuesta = c.fetchone()

    if respuesta:
        return respuesta[0]
    else:
        return "Lo siento, no pude entender tu pregunta"

# Función principal para el asistente virtual
def asistente():
    print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte?")
    while True:
        pregunta = input("Pregunta: ")
        if pregunta.lower() == 'salir':
            break
        else:
            respuesta = buscar_respuesta(pregunta)
            print("Respuesta:", respuesta)

    print("¡Hasta luego!")

# Ejecutar el asistente virtual
asistente()

# Cerrar la conexión a la base de datos
conn.close()