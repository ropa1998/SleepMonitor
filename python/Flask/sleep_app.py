import io

import datetime as datetime
from flask import Flask, render_template, make_response, request, redirect, flash, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from python.Flask import date_parser, graph_functions
from python.Flask.db_manager import getLastData, maxRowsTable, getHistData, get_report_data, save_sleeping_range, \
    get_sleeping_range
from python.Flask.graph_functions import plot_temp_with_data, plot_hum_with_data, plot_light_with_data
from python.Flask.date_parser import parse_time

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


@app.route("/configuration")
def configuration():
    email, start, end = get_sleeping_range()
    template_data = {
        'email': email,
        'initial': start,
        'end': end,
    }
    return render_template('configuration.html', **template_data)


@app.route("/configuration", methods=['POST'])
def modify_configuration():
    save_sleeping_range(request.form.get("mail"), request.form.get('initial'), request.form.get('end'))
    flash("Your information was updated successfully")
    return render_template('configuration.html')


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
    graph_functions.generate_home_graphs(numSamples)
    template_data = {
        'time': date_parser.PRETTY_FORMAT.format(parse_time(time, date_parser.HOME_FORMAT)),
        'temp': temp,
        'hum': hum,
        'light': light,
        'numSamples': numSamples,
        'temp_graph': "static/images/home/temp_graph",
        'hum_graph': "static/images/home/hum_graph",
        'light_graph': "static/images/home/light_graph"
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

    graph_functions.generate_home_graphs(numSamples)
    template_data = {
        'time': date_parser.PRETTY_FORMAT.format(parse_time(time, date_parser.HOME_FORMAT)),
        'temp': temp,
        'hum': hum,
        'light': light,
        'numSamples': numSamples,
        'temp_graph': "static/images/home/temp_graph",
        'hum_graph': "static/images/home/hum_graph",
        'light_graph': "static/images/home/light_graph"
    }
    return render_template('home.html', **template_data)


# TODO refactor all plots in one method.
# TODO cambiar "Samples" por timestamp. Formatear para que quede lindo.
# TODO armar documentacion de Arduino, python, y Base de Datos


@app.route('/report_generator')
def generate_a_report():
    return render_template('report_generator.html')


@app.route('/report_generator', methods=['POST'])
def generate_post_report():
    global initial
    initial = request.form['initial']
    global to
    to = request.form['to']

    graph_functions.generate_report_graphs(date_parser.string_to_format(initial), date_parser.string_to_format(to))
    template_data = {
        'from': date_parser.string_to_format(initial),
        'to': date_parser.string_to_format(to),
    }

    print(template_data)
    return render_template('report.html', **template_data)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)
