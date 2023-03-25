import re
import random
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('ey.db')
cursor = conn.cursor()


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}
    ID_Respuesta=1
    # Consulta a la base de datos para obtener las posibles respuestas
    cursor.execute('SELECT ID_Respuesta, Respuesta, Palabras, single_response, required_words FROM respuestash WHERE ID_Respuesta={}'.format(ID_Respuesta))
    rows = cursor.fetchall()

    # Iterar a través de las posibles respuestas y calcular la probabilidad de cada una
    for row in rows:
        response_text = row[1]
        recognized_words = row[2].split(',')
        required_words = row[3].split(',')
        single_response = bool(row[4])

        # Calcular la probabilidad de la respuesta
        prob = message_probability(message, recognized_words, single_response, required_words)

        # Guardar la probabilidad para cada respuesta
        highest_prob[response_text] = prob

    # Seleccionar la respuesta con la probabilidad más alta
    best_match = max(highest_prob, key=highest_prob.get)

    # Si la probabilidad es menor que 1, devolver una respuesta desconocida
    if highest_prob[best_match] < 1:
        return unknown()
    else:
        return best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))