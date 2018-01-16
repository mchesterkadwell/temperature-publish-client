#!/usr/bin/python3

import sys
import json

import paho.mqtt.client as mqtt

from config import *

def on_publish(client, userdata, msg):
    print("Publishing message %s to topic %s" % (str(msg), topic))

client = mqtt.Client(CLIENT_NAME)
client.on_publish = on_publish
client.connect(MQTT_SERVER)

last_message = ""
for message in sys.stdin:
    if not message.isspace() and message != last_message:
        last_message = message
        parsed_message = json.loads(message)
        thermometer_id = parsed_message['id']
        thermometer_location = THERMOMETERS[thermometer_id]
        topic = TOPIC_PREFIX + thermometer_location
        client.publish(topic, message.rstrip())