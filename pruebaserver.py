import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="preguntas",
    port=3306
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM respuestas WHERE ID_Respuesta=2')
resultado = mycursor.fetchone()

print(resultado[1])


#print('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)