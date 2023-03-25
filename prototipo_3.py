import mysql.connector
import nltk
from nltk.tokenize import word_tokenize
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="preguntas"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM respuestas")

results = mycursor.fetchall()
def get_keywords(text):
    tokens = word_tokenize(text)
    keywords = [word.lower() for word in tokens if word.isalnum()]
    return keywords
def get_matching_response(keywords, results):
    matching_responses = []

    for row in results:
        if row[3] == 'True':
            if all(word in row[2] for word in keywords):
                matching_responses.append(row[1])
        else:
            if any(word in row[2] for word in keywords):
                    matching_responses.append(row[1])

    if matching_responses:
        return matching_responses
    else:
        return None
def send_response(response):
    print(response)
while True:
    question = input("Pregúntame algo: ")
    keywords = get_keywords(question)
    response = get_matching_response(keywords, results)
    if response:
        send_response(response)
    else:
        send_response("Lo siento, no entiendo tu pregunta")
