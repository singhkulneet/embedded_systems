# -----------------------------------------------------------------------------
# Script Name: simulator.py
# Script Funtion: To simulate TI Boards publishing messages to MQTT
# Date Created: 04/02/2020
# Author: Kulneet Singh
# -----------------------------------------------------------------------------

# Neccesary Libraries
import time
import datetime
import paho.mqtt.client as mqtt
import json
from collections import defaultdict

# Function ran whenever script publishes anything
def on_publish(client,userdata,result):             #create function for callback
    print('Data published with ret code: ' + str(result))

# Set-up info for cloudmqtt
broker_address = 'soldier.cloudmqtt.com'
port = 10132
user = 'KC'
password = 'kc'

# Establishing connection with cloudmqtt server
client = mqtt.Client('simulator')
client.username_pw_set(user, password=password)
client.on_publish = on_publish
client.connect(broker_address, port=port)

# publishing topic information for all components with one second sleeps in between
ret =  client.publish("topics", "{\"id\": \"pixy\", \"pub\": 1, \"rec\": 0, \"t1\": \"\", \"t2\": \"\", \"t3\": \"\", \"t4\": \"\"}")
time.sleep(1)
ret =  client.publish("topics", "{\"id\": \"rover\", \"pub\": 1, \"rec\": 0, \"t1\": \"pixy\", \"t2\": \"ultra\", \"t3\": \"arm\", \"t4\": \"\"}")
time.sleep(1)
ret =  client.publish("topics", "{\"id\": \"ultra\", \"pub\": 1, \"rec\": 0, \"t1\": \"\", \"t2\": \"\", \"t3\": \"\", \"t4\": \"\"}")
time.sleep(1)
ret =  client.publish("topics", "{\"id\": \"arm\", \"pub\": 1, \"rec\": 0, \"t1\": \"pixy\", \"t2\": \"rover\", \"t3\": \"\", \"t4\": \"\"}")
time.sleep(1)

# Pixy publishing message of current status
timenow = datetime.datetime.now()
ret =  client.publish("pixy", "{\"id\": \"pixy\", \"pub\": 2, \"rec\": 0, \"x_coordinate\": 10, \"y_coordinate\": 5, \"height\": 2, \"width\": 1, \"signature\": 1, \"time\": " + str(timenow.strftime("%H%M%S")) + "}")
time.sleep(1)

# Rover publishing message of moving after reciving message from pixy
timenow = datetime.datetime.now()
ret =  client.publish("rover", "{\"id\": \"rover\", \"pub\": 2, \"rec\": 1, \"status\": \"moving\", \"atDestination\": \"false\", \"time\": " + str(timenow.strftime("%H%M%S")) + "}")
time.sleep(1)

# Ultrasonic Sensor publishing message of distance
timenow = datetime.datetime.now()
ret =  client.publish("ultra", "{\"id\": \"ultra\", \"pub\": 2, \"rec\": 0, \"distance\": 6, \"time\": " + str(timenow.strftime("%H%M%S")) + "}")
time.sleep(1)

# Rover publishing message of atDestination and stopped after reciving message from pixy and ultra
timenow = datetime.datetime.now()
ret =  client.publish("rover", "{\"id\": \"rover\", \"pub\": 3, \"rec\": 2, \"status\": \"stopped\", \"atDestination\": \"true\", \"time\": " + str(timenow.strftime("%H%M%S")) + "}")
time.sleep(1)

# Arm publishing message of searching and then retrieved after reciving message from pixy and rover
timenow = datetime.datetime.now()
ret =  client.publish("arm", "{\"id\": \"arm\", \"pub\": 2, \"rec\": 3, \"status\": \"searching\", \"time\": " + str(timenow.strftime("%H%M%S")) + "}")
time.sleep(1)
timenow = datetime.datetime.now()
ret =  client.publish("arm", "{\"id\": \"arm\", \"pub\": 3, \"rec\": 3, \"status\": \"retrieved\", \"time\": " + str(timenow.strftime("%H%M%S")) + "}")
time.sleep(1)

# Rover publishing message of moving after reciving message from arm
timenow = datetime.datetime.now()
ret =  client.publish("rover", "{\"id\": \"rover\", \"pub\": 4, \"rec\": 4, \"status\": \"moving\", \"atDestination\": \"false\", \"time\": " + str(timenow.strftime("%H%M%S")) + "}")
time.sleep(1)

# Error: Ultrasonic Sensor publishing incorrect number of pubs
timenow = datetime.datetime.now()
ret =  client.publish("ultra", "{\"id\": \"ultra\", \"pub\": 4, \"rec\": 0, \"distance\": 10, \"time\": " + str(timenow.strftime("%H%M%S")) + "}")
time.sleep(1)

# Error: Rover publishing message with wrong number of fields
timenow = datetime.datetime.now()
ret =  client.publish("rover", "{\"id\": \"rover\", \"pub\": 5, \"rec\": 5}")
time.sleep(1)

# End of simulation
# Disconnecting from cloudmqtt
client.disconnect()

# letting user know that script has executed
print("End of simulation")