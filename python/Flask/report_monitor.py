## @package report_monitor
# This module takes care of checking and sending a report by email.
import os
from datetime import datetime

from future.backports.datetime import timedelta

from SleepMonitor.python.Flask import graph_functions, email_sender, db_manager

WAIT_TO_SEND_REPORT = 5


## This method generates and sends a report
# @param email The email address of destination.
# @param initial The initial time for the range from where the report will be generated
# @param to The end time for the range from where the report will be generated
def send_report(email, initial, to):
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
    email_sender.send_email(email, email_sender.SUBJECT, email_sender.BODY,
                            [hum_graph, light_graph, temp_graph])


## This method checks if a certain time has elapsed in order to send the report by mail
# @param minutes The minutes to check
def check_report(minutes):
    return minutes == WAIT_TO_SEND_REPORT


## This method gets the time difference between a given time and now
# @param to The time to check
def get_time_difference(to):
    now = datetime.now()
    to_datetime = datetime(now.year, now.month, now.day, int(to[0:2]), int(to[3:5]), 00)
    difference = now - to_datetime
    return divmod(difference.seconds, 60)[0]


date = datetime(1970, 1, 1)

while True:
    try:
        email, initial, to = db_manager.get_sleeping_range()
        minutes = get_time_difference(to)
        if check_report(minutes):
            if not (date.day == datetime.now().day):
                print("Sending email to " + email)
                date = datetime.now()
                send_report(email, initial, to)
    except:
        print("No value configured in configuration!")
