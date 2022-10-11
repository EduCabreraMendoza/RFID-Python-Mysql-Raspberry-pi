#Bibliotecas
import mysql.connector
from time import sleep
import sys
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

#Conexión
cnx = mysql.connector.connect(user='laloremoto', password='2907', host='192.168.100.131', database='codigoIoT')

#Cursor
cursor = cnx.cursor()

try:
    while True:
        #Lectura del tag
        print("Acerca un tag al lector")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))

        #Query
        query_insert = ("INSERT INTO rfid (nombre,texto,rfid) VALUES ('Lalo','"+text+"',"+id+");")

        #Petición
        cursor.execute(query_insert)

        #Asegurarse de que la incercion de datos fue correcta
        cnx.commit()
        print("Query OK")

        sleep(5)
except KeyboardInterrupt:
    #Final de la conexión
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    raise