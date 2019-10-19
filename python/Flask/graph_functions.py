from matplotlib.figure import Figure

from python.Flask.db_manager import getDataAsTuple

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

HUM_GREEN_LOW = 45
HUM_GREEN_HIGH = 55
HUM_INFERIOR_YELLOW_LOW = 40
HUM_INFERIOR_YELLOW_HIGH = 45
HUM_SUPERIOR_YELLOW_LOW = 55
HUM_SUPERIOR_YELLOW_HIGH = 60
HUM_INFERIOR_RED_LOW = 30
HUM_INFERIOR_RED_HIGH = 40
HUM_SUPERIOR_RED_LOW = 60
HUM_SUPERIOR_RED_HIGH = 100

GREEN_ALPHA = 0.3
YELLOW_ALPHA = 0.5
RED_ALPHA = 0.3


def plot_temp_with_data(data):
    times, temps, hums, lights = getDataAsTuple(data)
    ys = temps
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [°C]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    length = temps.__len__()
    axis.set_ylim([min(ys) - 5, max(ys) + 5])
    xs = range(length)
    axis.plot(xs, ys)
    axis.axhspan(TEMP_SUPERIOR_RED_LOW, TEMP_SUPERIOR_RED_HIGH, facecolor='red', alpha=RED_ALPHA)
    axis.axhspan(TEMP_SUPERIOR_YELLOW_LOW, TEMP_SUPERIOR_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
    axis.axhspan(TEMP_GREEN_LOW, TEMP_GREEN_HIGH, facecolor='green', alpha=RED_ALPHA)
    axis.axhspan(TEMP_INFERIOR_YELLOW_LOW, TEMP_INFERIOR_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
    axis.axhspan(TEMP_INFERIOR_RED_LOW, TEMP_INFERIOR_RED_HIGH, facecolor='red', alpha=RED_ALPHA)
    return fig


def plot_hum_with_data(data):
    times, temps, hums, lights = getDataAsTuple(data)
    ys = hums
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Humidity [%]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    length = hums.__len__()
    axis.set_ylim([min(ys) - 5, max(ys) + 5])
    xs = range(length)
    axis.plot(xs, ys)
    axis.axhspan(HUM_INFERIOR_RED_LOW if min(ys) > HUM_INFERIOR_RED_LOW else min(ys)-5, HUM_INFERIOR_RED_HIGH, facecolor='red', alpha=RED_ALPHA)
    axis.axhspan(HUM_INFERIOR_YELLOW_LOW, HUM_INFERIOR_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
    axis.axhspan(HUM_GREEN_LOW, HUM_GREEN_HIGH, facecolor='green', alpha= GREEN_ALPHA)
    axis.axhspan(HUM_SUPERIOR_YELLOW_LOW, HUM_SUPERIOR_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
    axis.axhspan(HUM_SUPERIOR_RED_LOW, max(ys) + 5 if max(ys) > 60 else 70, facecolor='red', alpha=RED_ALPHA)
    return fig


def plot_light_with_data(data):
    times, temps, hums, lights = getDataAsTuple(data)
    ys = lights
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Light [Lux]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    length = lights.__len__()
    axis.set_ylim([min(ys) - 5, max(ys) + 5])
    xs = range(length)
    axis.plot(xs, ys)
    axis.axhspan(LIGHT_GREEN_LOW, LIGHT_GREEN_HIGH, facecolor='green', alpha=GREEN_ALPHA)
    axis.axhspan(LIGHT_YELLOW_LOW, LIGHT_YELLOW_HIGH, facecolor='yellow', alpha=YELLOW_ALPHA)
    axis.axhspan(LIGHT_RED_LOW, max(ys) if max(ys) > 10 else 20, facecolor='red', alpha=RED_ALPHA)
    return fig
