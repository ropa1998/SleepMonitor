## @package graph_functions
# This module takes care of creating all graphics that are used along the program.

import matplotlib.pyplot as plt

from python.Flask import date_parser, db_manager
from python.Flask.db_manager import getDataAsTuple, getHistData

TEMP_GREEN_LOW = 16
TEMP_GREEN_HIGH = 20
TEMP_INFERIOR_YELLOW_LOW = 11
TEMP_INFERIOR_YELLOW_HIGH = 16
TEMP_SUPERIOR_YELLOW_LOW = 20
TEMP_SUPERIOR_YELLOW_HIGH = 25
TEMP_INFERIOR_RED_LOW = 0
TEMP_INFERIOR_RED_HIGH = 11
TEMP_SUPERIOR_RED_LOW = 25
TEMP_SUPERIOR_RED_HIGH = 35

LIGHT_GREEN_LOW = 0
LIGHT_GREEN_HIGH = 5
LIGHT_YELLOW_LOW = 5
LIGHT_YELLOW_HIGH = 10
LIGHT_RED_LOW = 10
LIGHT_RED_HIGH = 20

HUM_GREEN_LOW = 30
HUM_GREEN_HIGH = 50
HUM_INFERIOR_YELLOW_LOW = 25
HUM_INFERIOR_YELLOW_HIGH = 30
HUM_SUPERIOR_YELLOW_LOW = 50
HUM_SUPERIOR_YELLOW_HIGH = 55
HUM_INFERIOR_RED_LOW = 0
HUM_INFERIOR_RED_HIGH = 25
HUM_SUPERIOR_RED_LOW = 55
HUM_SUPERIOR_RED_HIGH = 100

GREEN_ALPHA = 0.3
YELLOW_ALPHA = 0.5
RED_ALPHA = 0.3

X_AXIS_LABEL = "Time"
TEMPERATURE_LABEL = "Temperature [°C]"
HUMIDITY_LABEL = "Humidity [%]"
LIGHT_LABEL = "Light [Lux]"

HOME = "home"
REPORT = "report"


