## @package sleep_app
# This is the main module, which takes care of all the app routing
import datetime as datetime
import io

from flask import Flask, render_template, make_response, request, redirect, flash, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from SleepMonitor.python.Flask import date_parser
from SleepMonitor.python.Flask.date_parser import parse_time
from SleepMonitor.python.Flask.db_manager import maxRowsTable, get_sleeping_range, save_sleeping_range, getLastData, \
    getHistData, get_report_data
from SleepMonitor.python.Flask.graph_functions import plot_temp_with_data, plot_hum_with_data, plot_light_with_data

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
## This method renders the main page, index.html.
def index():
    return render_template('index.html')


@app.route("/configuration")
## This method gets the configuration information from the database and renders the html.
def configuration():
    # TODO que get_sleeping_ranges no se rompa si devuelve nulls.
    # TODO que todos los accesos a base de datos esten preparados para no traer nada.
    try:
        email, start, end = get_sleeping_range()
    except:
        email, start, end = "", "", ""
    template_data = {
        'email': email,
        'initial': start,
        'end': end,
    }
    return render_template('configuration.html', **template_data)


@app.route("/configuration", methods=['POST'])
## This method saves a given configuration to the database and sends a message back to the user to confirm that the configuration was saves successfully .
def modify_configuration():
    save_sleeping_range(request.form.get("mail"), request.form.get('initial'), request.form.get('end'))
    flash("Your information was updated successfully")
    return redirect(url_for('configuration'))


@app.route("/", methods=['POST'])
## This method validates the username and password and renders the home scren or login screen with an error message.
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
## This method searches the database for: the latest data and the last given number of samples to render the home screen.
def home():
    time, temp, hum, light = getLastData()
    template_data = {
        'time': date_parser.PRETTY_FORMAT.format(parse_time(time, date_parser.STANDARD_FORMAT)),
        'temp': temp,
        'hum': hum,
        'light': light,
        'numSamples': numSamples,
    }
    return render_template('home.html', **template_data)


@app.route('/home', methods=['POST'])
## This method updates the onld data by searching the database for: the latest data and the last given number of samples to render the home screen.
def my_form_post():
    global numSamples
    numSamples = int(request.form['numSamples'])
    num_max_samples = maxRowsTable()
    if numSamples > num_max_samples:
        numSamples = (num_max_samples - 1)

    time, temp, hum, light = getLastData()

    template_data = {
        'time': date_parser.PRETTY_FORMAT.format(parse_time(time, date_parser.STANDARD_FORMAT)),
        'temp': temp,
        'hum': hum,
        'light': light,
        'numSamples': numSamples,
    }
    return render_template('home.html', **template_data)


@app.route('/report_generator')
## This method renders the report generator screen.
def generate_a_report():
    return render_template('report_generator.html')


@app.route('/report_generator', methods=['POST'])
## This method receives an range and renders the report screen.
def generate_post_report():
    global initial
    initial = request.form['initial']
    global to
    to = request.form['to']

    template_data = {
        'from': date_parser.string_to_format(initial),
        'to': date_parser.string_to_format(to),
    }

    print(template_data)
    return render_template('report.html', **template_data)


@app.route('/plot/temp')
## This method renders an image with a plot of the temperature to be used in the home screen.
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
## This method renders an image with a plot of the humidity to be used in the home screen.
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
## This method renders an image with a plot of the light to be used in the home screen.
def plot_light():
    data = getHistData(numSamples)
    fig = plot_light_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/report/temp')
## This method renders an image with a plot of the temperature to be used in the report.
def report_temp():
    global initial
    global to
    data = get_report_data(parse_time(initial, date_parser.TIME_STAMP_FORMAT),
                           parse_time(to, date_parser.TIME_STAMP_FORMAT))
    fig = plot_temp_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/report/hum')
## This method renders an image with a plot of the humidity to be used in the report.
def report_hum():
    global initial
    global to
    data = get_report_data(parse_time(initial, date_parser.TIME_STAMP_FORMAT),
                           parse_time(to, date_parser.TIME_STAMP_FORMAT))
    fig = plot_hum_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/report/light')
## This method renders an image with a plot of the light to be used in the report.
def report_light():
    global initial
    global to
    data = get_report_data(parse_time(initial, date_parser.TIME_STAMP_FORMAT),
                           parse_time(to, date_parser.TIME_STAMP_FORMAT))
    fig = plot_light_with_data(data)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0')
