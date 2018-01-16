#!/usr/bin/python3

import argparse
import paho.mqtt.client as mqtt

def parse_args():
    """Parse one argument from command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="Message to publish")
    args = parser.parse_args()
    return args.message

message = parse_args()

client = mqtt.Client()
client.connect("localhost")
print("Publishing message to topic", "paho/test")
client.publish("paho/test", message)