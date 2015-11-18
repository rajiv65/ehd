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
rec = sr.Recognizer()
arg=""
first_arg=""
inp=""

def thread_audio():
    while True:
         with sr.Microphone() as source:
              audio = rec.listen(source)
              try:
                 inp=str(rec.recognize_google(audio))
                 print("You said "+inp)
                 if inp=='off':
                    GPIO.output(led1, 1)
                    print "Switching off light"
                    os.system('kill -9 '+str(pid))
              except sr.UnknownValueError:
                     print("Google Speech Recognition could not understand audio")
              except sr.RequestError as e:
                     print("Could not request results from Google Speech Recognition service; {0}".format(e)) 



thread.start_new_thread (thread_audio,())

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.setProperty('voice', "english")
engine.say("Switching on the light, Sir.")
engine.runAndWait()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led1=2
led2=3
led3=4

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

GPIO.output(led1, 1)
GPIO.output(led2, 0)
GPIO.output(led3,0)

while True: time.sleep(1)








