#!/usr/bin/python
# This shows a simple example of an MQTT subscriber.
import sys
try:
    import paho.mqtt.client as mqtt
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    #
    # If you have the module installed, just use "import paho.mqtt.client"
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.client as mqtt
def on_connect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))
def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
def on_log(mqttc, obj, level, string):
    print(string)
# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
#mqttc.on_log = on_log
mqttc.connect("127.0.0.1", 1883, 60)
mqttc.subscribe("news", 0)
mqttc.loop_forever()