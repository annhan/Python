import RPi.GPIO as GPIO
from time import sleep  # this lets us have a time delay (see line 15)
import os
def changeIP():
    print "Change IP"
    os.system('sudo ifconfig eth0 down')
    os.system('sudo ifconfig eth0 192.168.1.10')
    os.system('sudo ifconfig eth0 up')
def buttonCall(*args):
    if GPIO.input(21) == GPIO.LOW:
        print "Button nhan"
        changeIP()
GPIO.setmode(GPIO.BCM)  # set up BCM GPIO numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#cb = ButtonHandler(21, real_cb, edge='rising', bouncetime=100)
##GPIO.add_event_detect(21, GPIO.RISING, callback=cb)
GPIO.add_event_detect(21, GPIO.RISING, callback=buttonCall, bouncetime=500)
try:
    while True:  # this will carry on until you hit CTRL+C
        sleep(1)  # wait 0.1 seconds
finally:  # this block will run no matter how the try block exits
    GPIO.cleanup()  # clean up after yourself

