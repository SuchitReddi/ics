import paho.mqtt.client as mqtt
import os
import sys

topic = "suchit/image"

# Hide traceback
sys.tracebacklimit=0
SHOW_STACK_TRACE=False

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe, which need to put into on_connect
    # If reconnect after losing the connection with the broker, it will continue to subscribe to the suchit/image topic
    client.subscribe(topic)
    print("Subscribed to " + topic)
    print("Waiting for image...")

# The callback function, it will be triggered when receiving messages
def on_message(client, userdata, msg):
    #print(f"{msg.topic} {msg.payload}")
    os.system("mkdir img")
    f = open('./img/intruder_received.jpeg', "wb")
    f.write(msg.payload)
    print("Image Received")
    f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally, it will send the will message to other clients
client.will_set('suchit/image', b'{"status": "Off"}')

# Create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
client.connect("test.mosquitto.org", 1883, 60)

# Set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
client.loop_forever()
