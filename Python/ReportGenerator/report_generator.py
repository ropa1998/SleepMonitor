import sqlite3 as lite
from datetime import datetime


def generate_report(from_datetime: datetime, to_datetime: datetime):
    con = lite.connect('../sensorsData.db')
    with con:
        cur = con.cursor()
        query = "SELECT * FROM DHT_data WHERE timestamp BETWEEN '" + from_datetime.strftime(
            "%Y-%m-%d %H:%M:%S") + "' AND '" + to_datetime.strftime(
            "%Y-%m-%d %H:%M:%S") + "'"
        print(query)
        values = cur.execute(query)
        for elem in values:
            time = str(elem[0])
            temp = str(elem[1])
            hum = str(elem[2])
            light = str(elem[3])
            print(time + temp + hum + light)


x = datetime(2019, 10, 12, 10, 00, 00)
y = datetime(2019, 10, 12, 15, 00, 00)

generate_report(x, y)
