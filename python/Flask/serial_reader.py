## @package serial_reader
# This module takes care of reading data from the serial port, formatting it and saving it to the database
import sqlite3 as lite
from datetime import datetime
from SleepMonitor.python.Flask.date_parser import STANDARD_FORMAT
import serial


## This method saves the sensors data into the database
# @param read_list An array of values containing the temperature, humidity and light values.


def save_data(read_list):
    con = lite.connect('../sensorsData.db')
    with con:
        cur = con.cursor()
        std_frmt = str(datetime.now().strftime(STANDARD_FORMAT))
        query = "INSERT INTO sensors_data VALUES(\'" + std_frmt + "\'," + read_list[0] + "," + read_list[1] + "," + read_list[
            2] + " )"
        print(query)
        cur.execute(query)


ser = serial.Serial('/dev/ttyUSB1', 9600)

while True:
    read_serial = str(ser.readline().rstrip()).replace("'", "").replace("b", "")
    read_list = read_serial.split(",")
    save_data(read_list)
