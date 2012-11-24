from jinja2 import *
import datetime


def length(seconds):
    return str(datetime.timedelta(seconds=seconds))

environment.filters['gamelength'] = length
