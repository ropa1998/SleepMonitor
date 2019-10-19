import datetime as datetime

TIME_STAMP_FORMAT = '%Y-%m-%dT%H:%M'
HOME_FORMAT = '%Y-%m-%d %H:%M:%S'

PRETTY_FORMAT = '{:%A, %d %B %Y - %H:%M %p}'

def parse_time(date_str: str, format:str):
    date_time_obj = datetime.datetime.strptime(date_str, format)
    return date_time_obj


def string_to_format(string_date:str):
    date_time_obj = parse_time(string_date, TIME_STAMP_FORMAT)
    return PRETTY_FORMAT.format(date_time_obj)


# dt = "2019-10-12T01:00"
# parse_date = parse_time(dt)
# print('Date:', parse_date.date())
# print('Time:', parse_date.time())
# print('Date-time:', parse_date)
