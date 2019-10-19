from datetime import datetime

from python.Flask import db_manager, sleep_app, email_sender
from tempfile import TemporaryFile
import os


def send_report():
    pass


def create_and_save_report(initial, to):
    report = sleep_app.generate_report_html(initial, to)
    f = open("report.html", "w+")
    f.write(report)
    return os.path.abspath("report.html")


def check_report(minutes):
    if minutes == 5:
        email, initial, to = db_manager.get_sleeping_range()
        path = create_and_save_report(initial, to)
        email_sender.send_email(email, "Your SleepMonitor report is ready!", "", [path])


def get_time_difference_from_db():
    email, initial, to = db_manager.get_sleeping_range()
    now = datetime.now()
    to_datetime = datetime(now.year, now.month, now.day, int(to[0:2]), int(to[3:5]), 00)
    print(str(to_datetime))
    difference = now - to_datetime
    minutes = divmod(difference.seconds, 60)[0]
    return minutes


check_report(5)

while True:
    minutes = get_time_difference_from_db()
    if check_report(minutes):
       send_report()