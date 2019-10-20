## @package create_database
#  This module takes care of creating the database that the whole project will use.
#
# It automatically creates, at this level, a file called sensorsData.db.with all the information that the running
# project will create.

import sqlite3 as lite
import sys

con = lite.connect('sensorsData.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS DHT_data")
    cur.execute("CREATE TABLE sensors_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC, light NUMERIC)")
    cur.execute("CREATE TABLE sleeping_ranges(mail VARCHAR(255), initial DATETIME, end DATETIME)")
