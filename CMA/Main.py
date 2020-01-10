# -*- coding: utf8 -*-
from wifi import Cell, Scheme
from time import time
import time
from os.path import dirname, join
import socket               # Import socket module
import os,sys, threading, logging
import minimalmodbus
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL=True

def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"
    return cpuserial
########################################
####################################
if __name__ == '__main__':
    with open('Daikin.log', 'w'):
        pass
    logging.basicConfig(filename='Daikin.log', level=logging.DEBUG)
    logging.debug('Daikin begin')
    bien = serial_ports()
    while bien=="NO":
        bien = serial_ports()
    #delete_db()
    load_database()
    so_serial=getserial()
    mahoa1=hashlib.md5(so_serial).hexdigest()
    mahoa2=hashlib.md5(mahoa1).hexdigest()
    logging.debug('Daikin begin')
    infor_wifi_found=ssid_discovered()
    #print "NHAN",mahoa2
    #print(so_serial,ma_serial)
    #print(len(str(mahoa2)),len(str(ma_serial)))
    if str(ma_serial) == str(mahoa2):
        #print("dung serial")
        TCP_HC21 = modbus(serial_ports(),modbus_address,modbus_boudrate,modbus_timeout)
        TCP_HC21.start()
    else:
        #print("Sai Serial")
        TCP_HC21 = modbus(serial_ports(),123,9600,modbus_timeout)
        TCP_HC21.start()
        dungmaserial=1
    TCP_HC2 = server()
    TCP_HC2.start()
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0',port=8080,debug=True,use_reloader=False)