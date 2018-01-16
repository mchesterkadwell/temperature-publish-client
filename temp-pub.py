#!/usr/bin/python3

import sys
import paho.mqtt.client as mqtt

message = sys.argv[1]

client = mqtt.Client()
client.connect("localhost")
print("Publishing message to topic", "paho/test")
client.publish("paho/test", message)