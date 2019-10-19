import datetime as datetime



def parse_time(date_str: str):
    date_time_obj = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
    return date_time_obj


# dt = "2019-10-12T01:00"
# parse_date = parse_time(dt)
# print('Date:', parse_date.date())
# print('Time:', parse_date.time())
# print('Date-time:', parse_date)
