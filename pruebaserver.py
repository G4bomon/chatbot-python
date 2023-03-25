import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="preguntas",
    port=3306
)
mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM respuestas WHERE ID_Respuesta = 1')
resultado = mycursor.fetchone()
prueba=1

print(resultado[1])

