import re
import sqlite3 as lite
import sys

import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
s = [0, 1]


def save_data(read_list):
    con = lite.connect('../sensorsData.db')
    with con:
        cur = con.cursor()
        query = "INSERT INTO DHT_data VALUES(datetime('now')," + read_list[0] + "," + read_list[1] + "," + read_list[
            2] + " )"
        print(query)
        cur.execute(query)


while True:
    read_serial = str(ser.readline().rstrip()).replace("'", "").replace("b", "")
    read_list = read_serial.split(",")
    save_data(read_list)
