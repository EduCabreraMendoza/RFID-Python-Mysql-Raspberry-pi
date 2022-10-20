#Bibliotecas
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='laloremoto', password='2907', host='192.168.100.131', database='codigoIoT')

#Query
query = ("SELECT * FROM rfid WHERE id=1;")

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