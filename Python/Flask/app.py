import io
import sqlite3 as lite

from flask import Flask, render_template, make_response, request, redirect, flash, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

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
    return render_template('index.html')


@app.route("/reports")
def reports():
    return render_template('reports.html')


@app.route("/", methods=['POST'])
def login_post():
    email = request.form.get('username')
    password = request.form.get('password')

    # TODO: improve this?
    if email == 'admin' and password == 'admin':
        return redirect(url_for('home'))
    else:
        flash('Invalid credentials')
        return redirect(url_for('index'))


@app.route("/home")
def home():
    time, temp, hum, light = getLastData()
    templateData = {
        'time': time,
        'temp': temp,
        'hum': hum,
        'light': light,
        'numSamples': numSamples
    }
    return render_template('home.html', **templateData)


@app.route('/home', methods=['POST'])
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
    return render_template('home.html', **templateData)


# TODO refactor all plots in one method.
# TODO cambiar "Samples" por timestamp. Formatear para que quede lindo.
# TODO armar documentacion de Arduino, Python, y Base de Datos
@app.route('/plot/temp')
def plot_temp():
    times, temps, hums, lights = getHistData(numSamples)
    ys = temps
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [°C]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    axis.set_ylim([min(ys)-5, max(ys)+5])
    xs = range(numSamples)
    axis.plot(xs, ys)
    axis.axhspan(25, 35, facecolor='red', alpha=0.3)
    axis.axhspan(20, 25, facecolor='yellow', alpha=0.5)
    axis.axhspan(16, 20, facecolor='green', alpha=0.3)
    axis.axhspan(11, 16, facecolor='yellow', alpha=0.5)
    axis.axhspan(0, 11, facecolor='red', alpha=0.3)
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
    axis.set_ylim([min(ys)-5, max(ys)+5])
    xs = range(numSamples)
    axis.plot(xs, ys)
    print(min(temps))
    axis.axhspan(min(ys) - 5 if min(ys) < 30 else 30, 40, facecolor='red', alpha=0.3)
    axis.axhspan(40, 45, facecolor='yellow', alpha=0.5)
    axis.axhspan(45, 55, facecolor='green', alpha=0.3)
    axis.axhspan(55, 60, facecolor='yellow', alpha=0.5)
    axis.axhspan(60, max(ys) + 5 if max(ys) > 60 else 70, facecolor='red', alpha=0.3)
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
    axis.set_ylim([min(ys)-3, max(ys)+3])
    xs = range(numSamples)
    axis.plot(xs, ys)
    axis.axhspan(0, 5, facecolor='green', alpha=0.3)
    axis.axhspan(5, 10, facecolor='yellow', alpha=0.5)
    axis.axhspan(10, max(ys)  if max(ys) > 10 else 20, facecolor='red', alpha=0.3)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
