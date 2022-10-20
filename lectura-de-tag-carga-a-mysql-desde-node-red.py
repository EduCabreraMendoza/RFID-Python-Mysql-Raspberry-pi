#Bibliotecas
import mysql.connector
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import argparse


# Parser
parser = argparse.ArgumentParser()
parser.add_argument("texto")
textoTag = parser.parse_args()


reader = SimpleMFRC522()

#Conexión
cnx = mysql.connector.connect(user='laloremoto', password='2907', host='192.168.100.131', database='codigoIoT')

#Cursor
cursor = cnx.cursor()

try:
    
    #Lectura del tag
    print("Acerca un tag al lector")
    id, text = reader.read()
    datos = str.split(",")
    print("ID: %s\nText: %s" % (id,text))
    #Query
    query_insert = ("INSERT INTO rfid (nombre,texto,rfid) VALUES ('"+datos[0]+"','"+textoTag.texto+"',"+str (id)+");")

    #Petición
    cursor.execute(query_insert)

    #Asegurarse de que la incercion de datos fue correcta
    cnx.commit()
    print("Query OK")

    #Final de la conexión
    cursor.close()
    cnx.close()
    GPIO.cleanup()

    sleep(5)
except KeyboardInterrupt:
    #Final de la conexión
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    raise