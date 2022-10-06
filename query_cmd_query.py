import mysql.connector

cnx = mysql.connector.connect(user='lalo', password='2907', host='127.0.0.1', database='codigoIoT')
#cursor = cnx.cursor()

query = ("SELECT * FROM historicoAPI;")

#cursor.execute(query)
res = cnx.cmd_query(query)

print("Respueta: ")
print(res)

#cursor.close()
cnx.close()