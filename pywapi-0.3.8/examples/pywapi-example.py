#!/usr/bin/env python

import pywapi
import string

weather_com_result = pywapi.get_weather_from_weather_com('10001')
noaa_result = pywapi.get_weather_from_noaa('KJFK')

print "Weather.com says: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "C now in New York."

print("NOAA says: It is " + noaa_result['weather'].lower() + " and " + noaa_result['temp_c'] + "C now in New York.")
