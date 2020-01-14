#!/usr/bin/python
# -*- coding: utf8 -*-
import time
from MySQL import *
from webflask import runningFlask , app
import os,sys, threading, logging
from multiprocessing import Process
from mqttfile import Test
import Queue
from CheckButton import Worker
#import multiprocessing
#from multiprocessing import Process
bien = 0
q  = Queue.Queue(10)
#processQueue = multiprocessing.Queue()
#def Worker(processQueue):
#    while (True):
#        try:
#            work = processQueue.get()
#            print "process " , work
#            time.sleep(1.0)
#        except:
#            pass
class server(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        app.jinja_env.auto_reload = True
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        app.config['debug'] = True
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)


if __name__ == '__main__':
    try:
        load_database()
        FlaskWeb = server()
        FlaskWeb.start()
        mqttClient = Test()
        mqttClient.start()
        p = Process(target=Worker)
        p.start()
        chuydoi=0
        while (1):
            time.sleep(5.0)
    except KeyboardInterrupt:
        print "thoat chuong trinh"
        pass