from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import sqlite3 as lite

from flask import Flask, render_template, send_file, make_response, request

app = Flask(__name__)


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


def getHistData(numSamples):
    con = lite.connect('../sensorsData.db')
    with con:
        curs = con.cursor()
        curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT " + str(numSamples))
        data = curs.fetchall()
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


# initialize global variables
global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
    numSamples = 100


# main route
@app.route("/")
def index():
    time, temp, hum, light = getLastData()
    templateData = {
        'time': time,
        'temp': temp,
        'hum': hum,
        'light': light,
        'numSamples': numSamples
    }
    return render_template('index.html', **templateData)


@app.route('/', methods=['POST'])
def my_form_post():
    global numSamples
    numSamples = int(request.form['numSamples'])
    numMaxSamples = maxRowsTable()
    if (numSamples > numMaxSamples):
        numSamples = (numMaxSamples - 1)

    time, temp, hum, light = getLastData()

    templateData = {
        'time': time,
        'temp': temp,
        'hum': hum,
        'light': light,
        'numSamples': numSamples
    }
    return render_template('index.html', **templateData)


# TODO refactor all plots in one method.
# TODO cambiar "Samples" por timestamp. Formatear para que quede lindo.
# TODO armar documentacion de Arduino, Python, y Base de Datos
# TODO dejar mas lindo el HTML
@app.route('/plot/temp')
def plot_temp():
    times, temps, hums, lights = getHistData(numSamples)
    ys = temps
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [°C]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    xs = range(numSamples)
    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot/hum')
def plot_hum():
    times, temps, hums, lights = getHistData(numSamples)
    ys = hums
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Humidity [%]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    xs = range(numSamples)
    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot/light')
def plot_light():
    times, temps, hums, lights = getHistData(numSamples)
    ys = lights
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Light [Lux]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    xs = range(numSamples)
    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == '__main__':
    app.run(debug=True)
