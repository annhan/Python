import RPi.GPIO as GPIO
from time import sleep  # this lets us have a time delay (see line 15)
import os

def Worker(self):
    def changeIP():
        print"Change IP"
        os.system('sudo ifconfig eth0 down')
        os.system('sudo ifconfig eth0 192.168.135.10')
        os.system('sudo ifconfig eth0 up')

    print " Button"
    pin = 21
    GPIO.setmode(GPIO.BCM)  # set up BCM GPIO numbering
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while (True):
        try:
            if  GPIO.input(pin) == GPIO.HIGH:
                print "LOWWWWWW"
                start = time.time()
                print (start)
                time.sleep(0.2)
                while GPIO.input(pin) == GPIO.LOW:
                    time.sleep(0.01)
                length = time.time() - start
                print "chieu dai ",self.length
            if self.length > 3:
                self.length = 0
                changeIP()
            time.sleep(1)
        except:
            pass
    GPIO.cleanup()  # clean up after yourself