#Bibliotecas
import mysql.connector

#Programa
#Conexión a la base de datos
print("Intentado conectar con la base de datos")
cnx = mysql.connector.connect(user='laloremoto', password='2907', host='192.168.100.131', database='codigoIoT')
print("Conexión exitosa")
print(cnx)

#Desconexión de la base de datos
print("Finalizando conexión")
cnx.close()
print("Conexión cerrada")