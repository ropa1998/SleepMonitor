from flask import Flask, render_template, request

app = Flask(__name__)

import sqlite3


# Retrieve data from database
def getData():
    conn = sqlite3.connect('../sensorsData.db')
    curs = conn.cursor()

    for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
        time = str(row[0])
        temp = row[1]
        hum = row[2]
    conn.close()
    return time, temp, hum


# main route
@app.route("/")
def getPage():
    time, temp, hum = getData()
    templateData = {
        'time': time,
        'temp': temp,
        'hum': hum
    }
    return render_template('index.html', **templateData)


if __name__ == '__main__':
    app.run(debug=True)
