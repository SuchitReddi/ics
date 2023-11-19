import paho.mqtt.client as mqtt
import os

topic = "suchit/image"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    f=open("./img/intruder_compressed.jpeg", "rb")
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    #print(byteArr)
    client.publish(topic, byteArr, 2)
    print("Published")
    print("Redirecting to numpad.py")
    os.system("venv/bin/python3 numpad.py") #Anything after this line does not execute.

client = mqtt.Client()
client.on_connect = on_connect
client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
