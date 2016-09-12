#!/usr/bin/env python

import pywapi
import string
import sys
import math

#this requires pywapi which can be installed from https://code.google.com/p/python-weather-api/
#If in the US 00000 should be your area code
#If in Britian, try using the BBC weather scripts found here: https://github.com/duncanj/voice_scripts

# pass a second parameter, 'imperial' if you are feeling like ferinheight instead of celsius
#weather_com_result = pywapi.get_weather_from_weather_com(str(sys.argv[1]))
weather_com_result = pywapi.get_weather_from_weather_com('46556')

#print "It is " + string.lower(result['current_conditions']['text']) + " and " + result['current_conditions']['temperature'] + " degrees."0

#print "Google says: It is " + string.lower(google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_c'] + "C now.\n\n"

#tc = float(weather_com_result['current_conditions']['temperature'])
#tf = tc*1.8+32
#tcfinal = round(tc,0)
#tffinal = round(tf,0)
#print tc, tcfinal
#print "\n"
#print tf, tffinal
#print "\n"

print "Weather.com says: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + " degrees Celsius now."


#print "Humidity " + result['current_conditions']['humidity'] + " percent."

#today = result['forecasts'][0]
#highToday = today['high']
#if highToday > result['current_conditions']['temperature']:
#    print "The expected high is " + highToday + "."

#print "Overnight, " + today['night']['text'] + " with a low of " + today['low'] + " "
#if today['night']['chance_precip'] != "0":
#    print " and a " + today['night']['chance_precip'] + " percent chance of rain."

#tomorrow = result['forecasts'][1]
#print "Tomorrow, "+ tomorrow['day']['text'] + " with a high of " + tomorrow['high'] + " "

#if tomorrow['day']['chance_precip'] != "0":
#    print " and a " + tomorrow['day']['chance_precip'] + " percent chance of rain."
