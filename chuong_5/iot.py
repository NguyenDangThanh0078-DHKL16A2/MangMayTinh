import network
import time
import json
from machine import Pin
from umqtt.simple import MQTTClient
import dht


sensor = dht.DHT22(Pin(2))

ssid = "your_wifi_ssid"  # Replace with your Wi-Fi SSID
password = "your_wifi_password"  # Replace with your Wi-Fi password


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

MQTT_CLIENT_ID = "16A2-wether-01"
MQTT_BROKER = "mqtt.eclipseprojects.org"
MQTT_TOPIC = b"16A2-demo/temp"

def connect_mqtt():
    try:
        client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port = 1883)
        client.connect()
        print("Connected to MQTT broker", MQTT_BROKER)
        return client
    except Exception as e:
        print("Failed to connect to MQTT broker:", e)
        return None

connect_wifi()
client = connect_mqtt()

count = 1

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        payload = json.dumps({
            "temperature": temp,
            "humidity": hum,
            "count": count
        })

        if client:
            client.publish(MQTT_TOPIC, payload)
            print("Published:", payload)
        else:
            print("MQTT client not connected. Cannot publish data.")
        count += 1
    
    except Exception as e:
        print("Error:", e)
    
    time.sleep(3)
