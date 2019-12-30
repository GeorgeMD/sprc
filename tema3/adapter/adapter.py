import paho.mqtt.client as mqtt
import socket, json, os, influxdb
from datetime import datetime
from dateutil.parser import parse as parse_date
from time import mktime


DEBUG_MODE = "DEBUG_DATA_FLOW" in os.environ


def log(msg=None):
    if DEBUG_MODE:
        if msg is not None:
            print(f"{str(datetime.now())} {msg}")
        else:
            print()


def write_database(entries, timestamp):
    try:
        db_client = influxdb.InfluxDBClient(host="database", username="iot_user", password="unu", database="iot_db")
        db_client.write_points(entries, time_precision='s', protocol='line')
        db_client.close()
        log(f"Wrote entries: {entries}")
    except Exception as e:
        log(f"Exception: {str(e)}")


def on_connect(client, userdata, flags, rc):
    client.subscribe("#")


def parse_message(msg_string, location, station):
    try:
        msg = json.loads(msg_string)
    except json.JSONDecodeError:
        log(f"Can't json.loads: {msg_string}")
        return  
    
    timestamp = None
    entries = []
    for k, v in msg.items():
        if type(v) in [int, float]:
            entries.append(f"{k},location={location},station={station} value={v}")
            log(f"{str(datetime.now())} {location}.{station}.{k} {v}")
        elif k.lower() == "timestamp":
            timestamp = parse_date(str(v))
    
    if timestamp is None:
        timestamp = datetime.now()
        log("Data timestamp is NOW")
    else:
        log(f"Data timestamp is {timestamp}")
    
    timestamp = int(mktime(timestamp.timetuple()))
    entries = [f"{s} {timestamp}" for s in entries]    
    write_database(entries, timestamp)


def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    log(f"Received a message by topic [{msg.topic}]")
    tokens = msg.topic.split('/')
    if len(tokens) < 2:
        return
    location = tokens[0]
    station = tokens[1]
    parse_message(str(msg.payload.decode('utf-8', "ignore")), location, station)
    log()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

connected = False
while not connected:
    try:
        client.connect("broker", 1883, 60)
        connected = True
    except socket.gaierror:
        log("Failed to connect. Retrying.")
        connected = False
        continue

client.loop_forever()