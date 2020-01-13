import time
import threading
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json

def on_connect(client, userdata, flags, rc):
    if (rc == 0):
        print("connection successful broker linked")
    elif (rc == 1):
        print("connection refused -  incorrect protocol version")
    elif (rc == 2):
        print("connection refused - invalid client identifier")
    elif (rc == 3):
        print("connection refused- server unavailable")
    elif (rc == 4):
        print("connection refused- bad username or password")
    elif (rc == 5):
        print("connection refused- not authorised")
    else:
        print("currently unused")
    try:
        client.subscribe("Advantech/+/data")
    except:
        print ("loi subrice")
i = 0
# Advantech/MAC_of_WISE/Device_Status
# subscribe Advantech/00D0C9E27D59E/data {"s":8,"t":"2020-01-13T06:56:09Z","q":192,"c":0,"di1":false,"di2":false,"di3":false,"di4":false,"di5":false,"di6":false,"di7":false,"di8":false}
# publish   Advantech/00D0C9E27959/ctl/do1 {"v":true} / {"v":false}
def on_message(client, userdata, msg):
    global i
    bien="00D0C9E27959"
    print(msg.topic+" "+str(msg.payload))
    y = json.loads(msg.payload)
    print (y["di1"] )
    if (y["di1"] == False):
        print "Fals roi"
        infot = client.publish("Advantech/%s/ctl/do1"%(bien), '{"v":true}')
        infot.wait_for_publish()
    else:
        print "OK ROI"
        try:
            infot = client.publish("Advantech/%s/ctl/do1"%(bien), '{"v":false}')
        except :
            print ("loi send")
client = mqtt.Client("local")
client.username_pw_set("mhome", password="Chotronniemvui1")
client.on_connect = on_connect
client.on_message = on_message
print("EE")
#client.subscrizbe("/Test")
client.connect("localhost", 1883, 60)

client.publish("/Test","ddddddddddddd")
print("end")

class Test(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            client.loop_forever()
        print("a")
