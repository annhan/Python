
# Install nodejs on Raspberry

```  
wget http://nodejs.org/dist/latest/node-v14.9.0-linux-armv7l.tar.xz

tar -xvf node-v14.9.0-linux-armv7l.tar.xz

cd node-v14.9.0-linux-armv7l

sudo cp -R * /usr/local/
```

```node -v ``` check for install success


# install mosca

```sudo npm install mosca bunyan -g``` - Library for MQTT server

```npm install mqtt``` - Lib for mqtt client


# Cài đặt MQTT Server sử dụng Mosca NodeJS

Cài đặt các thư viện
Mosca là thư viện để tạo MQTT server

https://github.com/mcollina/mosca
https://www.npmjs.com/package/mosca

```
mkdir nodeapp
nano server.js
```

và pase đoạn code này vào

```js
var mosca = require('mosca');
var settings = {
		port : 18833
		}

var server = new mosca.Server(settings);

// fired client is connected
server.on('clientConnected', function(client) {
    console.log('Client connected', client.id);
});

// fired when a message is received
server.on('published', function(packet, client) {
    console.log('Message Received ', packet.payload);
  });

  server.on('ready', setup);

  // fired when the mqtt server is ready
function setup() {
    console.log('Mosca MQTT server is up and running at ' + settings.port);
}
  ```
```npm run server```

  - Vì sao chọn Mosca thay vì dung mosquitto : là mosca có thể được nhúng dễ dàng trong file js khác, từ đó ta có thể tùy biến data trực tiếp trên broker.

# Chạy nodeJs trong nền

- install PM2  ```sudo npm install -g pm2```

- ```pm2 start app.js``` để chạy app

- pm2 sẽ tự chạy lại app nếu app bị lỗi.

# Run PM2 at startup

- ```pm2 startup systemd``` đánh lệnh này thì pm2 sẽ in ra

```
[PM2] Init System found: systemd
[PM2] To setup the Startup Script, copy/paste the following command:
sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u pi --hp /home/pi
```

sau đó ta copy dòng lệnh và pase vào terminal

```sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u pi --hp /home/pi```

Thao tác này sẽ giúp pm2 chạy khi khởi động, pm2 sẽ load lại dump file đã chạy trước đó.
Để tạo file này ta command ```pm2 save``` trong khi server đang chạy.

```pm2 save``` sẽ lưu trạng thái hiện tại của pm2 (với app server đang chạy của chúng ta) và sẽ khởi động lại sau khi reboot.

# PM2 daemon

- ```pm2 list```
- ```pm2 status```
- ```pm2 show```
- pm2 restart app_name
- pm2 reload app_name
- pm2 stop app_name
- pm2 delete app_name
