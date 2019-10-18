import io

import datetime as datetime
from flask import Flask, render_template, make_response, request, redirect, flash, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from python.Flask.db_manager import getLastData, maxRowsTable, getHistData, get_report_data
from python.Flask.graph_functions import plot_temp_with_data, plot_hum_with_data, plot_light_with_data
from python.Flask.utils import parse_time

app = Flask(__name__)

# initialize global variables
global numSamples
numSamples = maxRowsTable()
if (numSamples > 101):
    numSamples = 100

global initial
initial = datetime.datetime.now()

global to
to = datetime.datetime.now()


# main route
@app.route("/")
def index():
    return render_template('index.html')


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
    template_data = {
        'time': time,
        'temp': temp,
        'hum': hum,
        'light': light,
        'numSamples': numSamples
    }
    return render_template('home.html', **template_data)


@app.route('/home', methods=['POST'])
def my_form_post():
    global numSamples
    numSamples = int(request.form['numSamples'])
    num_max_samples = maxRowsTable()
    if numSamples > num_max_samples:
        numSamples = (num_max_samples - 1)

    time, temp, hum, light = getLastData()

    template_data = {
        'time': time,
        'temp': temp,
        'hum': hum,
        'light': light,
        'numSamples': numSamples
    }
    return render_template('home.html', **template_data)


# TODO refactor all plots in one method.
# TODO cambiar "Samples" por timestamp. Formatear para que quede lindo.
# TODO armar documentacion de Arduino, python, y Base de Datos
@app.route('/plot/temp')
def plot_temp():
    data = getHistData(numSamples)
    fig = plot_temp_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot/hum')
def plot_hum():
    data = getHistData(numSamples)
    fig = plot_hum_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot/light')
def plot_light():
    data = getHistData(numSamples)
    fig = plot_light_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/reports')
def generate_a_report():
    return render_template('reports.html')


@app.route('/report/temp')
def report_temp():
    global initial
    global to
    data = get_report_data(parse_time(initial),parse_time(to))
    fig = plot_temp_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/report/hum')
def report_hum():
    global initial
    global to
    data = get_report_data(parse_time(initial),parse_time(to))
    fig = plot_hum_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/report/light')
def report_light():
    global initial
    global to
    data = get_report_data(parse_time(initial),parse_time(to))
    fig = plot_light_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/reports', methods=['POST'])
def generate_post_report():
    template_data = {
        'from': request.form['initial'],
        'to': request.form['to'],
    }
    global initial
    initial = request.form['initial']
    global to
    to = request.form['to']

    print(template_data)
    return render_template('report.html', **template_data)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
