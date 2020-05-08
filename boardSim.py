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
from signal import signal, SIGINT
from sys import exit

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

# Defining test cases 
def testCase1():
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

def testCase2():
    print("\nRunning test case 2...")
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 180, \"motor1\": 90, \"motor2\": 80, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 170, \"motor2\": 85, \"motor3\": 40}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 40, \"motor1\": 160, \"motor2\": 110, \"motor3\": 40}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 40, \"motor1\": 170, \"motor2\": 110, \"motor3\": 40}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 40, \"motor1\": 110, \"motor2\": 85, \"motor3\": 160}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 110, \"motor2\": 85, \"motor3\": 160}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 110, \"motor2\": 70, \"motor3\": 160}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 110, \"motor2\": 70, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 100, \"motor2\": 90, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    print("Recieved done.\n")

def testCase3():
    print("\nRunning test case 3...")
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 90, \"motor2\": 80, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 100, \"motor2\": 100, \"motor3\": 160}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 37, \"motor1\": 30, \"motor2\": 150, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 180, \"motor1\": 10, \"motor2\": 150, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 100, \"motor2\": 90, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    print("Recieved done.\n")

def testCase4():
    print("\nRunning test case 4...")
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 180, \"motor1\": 10, \"motor2\": 100, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 40, \"motor1\": 30, \"motor2\": 150, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 40, \"motor1\": 110, \"motor2\": 90, \"motor3\": 160}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"DROP\", \"motor0\": 180, \"motor1\": 110, \"motor2\": 80, \"motor3\": 160}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 100, \"motor2\": 90, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    print("Recieved done.\n")

def testCase5():
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

def testCase6():
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

def testCase7():
    print("\nRunning test case 7...")
    ret =  client.publish("/cc3200/MoveMotors", "{\"type\": \"PICK\", \"motor0\": 90, \"motor1\": 90, \"motor2\": 90, \"motor3\": 90}")
    msg = subscribe.simple("/server/DoneMoving", msg_count=2)
    print("Recieved done.\n")

def runLoop():
    val = 0
    while val != -1:
        val = input("\nTestcase # (1-6) to run, '10' to run script, '-1' to end sim: ")
        if val == 1:
            testCase1()
        elif val == 2:
            testCase2()
        elif val == 3:
            testCase3()
        elif val == 4:
            testCase4()
        elif val == 5:
            testCase5()
        elif val == 6:
            testCase6()
        elif val == 7:
            testCase7()
        elif val == 10:
            testCase1()
            time.sleep(1)
            testCase2()
            time.sleep(1)
            testCase3()
            time.sleep(1)
            testCase4()
            time.sleep(1)
            testCase1()
            time.sleep(1)
            testCase5()
            time.sleep(1)
            testCase6()
            time.sleep(1)
            testCase2()
        elif val == -1:
            print("End of Simulation.")
            client.disconnect()
            exit(0)
        else:
            print("Error: Invalid input try again...")

def handler(signal_received, frame):
    print('\nSIGINT or CTRL-C detected. Running default test case, then restarting')
    val = input("Restart (1) or Exit (0): ")
    if val == 1:
        testCase7()
        runLoop()
    else:
        print("End of Simulation.")
        client.disconnect()
        exit(0)

if __name__ == '__main__':
    print("Start of Simulation:")
    signal(SIGINT, handler)
    runLoop()
    client.disconnect()
    print("End of Simulation.")