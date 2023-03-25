import pymysql

class Database:
    def __init__(self):
        self.connection= pymysql.connect(
            user='root',password='',
            host='localhost',
            db='preguntas',
            port=3306
        )

        self.cursor=self.connection.cursor()
 

    def mostrar_pregunta(self,ID_Respuesta):
        sql= 'SELECT ID_Respuesta, Respuesta, Palabras, single_response, required_words FROM respuestas WHERE ID_Respuesta={}'.format(ID_Respuesta)  

        try:
            self.cursor.execute(sql)
            respuesta= self.cursor.fetchone()

            print("ID_Respuesta:", respuesta[0])
            print("Respuesta:", respuesta[1])
            print("Palabras:", respuesta[2])
            print("single_response:", respuesta[3])
            print("required_words:", respuesta[4])
        except Exception as e:
            raise 
    
    def mostrar_todo(self):
        sql='SELECT ID_Respuesta, Respuesta, Palabras, single_response, required_words FROM respuestas'
        
        try:
            self.cursor.execute(sql)
            respuestas= self.cursor.fetchone()

            for ID_Respuesta in respuestas:
                print("ID_Respuesta:", respuestas[0])
                print("Respuesta:", respuestas[1])
                print("Palabras:", respuestas[2])
                print("single_response:", respuestas[3])
                print("required_words:", respuestas[4])
                print("______\n")

        except Exception as e:
            raise 
         

db= Database()
db.mostrar_pregunta(2)
print("donde caemos gente!")