## @package create_database
#  This module takes care of creating the database that the whole project will use.
#
# It automatically creates, at this file system level, a file called 'sensorsData.db' that works as the database for
# the project (we are using SQLite3).
# This has two tables: sensors_data (datetime, temperature, humidity and light) and sleeping_ranges (email, initial, end).

import sqlite3 as lite
import sys

con = lite.connect('sensorsData.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS DHT_data")
    cur.execute("DROP TABLE IF EXISTS sleeping_ranges")
    cur.execute("DROP TABLE IF EXISTS sensors_data")
    cur.execute("CREATE TABLE sensors_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC, light NUMERIC)")
    cur.execute("CREATE TABLE sleeping_ranges(mail VARCHAR(255), initial DATETIME, end DATETIME)")
