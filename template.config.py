#Copy as config.py and change values as needed

MQTT_SERVER="localhost"
CLIENT_NAME="rf_thermometers"

TOPIC_PREFIX="house/thermometers/"

#{id:location}
#ID is reported by each thermometer
#Location is used to create topic name
THERMOMETERS={
    1:"bedroom",
    2:"kitchen",
    3:"outside"
}