import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe("upb/rpi_1")

def on_message(client, userdata, msg):
    print(msg.topic+": "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker", 1883, 60)

client.loop_start()
while True:
    msg = input()
    client.publish("upb/rpi_1", msg)
