#Bibliotecas
import mysql.connector

#Programa
#Conexión a la base de datos
print("Intentado conectar con la base de datos")
cnx = mysql.connector.connect(user='lalo', password='2907', host='127.0.0.1', database='codigoIoT')
print("Conexión exitosa")
print(cnx)

#Desconexión de la base de datos
print("Finalizando conexión")
cnx.close()
print("Conexión cerrada")