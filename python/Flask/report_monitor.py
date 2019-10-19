from datetime import datetime

from future.backports.datetime import timedelta

from python.Flask import db_manager, email_sender, graph_functions
from tempfile import TemporaryFile
import os

WAIT_TO_SEND_REPORT = 5


def send_report():
    email, initial, to = db_manager.get_sleeping_range()
    now = datetime.now()
    to_datetime = datetime(now.year, now.month, now.day, int(to[0:2]), int(to[3:5]), 00)
    from_datetime = datetime(now.year, now.month, now.day, int(initial[0:2]), int(initial[3:5]), 00)
    if to_datetime < from_datetime:
        yesterday = datetime.today() - timedelta(days=1)
        from_datetime = datetime(yesterday.year, yesterday.month, yesterday.day, int(initial[0:2]), int(initial[3:5]),
                                 00)
    graph_functions.generate_report_graphs(from_datetime, to_datetime)
    hum_graph = os.path.abspath("images/report/hum_graph.png")
    light_graph = os.path.abspath("images/report/light_graph.png")
    temp_graph = os.path.abspath("images/report/temp_graph.png")
    email_sender.send_email(email, email_sender.BODY, email_sender.BODY,
                            [hum_graph, light_graph, temp_graph])


def check_report(minutes):
    return minutes == WAIT_TO_SEND_REPORT


def get_time_difference_from_db():
    email, initial, to = db_manager.get_sleeping_range()
    now = datetime.now()
    to_datetime = datetime(now.year, now.month, now.day, int(to[0:2]), int(to[3:5]), 00)
    print(str(to_datetime))
    difference = now - to_datetime
    minutes = divmod(difference.seconds, 60)[0]
    return minutes


while True:
    try:
        minutes = get_time_difference_from_db()
        if check_report(minutes):
            send_report()
    except:
        print("No value configured in configuration!")
