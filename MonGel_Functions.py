import serial.tools.list_ports

def get_ports ():
    ports = serial.tools.list_ports.comports()
    return ports

def findMonGel ():
    ports = serial.tools.list_ports.comports() #array with port list
    commPort = 'None'
    numConnection = len(ports)
    for i in range(0,numConnection):
        port = ports[i]
        strPort = str(port)

        if 'Bluetooth' in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
            print(splitPort)
    
    return commPort