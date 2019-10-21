import sqlite3 as lite
from datetime import datetime


## @package db_manager
#  This module takes care of all the interactions with the database for the program

## This method takes an int 'n' and returns the last 'n' tuples in sensors_data.
#  @param numSamples The 'n' last sensors entries.
def getHistData(numSamples):
    con = lite.connect('../sensorsData.db')
    with con:
        curs = con.cursor()
        curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT " + str(numSamples))
        data = curs.fetchall()
        return data


## This method takes a list of tuples representing the 'sensors_data' tuples and returns a 4-uple with a list for each variable.
#  @param data A list of 'sensors_data' tuples.
def getDataAsTuple(data):
    dates = []
    temps = []
    hums = []
    lights = []
    for row in reversed(data):
        dates.append(row[0])
        temps.append(row[1])
        hums.append(row[2])
        lights.append(row[3])
    return dates, temps, hums, lights


## This method returns the number of tuples in the table of 'sensors_data'.
def maxRowsTable():
    con = lite.connect('../sensorsData.db')
    with con:
        curs = con.cursor()
        for row in curs.execute("select COUNT(temp) from  DHT_data"):
            maxNumberRows = row[0]
        return maxNumberRows


## This method returns the last tuples in the table of'sensors_data'.
def getLastData():
    con = lite.connect('../sensorsData.db')
    with con:
        curs = con.cursor()
        for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
            time = str(row[0])
            temp = row[1]
            hum = row[2]
            light = row[3]
    # conn.close()
    return time, temp, hum, light


## This method returns the tuples in the table of'sensors_data' that where generated between 'from_datetime' and 'to_datetime'.
#  @param from_datetime The datetime from which the query will be evaluated.
#  @param to_datetime The datetime to which the query will be evaluated.
def get_report_data(from_datetime: datetime, to_datetime: datetime):
    con = lite.connect('../sensorsData.db')
    with con:
        cur = con.cursor()
        query = "SELECT * FROM DHT_data WHERE timestamp BETWEEN '" + from_datetime.strftime(
            "%Y-%m-%d %H:%M:%S") + "' AND '" + to_datetime.strftime(
            "%Y-%m-%d %H:%M:%S") + "'"
        return cur.execute(query).fetchall()


## This method returns the information of the only tuple in 'sleeping_ranges'.
def get_sleeping_range():
    con = lite.connect('../sensorsData.db')
    with con:
        curs = con.cursor()
        for row in curs.execute("SELECT * FROM sleeping_ranges"):
            email = row[0]
            initial = row[1]
            to = row[2]
            return email, initial, to
    # conn.close()

## This method sets the only row in 'sleeping_ranges' to the values that are passed.
#  @param mail The email for the row.
#  @param date_from The 'from' for the row.
#  @param date_to The 'to' for the row.
def save_sleeping_range(mail, date_from, date_to):
    con = lite.connect('../sensorsData.db')
    with con:
        cur = con.cursor()
        query1 = "DELETE FROM sleeping_ranges"
        query2 = "INSERT INTO sleeping_ranges VALUES (" "\'" + mail + "\'" + "," + "\'" + date_from + "\',\'" + date_to + "\')"
        cur.execute(query1)
        cur.execute(query2)
