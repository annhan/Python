#!/usr/bin/python
# -*- coding: utf8 -*-
import time
from MySQL import *
from webflask import runningFlask , app
import os,sys, threading, logging
import Queue
q  = Queue.Queue(10)
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
            except q.Empty:
                # Handle empty queue here
                pass
            else:
                pass
            if q.qsize() > 0 :
                time.sleep(0.2)
            else:
                time.sleep(5.0)
class Test1(threading.Thread):
    global app
    def __init__(self,q):
        self.q = q
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):

            print("Chay 1")
            time.sleep(0.1)
class Test2(threading.Thread):
    global app
    def __init__(self,q):
        self.q = q
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            print("Chay 2")
            time.sleep(0.1)
class Test3(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            print("Chay 3")
            time.sleep(0.1)
class Test4(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            print("Chay 4")
            time.sleep(0.1)
class Test5(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            print("Chay 5")
            time.sleep(0.1)
class Test6(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            print("Chay 6")
            time.sleep(0.1)
class Test7(threading.Thread):
    global app
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def run(self):
        while (True):
            print("Chay 7")
            time.sleep(0.1)
if __name__ == '__main__':
    load_database()
    FlaskWeb = server()
    FlaskWeb.start()
    Test = Test(q)
    Test.daemon =False #daemon la luong van chay khi ket thuc chuong trinh
    Test.start()

    #Test3 = Test3()
    #Test3.start()
    #Test4 = Test4()
    #Test4.start()
    #Test5 = Test5()
    #Test5.start()
    #Test6 = Test6()
    #Test6.start()
    #Test7 = Test7()
    #Test7.start()
   # Test8 = Test3()
    #Test8.start()

    chuydoi=0
    while (1):
        q.put(chuydoi,0.1)
        chuydoi= chuydoi +1
        print "so lan chuyen ",chuydoi
        time.sleep(1.0)