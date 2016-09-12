#!/bin/bash

#zipcode=`cat $HOME/.misc | awk -F'zipcode==' '{print $2}'`
#zipcode=$1
zipcode=46556
result=`python /home/pi/PiAUISuite/Misc/getweather.py "zipcode"`

echo "$result"
tts "$result"

