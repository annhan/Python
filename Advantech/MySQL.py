#!/usr/bin/python
import MySQLdb as mariadb
import Variable
class databaseProject():
    TABLES_CREATE = {}
    TABLES_CREATE['infor_network'] = (
            """CREATE TABLE infor_network(
             ip  CHAR(20) NOT NULL,
             gateway  CHAR(16),
             subnet  CHAR(16),
             wifi_name CHAR(30),  
             wifi_password CHAR(60))""")
    TABLES_CREATE['mqttConf'] = (
            """CREATE TABLE mqttConf(
             serverMQTT  CHAR(32) NOT NULL,
             portMQTT  INT,
             userMQTT  CHAR(16),
             passwordMQTT CHAR(30),  
             TopicSub1 CHAR(60),
             TopicSub2 CHAR(60),
             TopicPub1 CHAR(60),
             TopicPub2 CHAR(60))""")
    TABLES_CREATE['infor_network_wifi'] = (
            """CREATE TABLE infor_network_wifi(
             ip  CHAR(20) NOT NULL,
             gateway  CHAR(16),
             subnet  CHAR(16),
             wifi_name CHAR(30),  
             wifi_password CHAR(60))""")
    TABLES_INSERT = {}
    TABLES_INSERT['infor_network'] = (
            "INSERT INTO infor_network(ip,gateway,subnet,wifi_name,wifi_password) VALUES ('%s','%s','%s','%s','%s')"%(Variable.ip_address, Variable.ip_gateway, Variable.ip_subnet, 'mHomeBH','123789456'))
    TABLES_INSERT['infor_network_wifi'] = (
            "INSERT INTO infor_network_wifi(ip,gateway,subnet,wifi_name,wifi_password) VALUES ('%s','%s','%s','%s','%s')"%(Variable.wifi_ip_address, Variable.wifi_ip_gateway, Variable.ip_subnet, 'mHomeBH','123789456'))
    TABLES_INSERT['mqttConf'] = (
            "INSERT INTO mqttConf(serverMQTT,portMQTT,userMQTT,passwordMQTT,TopicSub1,TopicSub2,TopicPub1,TopicPub2) VALUES ('%s','%d','%s','%s','%s','%s','%s','%s')"%(Variable.mqttServer, Variable.mqttPort, Variable.mqttUser, Variable.mqttPass ,'x','x','x','x'))
    #show table;
    def load_database():
        db = mariadb.connect("localhost", "root", "root", "advantechConf")
        cursor = db.cursor()
        for name, ddl in TABLES_CREATE.iteritems():
            print(name)
            try:
                #print("Creating table {}: ".format(name))
                # print(ddl)
                cursor.execute(ddl)
                db.commit()
                #print(ddl)
                #print("target 1 {}: ".format(name))
                cursor.execute(TABLES_INSERT[name])
                db.commit()
                print("Creating donw table {}: ".format(name))
            except :
                db.rollback()
                sql = "SELECT * FROM {}".format(name)
                cursor.execute(sql)
                results = cursor.fetchall()
                variable_loadata=0
                for row in results:
                    if name=="Serial_Raspberry":
                        ma_serial = row[0]
                        print ("Ma serial ",ma_serial)
                    elif name=="infor_network_wifi":
                        Variable.wifi_ip_address, Variable.wifi_ip_gateway, Variable.ssid, Variable.wpa_password = row[0], row[1], row[3], row[4]
                        print (" WIFI " ,Variable.wifi_ip_address, Variable.wifi_ip_gateway, Variable.ssid, Variable.wpa_password)
                    elif name == "infor_network":
                        Variable.ip_address,Variable.ip_gateway,Variable.ip_subnet = row[0], row[1],  row[2]
                        print (" WIRE ", Variable.ip_address,Variable.ip_gateway,Variable.ip_subnet)
                    elif name=="mqttConf":
                        Variable.mqttServer,Variable.mqttPort,Variable.mqttUser,Variable.mqttPass,Variable.mqttTopicSub1,Variable.mqttTopicSub2,Variable.mqttTopicPub1,Variable.mqttTopicPub2=row[0],int(row[1]),row[2],row[3],row[4],row[5],row[6],row[7]
                        print (" MQTT ", Variable.mqttServer,Variable.mqttPort,Variable.mqttUser,Variable.mqttPass,Variable.mqttTopicSub1,Variable.mqttTopicSub2,Variable.mqttTopicPub1,Variable.mqttTopicPub2)
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
                print ("already exists.")
                db.rollback()
        db.close()
    def update_database(table):
        db = mariadb.connect("localhost", "root", "root", "advantechConf")
        cursor = db.cursor()
        #try:
        print(table)
        cursor.execute("SET SQL_SAFE_UPDATES = 0")
        cursor.execute(table)
        cursor.execute("SET SQL_SAFE_UPDATES = 1")
        db.commit()
        print(table)
        #except:
        #    print("already exists.")
        #    db.rollback()
        db.close()
def main():
    print ("chay wweb")
    databaseProject.update_database()
if __name__ == '__main__':
    main()