#!/usr/bin/python3

import paho.mqtt.client as mqtt

client = mqtt.Client()
mqttc.connect("localhost")
print("Publishing message to topic","paho/test")
client.publish("paho/test","Test message!")