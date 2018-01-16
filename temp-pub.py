#!/usr/bin/python3

import sys

import paho.mqtt.client as mqtt

import config

client = mqtt.Client()
client.connect(config.host)
print("Publishing message to topic", "paho/test")
for message in sys.stdin:
    if not message.isspace():
        client.publish("paho/test", message.rstrip())