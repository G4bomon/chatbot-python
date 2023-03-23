import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="preguntas",
    port=3306
)
mycursor = mydb.cursor()
def mostrar_pregunta(ID_Respuesta):
    mycursor.execute ('SELECT * FROM respuestas WHERE WHERE ID_Respuesta={}').format(ID_Respuesta)
    resultado = mycursor.fetchone()
    print(resultado)

mostrar_pregunta(2)
#print('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)