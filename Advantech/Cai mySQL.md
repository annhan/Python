------------------------------
Install mySQL
---------------------------------
```
sudo apt-get install python-pip python-dev libmysqlclient-dev
sudo apt-get install python-mysqldb
sudo apt-get install mysql-server python-mysqldb
sudo apt install mariadb-server
pip install mysql-connector 
mysql -u root -p
```

-----------------------------------------------------------------------------
My SQL Database Python 
--------------------
```
sudo /etc/init.d/mysql stop
sudo /etc/init.d/mysql start
```


1.Login

sudo mysql -u root -p

password: root

2. Create Database:
create database WifiSetting;
3. Show database:
show databases;

Trang huong dan database:
http://thuthuatvietnam.com/tao-database-va-user-mysql-bang-lenh-terminal.html


-----------------------
WifiSetting
---------------------
Cai Wifi
Vao /etc/wpa_supplicant/wpa_supplicant.conf
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="scc"
scan_ssid=1
psk="ss"
}
```


-----------------
 File Static IP:
-----------------------------
 sudo nano /etc/dhcpcd.conf

add them dong cuoi cung
```
nohook lookup-hostname
```
---------
threading  và process
------------

Khác biệt process ứng dụng cho nhiều core, bộ nhớ không liên thông nên không dùng chung bộ nhớ với process khác. Phaoir đung queue của multiprocess
