# -----------------------------------------------------------------------------
# Script Name: boardSim.py
# Script Funtion: To simulate a TI Board publishing messages to MQTT
# Date Created: 05/06/2020
# Author: Kulneet Singh
# -----------------------------------------------------------------------------

# Neccesary Libraries
import time
import datetime
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json
from collections import defaultdict

# Function ran whenever script publishes anything
def on_publish(client,userdata,result):      #create function for callback
    print('Sent MoveMotor with ret code: ' + str(result))

# Set-up info for server
broker_address = "172.16.0.29"
port = 1883

# Establishing connection with RPi server
client = mqtt.Client('boardSim')
client.on_publish = on_publish
client.connect(broker_address, port=port)

print("Start of Simulation:")

val = 0
while val != -1:
    val = input("Testcase # to run or '-1' to end sim: ")
    if val == 1:
        print("\nRunning test case 1...")
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 90, \"motor2\": 70, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 100, \"motor2\": 90, \"motor3\": 160}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 37, \"motor1\": 160, \"motor2\": 100, \"motor3\": 40}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 160, \"motor2\": 90, \"motor3\": 40}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 160, \"motor2\": 90, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 100, \"motor2\": 90, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        print("Recieved done.\n")
    
    elif val == 2:
        print("\nRunning test case 2...")
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 180, \"motor1\": 90, \"motor2\": 80, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 160, \"motor2\": 100, \"motor3\": 40}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 160, \"motor2\": 100, \"motor3\": 40}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 110, \"motor2\": 85, \"motor3\": 160}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 110, \"motor2\": 85, \"motor3\": 160}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 110, \"motor2\": 85, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 100, \"motor2\": 90, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        print("Recieved done.\n")

    elif val == 3:
        print("\nRunning test case 3...")
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 90, \"motor2\": 80, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 100, \"motor2\": 90, \"motor3\": 160}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 30, \"motor2\": 150, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 180, \"motor1\": 10, \"motor2\": 150, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 100, \"motor2\": 90, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        print("Recieved done.\n")

    elif val == 4:
        print("\nRunning test case 4...")
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 180, \"motor1\": 10, \"motor2\": 100, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 30, \"motor2\": 150, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 37, \"motor1\": 110, \"motor2\": 90, \"motor3\": 160}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 110, \"motor2\": 80, \"motor3\": 160}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 100, \"motor2\": 90, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        print("Recieved done.\n")

    elif val == 5:
        print("\nRunning test case 5...")
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 90, \"motor2\": 80, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 160, \"motor2\": 100, \"motor3\": 40}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 37, \"motor1\": 160, \"motor2\": 100, \"motor3\": 40}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 30, \"motor2\": 130, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 180, \"motor1\": 10, \"motor2\": 150, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 100, \"motor2\": 90, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        print("Recieved done.\n")

    elif val == 6:
        print("\nRunning test case 6...")
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 180, \"motor1\": 10, \"motor2\": 100, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 30, \"motor2\": 150, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 37, \"motor1\": 160, \"motor2\": 100, \"motor3\": 40}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 170, \"motor2\": 90, \"motor3\": 40}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 100, \"motor2\": 90, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        print("Recieved done.\n")

    elif val == 7:
        print("\nRunning test case 7...")
        ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 90, \"motor1\": 90, \"motor2\": 90, \"motor3\": 90}")
        msg = subscribe.simple("/server/DoneMoving", msg_count=2)
        print("Recieved done.\n")

    elif val != -1:
        print("Error: Invalid input try again...")

client.disconnect()

print("End of Simulation.")