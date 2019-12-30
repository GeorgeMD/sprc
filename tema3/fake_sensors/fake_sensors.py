import paho.mqtt.client as mqtt
import random, socket, json
from datetime import datetime
from time import mktime, sleep

random.seed(mktime(datetime.now().timetuple()))

topics = ["upb/rpi_1", "upb/rpi_2", "gigel/ard_a", "gigel/ard_b"]

message_template = {
    topics[0]: ["TMP", "BAT", "HUMID"], 
    topics[1]: ["RSSI", "AQI"],
    topics[2]: ["Light", "Voltage"],
    topics[3]: ["BAT", "TMP"]
}

def on_connect(client, userdata, flags, rc):
    print("Connected!")

client = mqtt.Client()
client.on_connect = on_connect

while True:
    try:
        client.connect("broker", 1883, 60)
    except socket.gaierror:
        print("Failed to connect")
        continue
    break

client.loop_start()

while True:
    for topic in topics:
        msg = {}
        for key in message_template[topic]:
            msg[key] = random.random() * 100
        if random.randint(0, 1) == 1:
            msg['timestamp'] = str(datetime.now())
        if random.randint(0, 1) == 1:
            msg["str"] = "top kek"
        
        client.publish(topic, json.dumps(msg))
        print(f"Sent {str(msg)} to {topic}")
    sleep(0.2)

client.loop_stop()