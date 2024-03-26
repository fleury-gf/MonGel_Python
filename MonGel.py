import serial.tools.list_ports
import MonGel_Functions
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys


commPort = MonGel_Functions.connectBluetooth()
print(commPort)
ser = serial.Serial(commPort,baudrate = 115200,timeout=1,exclusive=True)





while True:
    value= ser.readline()
    valueInString=str(value,'UTF-8')
    print(valueInString)
    ser.write("OLA\r\n".encode())