#!/usr/bin/python
# -*- coding: utf8 -*-
import time
from MySQL import *
from webflask import runningFlask , app
import os,sys, threading, logging
import Queue
import multiprocessing
#from multiprocessing import Process
bien = 0
q  = Queue.Queue(10)
processQueue = multiprocessing.Queue()
class Worker(multiprocessing.Process):
    def __init__(self,processQueue):
        self.q=processQueue
        multiprocessing.Process.__init__(self)
        print("process init")
    def run(self):
        global bien
        while (True):
            print "running"
            try:
                work = self.q.get(timeout=0.01)
                print("Process ", work)
            except Queue.Empty :
                # Handle empty queue here
                pass
            else:
                pass
            if q.qsize() > 0 :
                time.sleep(2.0)
            else:
                time.sleep(2.0)

class server(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        app.jinja_env.auto_reload = True
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        app.config['debug'] = True
        # app.run(host='0.0.0.0',port=8080,debug=True,use_reloader=False)
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
class Test(threading.Thread):
    global app
    def __init__(self,q):
        self.q = q
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            try:
                work = self.q.get(timeout=0.01)
                print("chay tum ", work)
            except Queue.Empty :
                # Handle empty queue here
                pass
            else:
                pass
            if q.qsize() > 0 :
                time.sleep(2.0)
            else:
                time.sleep(2.0)
class Test1(threading.Thread):
    global app
    def __init__(self,q):
        self.q = q
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            print("S")
            time.sleep(2.0)
if __name__ == '__main__':
    try:
        global bien
        load_database()
        FlaskWeb = server()
        FlaskWeb.start()
        #Test = Test(q)
        #Test.daemon =False #daemon la luong van chay khi ket thuc chuong trinh
        #Test.start()
        #Test3 = Test1(q)
        #Test3.start()
        p = Worker(q)
        p.start()
        chuydoi=0
        while (1):
            q.put(bien,0.1)
            processQueue.put(bien,timeout=0.1)
            bien= bien +1
            print "so lan chuyen ",bien
            time.sleep(5.0)
    except KeyboardInterrupt:
        print "thoat chuong trinh"
        pass