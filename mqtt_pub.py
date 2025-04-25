import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

try:
    while True:
        print("Actions Available:")
        print("1.- A - 45 grados")
        print("2.- B - 90 grados")
        print("3.- C - 135 grados")
        print("4.- D - 180 grados")
        print("5.- I - Posicion inicial")
        print("F - Terminar programa")
        message = input("> ")
        if message.upper() == "F":
            print("Finishing and disconnecting...")
            break
        client.publish("ALSW/ORDEN", message.upper())
        print(f"Published: {message}")
finally:
    client.disconnect()
    print("Disconnected from broker.")
