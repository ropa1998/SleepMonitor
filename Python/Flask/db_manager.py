import sqlite3 as lite


def getHistData(numSamples):
    con = lite.connect('../sensorsData.db')
    with con:
        curs = con.cursor()
        curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT " + str(numSamples))
        data = curs.fetchall()
        return data


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


def maxRowsTable():
    con = lite.connect('../sensorsData.db')
    with con:
        curs = con.cursor()
        for row in curs.execute("select COUNT(temp) from  DHT_data"):
            maxNumberRows = row[0]
        return maxNumberRows


# Retrieve LAST data from database
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
