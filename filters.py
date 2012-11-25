from jinja2 import *
import datetime

date_format = "%m/%d/%Y"


def length(seconds):
    return str(datetime.timedelta(seconds=seconds))


def date(date_time):
    return date_time.strftime(date_format)
