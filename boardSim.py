# -----------------------------------------------------------------------------
# Script Name: boardSim.py
# Script Funtion: To simulate TI Boards publishing messages to MQTT
# Date Created: 05/06/2020
# Author: Kulneet Singh
# -----------------------------------------------------------------------------

# Neccesary Libraries
import time
import datetime
import paho.mqtt.client as mqtt
import json
from collections import defaultdict

# Function ran whenever script publishes anything
def on_publish(client,userdata,result):      #create function for callback
    print('Data published with ret code: ' + str(result))

# Set-up info for server
broker_address = "172.16.0.29"
port = 1883

# Establishing connection with RPi server
client = mqtt.Client('boardSim')
client.on_publish = on_publish
client.connect(broker_address, port=port)

print("Start of Simulation:")

ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 120, \"motor1\": 120, \"motor2\": 120, \"motor3\": 120}")
time.sleep(3)

ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 90, \"motor2\": 90, \"motor3\": 90}")
time.sleep(3)

print("End of Simulation.")