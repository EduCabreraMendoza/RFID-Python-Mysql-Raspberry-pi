import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('Nuevos datos:')
        print("Ahora acerca un tag para escribir")
        reader.write(text)
        print("Escrito")
finally:
        GPIO.cleanup()