from numpy import double


nombre = input("Ingresa tu nombre: ")
texto = input("Ingresa tu texto: ")
id = input("Ingresa tu id: ")

print ("INSERT INTO rfid (nombre,texto,rfid) VALUES ('"+nombre+"','"+texto+"',"+id+");")