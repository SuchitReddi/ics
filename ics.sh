main() {

	echo "Welcome to Intruder Capture System!!"
	echo
	echo "Select how this device functions:  "
	echo "[1] Access Control System / Publisher (Sends alerts if auth fails)"
	echo "[2] Command and Control Server / Subscriber (Receives alerts)"

		read -p "Select an option: " number
		echo
		case $number in
			1)
			echo "Setting up this device as a Access Control System..."
			venv/bin/python3 numpad.py
			;;
			2)
			echo "Setting up this device as a Command and Control Server..."
			venv/bin/python3 receive.py
			;;
			*)
			echo "Select a valid option (1 or 2)"
			echo
			main
			;;
		esac
}

main
