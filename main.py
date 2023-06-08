from Vibe import *
from Vibestats import *
import datetime

vibe = Vibe()
vibestats = Vibestats()
result = vibestats.minmaxweek(datetime.date(2023, 5, 11), "max")
vibestats.average(datetime.date(2023, 5, 11))