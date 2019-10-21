import datetime as datetime

TIME_STAMP_FORMAT = '%Y-%m-%dT%H:%M'
STANDARD_FORMAT = '%Y-%m-%d %H:%M:%S'

PRETTY_FORMAT = '{:%A, %d %B %Y - %H:%M %p}'


## @package date_parser
#  This module takes care of parsing datetimes in string fomat to datetime objects

## This method takes a string that represents a datetime in a specific format and returns it as a datetime.
#  @param date_str The datetime as a string with a specific format.
#  @param format The format on which the datetime arrives
def parse_time(date_str: str, format: str):
    date_time_obj = datetime.datetime.strptime(date_str, format)
    return date_time_obj


## This method takes a string that represents a datetime in a specific format and returns another string that represent the same datetime with the PRETTY_FORMAT.
#  @param string_date The datetime as a string with a specific format that will be converted.
def string_to_format(string_date: str):
    date_time_obj = parse_time(string_date, TIME_STAMP_FORMAT)
    return PRETTY_FORMAT.format(date_time_obj)


## This method takes a string that represents a datetime in STANDARD_FORMAT and returns it as a datetime.
#  @param date_str The datetime as a string with a specific format.
def parse_standard(date_str: str):
    return parse_time(date_str, STANDARD_FORMAT)
