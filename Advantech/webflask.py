# -*- coding: utf8 -*-

from os.path import dirname, join
from flask import Flask, render_template
from flask import request
from MySQL import *

##################3
## Ham SET STATIC IP CHO PI
############################
def write_netword():
    #global ip_address, ip_gateway, ip_subnet, wifi_ip_gateway, wifi_ip_address
    f = open("/etc/dhcpcd.conf", "r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if "nohook lookup-hostname" in i:
            f.write(i)
            break
        else:
            f.write(i)
    f.write("\n")
    f.write("interface eth0\n")
    f.write("\n")
    f.write("static ip_address={}/24\n".format(Variable.ip_address))
    f.write("static routers={}\n".format(Variable.ip_gateway))
    f.write("static domain_nam_servers=8.8.8.8\n")
    f.write("\n")
    f.write("interface wlan0\n")
    f.write("\r\n")
    f.write("static ip_address={}/24\n".format(Variable.wifi_ip_address))
    f.write("static routers={}\n".format(Variable.wifi_ip_gateway))
    f.write("static domain_nam_servers=8.8.8.8\n")
    f.truncate()
    f.close()
###########################
## Ham lưu Wifi cho raspberry kết nối
#############################
def write_wifi():
    f = open("/etc/wpa_supplicant/wpa_supplicant.conf", "r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if "network={" in i:
            f.write(i)
            break
        else:
            f.write(i)
    f.write("ssid=\"{}\"\n".format(Variable.ssid))
    f.write("scan_ssid=1\n")
    f.write("psk=\"{}\"\n".format(Variable.wpa_password))
    f.write("}\r\n")
    f.truncate()
    f.close()
app = Flask(__name__)
@app.route('/')
def trang_chu():
    return render_template('index.html')
@app.route('/setip', methods=['POST', 'GET'])
def set_ip():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            return ("JSON Message:  Not Accept") #" + json.dumps(request.json + "
        Variable.ip_address_new,Variable.ip_subnet_new,Variable.ip_gateway_new=request.form['html_ip'],request.form['html_subnet'],request.form['html_gateway']
        if len(ip_address_new) < 7:
            print("Khong gia tri IP")
            return "Dia chi IP ngan"
        elif len(ip_gateway_new) < 7:
            print ("Khong gia tri Gateway")
            return "Dia chi gateway ngan"
        elif ip_address_new==wifi_ip_address:
            print("Trung Ip voi mnag Wifi")
            return "Error IP trung voi mang VLAN"
        else:
            Variable.ip_address,Variable.ip_subnet,Variable.ip_gateway=ip_address_new,ip_subnet_new,ip_gateway_new
            MySQL.update_database("UPDATE infor_network SET ip='{}',gateway= '{}',subnet= '{}'".format(Variable.ip_address,Variable.ip_gateway,Variable.ip_subnet))
            write_netword()
        #os.system('sudo ifconfig eth0 down')
        #os.system('sudo ifconfig eth0 {}'.format(ip_address))
        #os.system('sudo ifconfig eth0 up')

            return "OK"
    else:
        return render_template('set_ip.html', ip=Variable.ip_address,gateway=Variable.ip_gateway,subnet=Variable.ip_subnet)
@app.route('/setmaso', methods=['POST', 'GET'])
def set_maso():
    global so_serial,ma_serial
    if request.method == 'POST':
        ma_tam = request.form['html_code']
        if len(ma_tam) < 20:
            print("Sai ma")
            return "NOT OK"
        else:
            ma_serial = ma_tam
            update_database("UPDATE Serial_Raspberry SET So_Serial='{}'".format(ma_serial))
            return "OK"
    else:
        return render_template('set_maso.html', uuid=so_serial,macode=ma_serial)
@app.route('/setwifi', methods=['POST', 'GET'])
def set_wifi():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            return ("JSON Message:  Not Accept") #" + json.dumps(request.json + "
        ssid_new,wpa_password_new,wifi_ip_address_new,wifi_ip_gateway_new=request.form['html_ssid'],request.form['html_wpa_password'],request.form['html_ip_wifi'],request.form['html_gateway_wifi']
        if wifi_ip_address_new==Variable.ip_address:
            print ("Dia chi trung IP voi Wire")
            return "Error IP trung voi mmang LAN"
        else:
            Variable.ssid,Variable.wpa_password,Variable.wifi_ip_address,Variable.wifi_ip_gateway=ssid_new,wpa_password_new,wifi_ip_address_new,wifi_ip_gateway_new
            update_database("UPDATE infor_network_wifi SET wifi_name='{}',wifi_password='{}',ip='{}',gateway= '{}'".format(Variable.ssid,Variable.wpa_password,Variable.wifi_ip_address,Variable.wifi_ip_gateway))
            write_netword()
            write_wifi()
            #os.system('sudo ifconfig eth0 down')
            #os.system('sudo ifconfig eth0 {}'.format(ip_address))
            #os.system('sudo ifconfig eth0 up')
            return "OK"
    else:
        return render_template('set_wifi.html', ssid=Variable.ssid,wpa_pass=Variable.wpa_password,ip_wifi=Variable.wifi_ip_address,gateway_wifi=Variable.wifi_ip_gateway,infor_wifi_found=Variable.infor_wifi_found)
def runningFlask():
    print "chay wweb"
    #app.jinja_env.auto_reload = True
    #app.config['TEMPLATES_AUTO_RELOAD'] = True
    #app.run(host='0.0.0.0',port=8080,debug=True,use_reloader=False)