import re
import random
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="preguntas",
    port=3306
)

prueba=1

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

        mycursor = mydb.cursor()
        guayaba=1
        mycursor.execute('SELECT * FROM respuestas WHERE id = %s', (guayaba,))
        resultado = mycursor.fetchone()
        mycursor.execute('SELECT * FROM respuestas')
        resultados = mycursor.fetchall()

        def response(bot_response= resultado[1], list_of_words= resultado[2], single_response = resultado[3] , required_words = [resultado[3]]):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)
            

        for resultado in resultados:
            response()
            guayaba += 1

        
        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))
