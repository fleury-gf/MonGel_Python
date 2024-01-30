import serial.tools.list_ports
import MonGel_Functions
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


ports = MonGel_Functions.get_ports()
MonGel_port = MonGel_Functions.findMonGel()
MonGel_port = ports[1]



ser = serial.Serial('COM5',baudrate = 115200,timeout=1,exclusive=True)


while True:
    value= ser.readline()
    valueInString=str(value,'UTF-8')
    print(valueInString)