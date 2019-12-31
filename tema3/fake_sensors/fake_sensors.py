import paho.mqtt.client as mqtt
import random, socket, json
from datetime import datetime
from time import mktime, sleep

random.seed(mktime(datetime.now().timetuple()))

topics = ["UPB/rpi_1", "UPB/rpi_2", "gigel/ard_a", "gigel/ard_b"]

message_template = {
    topics[0]: [("TMP", (0, 20)), ("BAT", (65, 65)), ("HUMID", (85, 100))],
    topics[1]: [("RSSI", (20, 30)), ("AQI", (70, 80))],
    topics[2]: [("Light", (0, 15)), ("Voltage", (65, 80))],
    topics[3]: [("BAT", (54, 54)), ("TMP", (20, 30))]
}

def on_connect(client, userdata, flags, rc):
    print("Connected!")

client = mqtt.Client()
client.on_connect = on_connect

while True:
    try:
        client.connect("localhost", 1883, 60)
    except socket.gaierror:
        print("Failed to connect")
        continue
    break

client.loop_start()

def generate_random(topic):
    msg = {}
    for key, val in message_template[topic]:
        mini, maxi = val
        msg[key] = mini
        if mini != maxi:
            msg[key] += random.random() * (maxi - mini)
    if random.randint(0, 1) == 1:
        msg['timestamp'] = str(datetime.now())
    if random.randint(0, 1) == 1:
        msg["str"] = "top kek"
    
    client.publish(topic, json.dumps(msg))
    print(f"Sent {str(msg)} to {topic}")

upb_n = 0

while True:
    upb_topic = topics[upb_n]
    gigel_topic = topics[3 - upb_n]
    
    generate_random(upb_topic)
    generate_random(gigel_topic)
    
    upb_n = 1 if upb_n == 0 else 0
    sleep(1)

client.loop_stop()