## This method takes data straight from the 'db_manager' and returns a figure with time in the X-axis and temperature in the Y-Axis
# @param data 'sensors_data' rows straight from the database without any transformation.
def plot_temp_with_data(data):
    times, temps, hums, lights = getDataAsTuple(data)
    times = list(map(date_parser.parse_standard, times))
    ys = temps
    fig, axis = plt.subplots()
    axis.set_title(TEMPERATURE_LABEL)
    axis.set_xlabel(X_AXIS_LABEL)
    axis.grid(True)
    axis.set_ylim([min(ys) - 5, max(ys) + 5]) if ys.__len__() >= 1 else axis.set_ylim()
    xs = times
    axis.plot(xs, ys)
    fig.autofmt_xdate()
    if ys.__len__() >= 1:
        axis.axhspan(TEMP_SUPERIOR_RED_LOW, TEMP_SUPERIOR_RED_HIGH, facecolor='red', alpha=RED_ALPHA)
        axis.axhspan(TEMP_SUPERIOR_YELLOW_LOW, TEMP_SUPERIOR_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
        axis.axhspan(TEMP_GREEN_LOW, TEMP_GREEN_HIGH, facecolor='green', alpha=RED_ALPHA)
        axis.axhspan(TEMP_INFERIOR_YELLOW_LOW, TEMP_INFERIOR_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
        axis.axhspan(TEMP_INFERIOR_RED_LOW, TEMP_INFERIOR_RED_HIGH, facecolor='red', alpha=RED_ALPHA)
    return fig


## This method takes data straight from the 'db_manager' and returns a figure with time in the X-axis and humidity percentage in the Y-Axis
# @param data 'sensors_data' rows straight from the database without any transformation.
def plot_hum_with_data(data):
    times, temps, hums, lights = getDataAsTuple(data)
    times = list(map(date_parser.parse_standard, times))
    ys = hums
    fig, axis = plt.subplots()
    axis.set_title(HUMIDITY_LABEL)
    axis.set_xlabel(X_AXIS_LABEL)
    axis.grid(True)
    axis.set_ylim([min(ys) - 5, max(ys) + 5]) if ys.__len__() >= 1 else axis.set_ylim()
    xs = times
    axis.plot(xs, ys)
    fig.autofmt_xdate()
    if ys.__len__() >= 1:
        axis.axhspan(HUM_INFERIOR_RED_LOW if min(ys) > HUM_INFERIOR_RED_LOW else min(ys) - 5, HUM_INFERIOR_RED_HIGH,
                     facecolor='red', alpha=RED_ALPHA)
        axis.axhspan(HUM_INFERIOR_YELLOW_LOW, HUM_INFERIOR_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
        axis.axhspan(HUM_GREEN_LOW, HUM_GREEN_HIGH, facecolor='green', alpha=GREEN_ALPHA)
        axis.axhspan(HUM_SUPERIOR_YELLOW_LOW, HUM_SUPERIOR_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
        axis.axhspan(HUM_SUPERIOR_RED_LOW, max(ys) + 5 if max(ys) > 60 else 70, facecolor='red', alpha=RED_ALPHA)
    return fig


## This method takes data straight from the 'db_manager' and returns a figure with time in the X-axis and lux level in the Y-Axis
# @param data 'sensors_data' rows straight from the database without any transformation.
def plot_light_with_data(data):
    times, temps, hums, lights = getDataAsTuple(data)
    times = list(map(date_parser.parse_standard, times))
    ys = lights
    fig, axis = plt.subplots()
    axis.set_title(LIGHT_LABEL)
    axis.set_xlabel(X_AXIS_LABEL)
    axis.grid(True)
    axis.set_ylim([0, max(ys) + 5]) if ys.__len__() >= 1 else axis.set_ylim()
    xs = times
    axis.plot(xs, ys)
    fig.autofmt_xdate()
    if ys.__len__() >= 1:
        axis.axhspan(LIGHT_GREEN_LOW, LIGHT_GREEN_HIGH, facecolor='green', alpha=GREEN_ALPHA)
        axis.axhspan(LIGHT_YELLOW_LOW, LIGHT_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
        axis.axhspan(LIGHT_RED_LOW, max(ys) if max(ys) > 10 else 20, facecolor='red', alpha=RED_ALPHA)
    return fig


## This method takes data straight from the 'db_manager' and returns a figure with time in the X-axis and temperature in the Y-Axis. It laters stores this figure as a .png in the given path.
# @param data 'sensors_data' rows straight from the database without any transformation.
# @param path The path on which the user wants to save the image
def generate_temp(data, path):
    fig = plot_temp_with_data(data)
    fig.savefig('images/' + path + '/temp_graph.png')


## This method takes data straight from the 'db_manager' and returns a figure with time in the X-axis and humidity levels in the Y-Axis. It laters stores this figure as a .png in the given path.
# @param data 'sensors_data' rows straight from the database without any transformation.
# @param path The path on which the user wants to save the image
def generate_hum(data, path):
    fig = plot_hum_with_data(data)
    fig.savefig('images/' + path + '/hum_graph.png')


## This method takes data straight from the 'db_manager' and returns a figure with time in the X-axis and lux levels in the Y-Axis. It laters stores this figure as a .png in the given path.
# @param data 'sensors_data' rows straight from the database without any transformation.
# @param path The path on which the user wants to save the image
def generate_light(data, path):
    fig = plot_light_with_data(data)
    fig.savefig('images/' + path + '/light_graph.png')


## This method takes an int 'n' that will later look for the last 'n' rows in the 'sensors_data' and generate automatically three graphs with that data: one for tempertaure, one for humidity an done for lux levels. It laters stores them in the HOME path.
# @param numSamples 'sensors_data' rows straight from the database without any transformation.
def generate_home_graphs(numSamples):
    data = getHistData(numSamples)
    generate_hum(data, HOME)
    generate_light(data, HOME)
    generate_temp(data, HOME)


## This method takes two dattimes and gets the rows in the 'sensors_data' table that fall into the range passed. It then generates automatically three graphs with that data: one for tempertaure, one for humidity an done for lux levels. It laters stores them in the REPORT path.
# @param initial The initial date for the range from where the info will be taken from
# @param to The to date for the range from where the info will be taken from
def generate_report_graphs(initial, to):
    data = db_manager.get_report_data(initial, to)
    generate_hum(data, REPORT)
    generate_light(data, REPORT)
    generate_temp(data, REPORT)

# init = datetime(2019, 10, 12, 00, 00, 00)
# to = datetime(2019, 10, 19, 20, 00, 00)
#
# generate_report_graphs(init, to)
