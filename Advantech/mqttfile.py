import time
import threading
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json
class MyMQTTClass(mqtt.Client):
    def on_connect(self, mqttc, obj, flags, rc):
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
            self.subscribe("Advantech/+/data")
        except:
            print("loi subrice")

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        global i
        bien = "00D0C9E27959"
        print(msg.topic + " " + str(msg.payload))
        y = json.loads(msg.payload)
        print(y["di1"])
        if (y["di1"] == False):
            print "Fals roi"
            infot = self.publish("Advantech/%s/ctl/do1" % (bien), '{"v":true}')
            infot.wait_for_publish()
        else:
            print "OK ROI"
            try:
                infot = self.publish("Advantech/%s/ctl/do1" % (bien), '{"v":false}')
            except:
                print("loi send")
    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        self.username_pw_set("mhome", password="Chotronniemvui1")
        self.connect("localhost", 1883, 60)
        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc


# Advantech/MAC_of_WISE/Device_Status
# subscribe Advantech/00D0C9E27D59E/data {"s":8,"t":"2020-01-13T06:56:09Z","q":192,"c":0,"di1":false,"di2":false,"di3":false,"di4":false,"di5":false,"di6":false,"di7":false,"di8":false}
# publish   Advantech/00D0C9E27959/ctl/do1 {"v":true} / {"v":false}
class Test(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            try:
                mqttc = MyMQTTClass()
                rc = mqttc.run()
                #client.loop_forever()
            except:
                print("fail")
                time.sleep(1)
