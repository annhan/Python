import RPi.GPIO as GPIO
import time
import os
import threading



class button(threading.Thread):
    length = 0
    def __init__(self):
        threading.Thread.__init__(self)
        print("Serveer init")
    def changeIP(self):
        print ("Change IP")
        os.system('sudo ifconfig eth0 down')
        os.system('sudo ifconfig eth0 192.168.135.10')
        os.system('sudo ifconfig eth0 up')
    def run(self):
        pin = 21
        GPIO.setmode(GPIO.BCM)  # set up BCM GPIO numbering
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        while (True):
            try:
                if GPIO.input(pin) == GPIO.LOW:
                    start = time.time()
                    time.sleep(0.2)
                    while GPIO.input(pin) == GPIO.LOW:
                        time.sleep(0.01)
                    self.length = time.time() - start
                    print("time press ", self.length)
                if self.length > 3:
                    self.length = 0
                    changeIP()
                time.sleep(1)
            except:
                pass
                time.sleep(0.2)
        GPIO.cleanup()  # clean up after yourself
