from urllib2 import urlopen
from json import loads
import codecs
import time
import pyttsx
import os
import atexit
import sys
import signal
import speech_recognition as sr
import thread

pid=0
pid=os.getpid()
r = sr.Recognizer()






def get_weather_details():
    url = "http://api.openweathermap.org/data/2.5/weather?q=gandhinagar&APPID=0161c61999369a6dc6090163da35d4ba&units=metric"
    return loads(urlopen(url).read())


def thread_audio():
    while True:
         with sr.Microphone() as source:
              audio = r.listen(source)
              try:
                 inp=str(r.recognize_google(audio))
                 print("You said "+inp)
                 if inp=='stop':
                    os.system('kill -9 '+str(pid))
              except sr.UnknownValueError:
                     print("Google Speech Recognition could not understand audio")
              except sr.RequestError as e:
                     print("Could not request results from Google Speech Recognition service; {0}".format(e))         


 
thread.start_new_thread (thread_audio,())



engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-70)
engine.setProperty('voice', "english")

main=""
description=""
temp=0
pressure=0
humidity=0
windspeed=0
cloudy=0


weather_details = get_weather_details()
main=weather_details["weather"][0]['main']
description=weather_details["weather"][0]['description']
temp=weather_details["main"]['temp']
pressure=(weather_details["main"]['pressure'])/1000
humidity=weather_details["main"]['humidity']
windspeed=weather_details["wind"]['speed']
cloudy=weather_details['clouds']['all']

engine.say("Today's weather report. Mainly"+main+".")
engine.say("description"+description+".")
engine.say("Temperature"+str(temp)+"degree celsius.")
engine.say("Pressure"+str(pressure)+"barometer.")
engine.say("Humidity"+str(humidity)+"percentage.")
engine.say("Wind speed"+str(windspeed)+"meters per second")
engine.say("Clouds"+str(cloudy)+"percentage.")
engine.runAndWait()
#. Pressure in barometer"+pressure.toString()+"Humidity"+humidity.toString()+"percent. Wind speed"+windspeed.toString()+"meters per second. Clouds"+cloudy.toString()+"percent"