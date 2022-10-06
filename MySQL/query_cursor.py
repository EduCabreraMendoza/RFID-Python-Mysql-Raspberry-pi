#Bibliotecas
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='lalo', password='2907', host='127.0.0.1', database='detectorsintomas')

#Query
query = ("SELECT id,nombre,temp,bpm,sp02 FROM registro WHERE protodiagnostico='Signos vitales anormales, se le recomienda visitara a un médico';")

#Petición
cursor = cnx.cursor()
cursor.execute(query)
res = cursor.fetchall()

#Impresion del resultado
for x in res:
    print(x)

#Final de la conexión
cursor.close()
cnx.close()