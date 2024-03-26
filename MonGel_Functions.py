import serial.tools.list_ports
from time import sleep

def get_ports ():
    ports = serial.tools.list_ports.comports()
    return ports

def connectUART ():
    ports = serial.tools.list_ports.comports() #array with port list
    commPort = 'None'
    numConnection = len(ports)
    for i in range(0,numConnection):
        port = ports[i]
        strPort = str(port)

        if "MSP Application UART1" in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
            ser = serial.Serial(commPort,baudrate = 115200,timeout=1,exclusive=True)
            ser.write("!\r\n".encode())
            sleep(0.005)
            response = ser.readline()
            if response == "\r\nUART\r\n":
                return commPort


    
    return commPort


def connectBluetooth ():
    ports = serial.tools.list_ports.comports() #array with port list
    commPort = 'None'
    numConnection = len(ports)
    for i in range(0,numConnection):
        port = ports[i]
        strPort = str(port)

        if 'Bluetooth' in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
            ser = serial.Serial(commPort,baudrate = 115200,timeout=1,exclusive=True)
            ser.write("!\r\n".encode())
            while True:
                response = ser.readline()
                responseString = str(response,'UTF-8')
                print(responseString)
                if responseString == "BLUE\r\n":
                    return commPort


    
    return commPort