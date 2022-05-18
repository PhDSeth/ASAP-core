import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

# we need to define the location of the MQTT Broker (line 5). 
# I am using the free online broker Eclipse Mosquitto, but you can use an
mqttBroker ="mqtt.eclipseprojects.io" 


client = mqtt.Client("body_temp") #creates a new client. Client id
client.connect(mqttBroker) #connect the client to the broker

while True:
    randNumber = uniform(36.4, 36.7)
    client.publish("SENSORDATA", randNumber)
    print("Just published (body temp)" + str(randNumber) + " to topic SENSORDATA")
    time.sleep(1)