import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="preguntas",
    port=3306
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM respuestas")
resultado = mycursor.fetchone()
print(resultado)
