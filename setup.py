#Setup to run on a device before running any of these scripts
import os

os.system("python3 -m venv ./venv")
os.system("venv/bin/pip3 install rpi-gpio")
os.system("venv/bin/pip3 install paho-mqtt")
os.system("sudo apt install mosquitto mosquitto-clients -y && sudo systemctl enable mosquitto.service && sudo systemctl start mosquitto.service")

# To run on main device
#venv/bin/python3 numpad.py

# To run on receiver device
#venv/bin/python3 receive.py