import serial.tools.list_ports

# Get name ex: COM3 or COM5
for i in serial.tools.list_ports.comports():
    print(str(i).split(" ")[0])
# get name và detail    
for i in serial.tools.list_ports.comports():
    print(i) 