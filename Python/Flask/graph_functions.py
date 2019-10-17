def plot_temp_with_data(data):
    times, temps, hums, lights = getDataAsTuple(data)
    ys = temps
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [°C]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    length = temps.__len__()
    xs = range(length)
    axis.plot(xs, ys)
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
    xs = range(length)
    axis.plot(xs, ys)
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
    xs = range(length)
    axis.plot(xs, ys)
    return fig
