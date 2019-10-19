import sqlite3 as lite
import sys

con = lite.connect('sensorsData.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS DHT_data")
    cur.execute("CREATE TABLE sensors_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC, light NUMERIC)")
    cur.execute("CREATE TABLE sleeping_ranges(initial DATETIME, end DATETIME)")
