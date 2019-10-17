from matplotlib.figure import Figure

from SleepMonitor.Python.Flask.db_manager import getDataAsTuple


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
    axis.axhspan(25, 35, facecolor='red', alpha=0.3)
    axis.axhspan(20, 25, facecolor='yellow', alpha=0.5)
    axis.axhspan(16, 20, facecolor='green', alpha=0.3)
    axis.axhspan(11, 16, facecolor='yellow', alpha=0.5)
    axis.axhspan(0, 11, facecolor='red', alpha=0.3)
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
    axis.axhspan(30, 40, facecolor='red', alpha=0.3)
    axis.axhspan(40, 45, facecolor='yellow', alpha=0.5)
    axis.axhspan(45, 55, facecolor='green', alpha=0.3)
    axis.axhspan(55, 60, facecolor='yellow', alpha=0.5)
    axis.axhspan(60, max(ys) + 5 if max(ys) > 60 else 70, facecolor='red', alpha=0.3)
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
    axis.axhspan(0, 5, facecolor='green', alpha=0.3)
    axis.axhspan(5, 10, facecolor='yellow', alpha=0.5)
    axis.axhspan(10, max(ys) if max(ys) > 10 else 20, facecolor='red', alpha=0.3)
    return fig
