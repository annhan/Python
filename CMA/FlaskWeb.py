from flask import Flask, render_template
from flask import request
##################3
## Ham SET STATIC IP CHO PI
############################
def write_netword():
    global ip_address, ip_gateway, ip_subnet, wifi_ip_gateway, wifi_ip_address
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
    f.write("static ip_address={}/24\n".format(ip_address))
    f.write("static routers={}\n".format(ip_gateway))
    f.write("static domain_nam_servers=8.8.8.8\n")
    f.write("\n")
    f.write("interface wlan0\n")
    f.write("\r\n")
    f.write("static ip_address={}/24\n".format(wifi_ip_address))
    f.write("static routers={}\n".format(wifi_ip_gateway))
    f.write("static domain_nam_servers=8.8.8.8\n")
    f.truncate()
    f.close()
###########################
## Ham lưu Wifi cho raspberry kết nối
#############################
def write_wifi():
    global ssid,wpa_password
    f = open("/etc/wpa_supplicant/wpa_supplicant.conf", "r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if "network={" in i:
            f.write(i)
            break
        else:
            f.write(i)
    f.write("ssid=\"{}\"\n".format(ssid))
    f.write("scan_ssid=1\n")
    f.write("psk=\"{}\"\n".format(wpa_password))
    f.write("}\r\n")
    f.truncate()
    f.close()
app = Flask(__name__)
@app.route('/')
def trang_chu():
    return render_template('index.html',global3=Daikin1,name_zone1=Daikin1["Zone1"]["Name"], name_zone2=Daikin1["Zone2"]["Name"], name_zone3=Daikin1["Zone3"]["Name"], name_zone4=Daikin1["Zone4"]["Name"],name_zone5=Daikin1["Zone5"]["Name"],name_zone6=Daikin1["Zone6"]["Name"],name_zone7=Daikin1["Zone7"]["Name"],name_zone8=Daikin1["Zone8"]["Name"],name_zone9=Daikin1["Zone9"]["Name"],name_zone10=Daikin1["Zone10"]["Name"],name_zone11=Daikin1["Zone11"]["Name"],name_zone12=Daikin1["Zone12"]["Name"],name_zone13=Daikin1["Zone13"]["Name"],name_zone14=Daikin1["Zone14"]["Name"],name_zone15=Daikin1["Zone15"]["Name"],name_zone16=Daikin1["Zone16"]["Name"],_Using_zone1=Daikin1["Zone1"]["Using"], _Using_zone2=Daikin1["Zone2"]["Using"], _Using_zone3=Daikin1["Zone3"]["Using"], _Using_zone4=Daikin1["Zone4"]["Using"],_Using_zone5=Daikin1["Zone5"]["Using"],_Using_zone6=Daikin1["Zone6"]["Using"],_Using_zone7=Daikin1["Zone7"]["Using"],_Using_zone8=Daikin1["Zone8"]["Using"],_Using_zone9=Daikin1["Zone9"]["Using"],_Using_zone10=Daikin1["Zone10"]["Using"],_Using_zone11=Daikin1["Zone11"]["Using"],_Using_zone12=Daikin1["Zone12"]["Using"],_Using_zone13=Daikin1["Zone13"]["Using"],_Using_zone14=Daikin1["Zone14"]["Using"],_Using_zone15=Daikin1["Zone15"]["Using"],_Using_zone16=Daikin1["Zone16"]["Using"])

@app.route('/setmodbus', methods=['POST', 'GET'])
def set_modbus():
    global modbus_boudrate,modbus_timeout,modbus_address
    if request.method == 'POST':
        print(modbus_timeout)
        modbus_boudrate=request.form['html_Boudrate']
        modbus_address=request.form['html_slave_address']
        modbus_timeout=request.form['html_timeout']
        print(modbus_timeout)
        update_database("UPDATE Daikin SET mode='{}',boudrate={},slave_address={},timeout={}".format('rtu',modbus_boudrate,modbus_address,modbus_timeout))
        return "OK dsds"
    else:
        return render_template('set_modbus.html')

@app.route('/setwifi', methods=['POST', 'GET'])
def set_wifi():
    global ip_address,ip_gateway,ip_subnet,wpa_password,ssid,wifi_ip_address,wifi_ip_gateway,infor_wifi_found
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            return ("JSON Message:  Not Accept") #" + json.dumps(request.json + "
        ssid_new,wpa_password_new,wifi_ip_address_new,wifi_ip_gateway_new=request.form['html_ssid'],request.form['html_wpa_password'],request.form['html_ip_wifi'],request.form['html_gateway_wifi']
        if wifi_ip_address_new==ip_address:
            print ("Dia chi trung IP voi Wire")
            return "Error IP trung voi mmang LAN"
        else:
            ssid,wpa_password,wifi_ip_address,wifi_ip_gateway=ssid_new,wpa_password_new,wifi_ip_address_new,wifi_ip_gateway_new
            update_database("UPDATE infor_network_wifi SET wifi_name='{}',wifi_password='{}',ip='{}',gateway= '{}'".format(ssid,wpa_password,wifi_ip_address,wifi_ip_gateway))
            write_netword()
            write_wifi()
            #os.system('sudo ifconfig eth0 down')
            #os.system('sudo ifconfig eth0 {}'.format(ip_address))
            #os.system('sudo ifconfig eth0 up')
            return "OK"
    else:
        infor_wifi_found = ssid_discovered()
        return render_template('set_wifi.html', ssid=ssid,wpa_pass=wpa_password,ip_wifi=wifi_ip_address,gateway_wifi=wifi_ip_gateway,infor_wifi_found=infor_wifi_found)

