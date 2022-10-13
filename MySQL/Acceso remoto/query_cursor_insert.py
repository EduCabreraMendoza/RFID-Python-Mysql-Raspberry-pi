#Bibliotecas
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='laloremoto', password='2907', host='192.168.100.131', database='codigoIoT')

#Query
query_insert = ("INSERT INTO rfid (nombre,texto,rfid) VALUES ('Lalo','Raspberry Pi 2',128725897278);")

#Petición
cursor = cnx.cursor()
cursor.execute(query_insert)

#Asegurarse de que la incercion de datos fue correcta
cnx.commit()
print("Query OK")

#Final de la conexión
cursor.close()
cnx.close()