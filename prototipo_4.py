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

def get_response(question):
    tokens = word_tokenize(question.lower())
    keywords = [word for word in tokens if word.isalnum()]

    if len(keywords) == 1:
        response = [row[1] for row in results if row[2].lower() == keywords[0]]
    elif len(keywords) == 2:
        response = [row[1] for row in results if row[2].lower() == keywords[0] and row[3].lower() == keywords[1]]
    else:
        response = "Lo siento, no puedo ayudarte con esa pregunta."

    return response

while True:
    question = input("Hazme una pregunta: ")
    response = get_response(question)
    print(response)
