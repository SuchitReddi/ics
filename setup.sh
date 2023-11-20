#Setup to run on a device before running any of these scripts

python3 -m venv ./venv
venv/bin/pip3 install rpi-gpio
venv/bin/pip3 install paho-mqtt
sudo apt install mosquitto mosquitto-clients -y && sudo systemctl enable mosquitto.service && sudo systemctl start mosquitto.service

# To run on main device
#venv/bin/python3 numpad.py

# To run on receiver device
#venv/bin/python3 receive.py
