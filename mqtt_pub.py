import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

try:
    while True:
        print("Actions Available:")
        print("1.- ON - turns led on")
        print("2.- OFF - turns led off")
        print("F - Quit the program")
        message = input("> ")
        if message.upper() == "F":
            print("Finishing and disconnecting...")
            break
        client.publish("ALSW/LED", message.upper())
        print(f"Published: {message}")
finally:
    client.disconnect()
    print("Disconnected from broker.")
