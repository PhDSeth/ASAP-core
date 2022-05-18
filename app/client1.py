
import paho.mqtt.client as mqtt 
from random import randrange, uniform, gammavariate
import time

mqttBroker ="mqtt.eclipseprojects.io" 

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 

while True:
    randNumber = gammavariate(30,2)
    client.publish("SENSORDATA", randNumber)
    print("Just published (heart rate) " + str(randNumber) + " to topic SENSORDATA")
    time.sleep(1)