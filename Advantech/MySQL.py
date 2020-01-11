import MySQLdb as mariadb
#from mainAdvantech import ip_gateway, ip_address, ip_subnet, wifi_ip_gateway, wifi_ip_address, ssid, wpa_password

#global ip_gateway, ip_address, ip_subnet, wifi_ip_gateway, wifi_ip_address
#global ssid, wpa_password
#global ip_gateway
#global ip_address
#global ip_subnet, wifi_ip_gateway, wifi_ip_address
#global ssid, wpa_password
############
## Bien cho Wifi
##################
ssid=""
wpa_password=""
wifi_ip_address="192.168.65.130"
wifi_ip_gateway="192.168.99.1"
infor_wifi_found=""
############
## Bien cho Wire NEtword
##################
ip_address="192.168.99.130"
ip_subnet="255.255.255.0"
ip_gateway="192.168.99.1"
TABLES_CREATE = {}
TABLES_CREATE['infor_network'] = (
        """CREATE TABLE infor_network(
         ip  CHAR(20) NOT NULL,
         gateway  CHAR(16),
         subnet  CHAR(16),
         wifi_name CHAR(30),  
         wifi_password CHAR(60))""")
TABLES_CREATE['infor_network_wifi'] = (
        """CREATE TABLE infor_network_wifi(
         ip  CHAR(20) NOT NULL,
         gateway  CHAR(16),
         subnet  CHAR(16),
         wifi_name CHAR(30),  
         wifi_password CHAR(60))""")
TABLES_INSERT = {}
TABLES_INSERT['infor_network'] = (
        "INSERT INTO infor_network(ip,gateway,subnet,wifi_name,wifi_password) VALUES ('%s','%s','%s','%s','%s')"%(ip_address, ip_gateway, ip_subnet, 'mHomeBH','123789456'))
TABLES_INSERT['infor_network_wifi'] = (
        "INSERT INTO infor_network_wifi(ip,gateway,subnet,wifi_name,wifi_password) VALUES ('%s','%s','%s','%s','%s')"%(wifi_ip_address, wifi_ip_gateway, ip_subnet, 'mHomeBH','123789456'))

def load_database():
    global wifi_ip_gateway,wifi_ip_address,ssid,wpa_password
    global ip_gateway,ip_address,ip_subnet
    db = mariadb.connect("localhost", "root", "root", "advantechConf")
    cursor = db.cursor()
    for name, ddl in TABLES_CREATE.iteritems():
        print(name)
        try:
            cursor.execute(ddl)
            db.commit()
            cursor.execute(TABLES_INSERT[name])
            db.commit()
            print("Creating table {}: ".format(name))
        except :
            db.rollback()
            sql = "SELECT * FROM {}".format(name)
            cursor.execute(sql)
            results = cursor.fetchall()
            variable_loadata=0
            for row in results:
                if name=="Serial_Raspberry":
                    ma_serial = row[0]
                    print "Ma serial ",ma_serial
                elif name=="infor_network_wifi":
                    wifi_ip_address, wifi_ip_gateway, ssid, wpa_password = row[0], row[1], row[3], row[4]
                    print " WIFI " ,wifi_ip_address, wifi_ip_gateway, ssid, wpa_password
                elif name=="infor_network":
                    ip_address,ip_subnet,ip_gateway=row[0],row[2],row[1]
                    print " IP ", ip_address, ip_subnet, ip_gateway
                variable_loadata=variable_loadata+1
            if variable_loadata==0:
                print("Inser table {}: ".format(name))
                cursor.execute(TABLES_INSERT[name])
                db.commit()
        db.commit()
    db.close()
def delete_db():
    db = mariadb.connect("localhost","root", "root", "advantechConf")
    cursor = db.cursor()
    for name, ddl in TABLES_CREATE.iteritems():
        try:
            print("Delete table {}: ".format(name))
            sql = "DROP TABLE {};".format(name)
            cursor.execute(sql)
            db.commit()
        except:
            print "already exists."
            db.rollback()
    db.close()
def update_database(table):
    db = mariadb.connect("localhost", "root", "root", "advantechConf")
    cursor = db.cursor()
    try:
        print(table)
        cursor.execute("SET SQL_SAFE_UPDATES = 0")
        cursor.execute(table)
        cursor.execute("SET SQL_SAFE_UPDATES = 1")
        db.commit()
        print(table)
    except:
        print("already exists.")
        db.rollback()
    db.close()