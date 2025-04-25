#a 0.5 MAMP

import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

# Pines del motor
A = 17
B = 27
C = 22
D = 18

# Secuencia de pasos
secuencia = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)

# Función para girar el motor
def paso(pasos, sentido=1):
    secuencia_utilizada = secuencia if sentido == 1 else list(reversed(secuencia))
    for _ in range(pasos):
        for paso in secuencia_utilizada:
            GPIO.output(A, paso[0])
            GPIO.output(B, paso[1])
            GPIO.output(C, paso[2])
            GPIO.output(D, paso[3])
            time.sleep(0.002)

# Función al conectar al broker MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado con código: " + str(rc))
    client.subscribe("ALSW/ORDEN")

# Extraer el texto del mensaje
def extract_text(bstring):
    return bstring.strip()[2:-1]

# Función que recibe los mensajes
def motorControl(client, userdata, msg):
    action = extract_text(str(msg.payload))
    match action:
        case "A":
            print("Girando 45 grados en sentido horario ")
            paso(50, sentido=1)
        case "B":
            print("Girando 90 grados en sentido horario")
            paso(50, sentido=1)
        case "C":
            print("Girando 135 grados en sentido horario")
            paso(50, sentido=1)
        case "D":
            print("Girando 180 grados en sentido horario")
            paso(50, sentido=1)
        case "I":
            print("Posicion inicial")
            paso(200, sentido=-1)
        case _:
            print(f"Comando desconocido: {action}")

# Configuración MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = motorControl

# Conexión al broker
client.connect("test.mosquitto.org", 1883, 60)

try:
    print("Esperando comandos MQTT...")
    client.loop_forever()
except KeyboardInterrupt:
    print("Finalizando...")
finally:
    GPIO.cleanup()
