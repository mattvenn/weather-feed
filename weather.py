#!/usr/bin/env python
import random
import requests
from pprint import pprint
import csv
import datetime
from xively import xively
from post_data import cursive_data
import logging

url = "http://api.openweathermap.org/data/2.5/weather?q=Bristol,uk&units=metric"

# fetch the url
r = requests.get(url)
# sometimes the data is invalid - so we handle it nicely
try:
    data = r.json()
except ValueError:
    print("got bad data, quitting")
    exit(1)

# print it nicely
#pprint(data)

# grab the bits we want in separate variables
wind = data["wind"]["speed"]
temp = data["main"]["temp"]
# we subtract 800 to get a number from 0 to 5 see link below about
# conditions : http://openweathermap.org/weather-conditions
clouds = data["clouds"]["all"] + random.random()/10
# get the date and time
date = datetime.datetime.now()
"""
# write the data as a CSV file
with open('log.csv', 'a') as fh:
    writer = csv.writer(fh)
    writer.writerow([date,wind, temp, clouds])
"""

feed_id = "1426337377"
xively_timeout = 10
logging.basicConfig(level=logging.INFO)
"""
xively_t = xively(feed_id, logging, timeout=xively_timeout, keyfile="api.key")
xively_t.add_datapoint('wind',wind)
xively_t.add_datapoint('temp',temp)
xively_t.add_datapoint('clouds',clouds)
xively_t.start()
"""
datastore_id = 13
key = 'clouds'
value = clouds

cd = cursive_data(datastore_id)
cd.add_datapoint(key, value)
cd.start()
