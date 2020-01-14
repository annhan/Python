import time
import threading
import paho.mqtt.client as mqtt
import json
import datetime
import re
import logging
class MVCModel:
    def getTopicPub(self,data):
        return "Advantech/%s/ctl/do1" % (data)
    def getTopicSub(self):
        return "Advantech/+/data"
    def getTopicSub1(self):
        return "Advantech/+/Device_Status"
class MVCPrint:
    def show(self,data):
        print (data)
class MyMQTTClass:
    def __init__(self, clientid=None):
        self._mqttc = mqtt.Client()
        self._mqttc.on_message = self.on_message
        self._mqttc.on_connect = self.on_connect
        self._mqttc.on_publish = self.on_publish
        self._mqttc.on_subscribe = self.on_subscribe
        #self._mqttc.message_callback_add(self.MVCModel.getTopicSub1(), on_message_msgs)
        self.printdata = MVCPrint()
        self.MVCModel = MVCModel()
        self.statusold = 4
        self.listTopic = []
    def on_message_msgs(mosq, obj, msg):
        # This callback will only be called for messages with topics that match
        # $SYS/broker/messages/#
        print("MESSAGES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    def on_connect(self, mqttc, obj, flags, rc):
        if (rc == 0):
            self.printdata.show("connection successful broker linked")
        elif (rc == 2):
            self.printdata.show("connection refused - invalid client identifier")
        elif (rc == 3):
            self.printdata.show("connection refused- server unavailable")
        elif (rc == 4):
            self.printdata.show("connection refused- bad username or password")
        elif (rc == 5):
            self.printdata.show("connection refused- not authorised")
        else:
            self.printdata.show("currently unused")
        try:
            self._mqttc.subscribe(self.MVCModel.getTopicSub())
            self._mqttc.subscribe(self.MVCModel.getTopicSub1())
        except:
            self.printdata.show("loi subrice")

    def on_message(self, mqttc, obj, msg):
        #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        #{"status":"connect","name":"WISE-4012","macid":"00D0C9E27959","ipaddr":"192.168.135.156"}
        bien = "00D0C9E27959"
        if "/Device_Status" in msg.topic:
            print "data ", msg.topic
            try:
                y = json.loads(msg.payload)
                if y["name"] == "WISE-4012":
                    if y["macid"] in self.listTopic:
                        print("giong data")
                        pass
                    else:
                        self.listTopic.append(y["macid"])
                    #print(y["macid"])
            except:
                pass
        elif "/data" in msg.topic:
            bienlocal = re.search('Advantech/(.*)/data', str(msg.topic))
            try:
                y = json.loads(msg.payload)
                if y["di1"] != self.statusold:
                    self.statusold = y["di1"]
                    for x in self.listTopic:
                        if (y["di1"] == False):
                            self.printdata.show("%s - send false to %s" % (datetime.datetime.now(),self.MVCModel.getTopicPub(x)))
                            infot = self._mqttc.publish(self.MVCModel.getTopicPub(x), '{"v":false}', qos = 1)
                        else:
                            self.printdata.show("%s - send true to %s" % (datetime.datetime.now(),self.MVCModel.getTopicPub(x)))
                            infot = self._mqttc.publish(self.MVCModel.getTopicPub(x), '{"v":true}', qos = 1)
            except:
                pass
    def on_publish(self, mqttc, obj, mid):
        pass

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        pass
    def on_log(self, mqttc, obj, level, string):
        pass

    def run(self):
        self._mqttc.username_pw_set("mhome", password="Chotronniemvui1")
        self._mqttc.connect("localhost", 1883, 60)
        rc = 0
        while rc == 0:
            try:
                self._mqttc.loop_forever()
            except:
                pass
# Advantech/MAC_of_WISE/Device_Status
# subscribe Advantech/00D0C9E27D59E/data {"s":8,"t":"2020-01-13T06:56:09Z","q":192,"c":0,"di1":false,"di2":false,"di3":false,"di4":false,"di5":false,"di6":false,"di7":false,"di8":false}
# publish   Advantech/00D0C9E27959/ctl/do1 {"v":true} / {"v":false}
class Test(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while (True):
            try:
                mqttc = MyMQTTClass()
                rc = mqttc.run()
            except:
                time.sleep(1)
