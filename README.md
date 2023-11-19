# intruder_capture_system_mqtt
This IoT project uses a raspberry pi, a keypad and camera module connected to a server via mqtt. The camera sends a captured image if the input pin is wrong.

Run setup.py on both subscriber and publisher.
Run receiver.py on subscriber first.
Run numpad.py on publisher once subscriber shows the message "Subscribed to <topic>"
