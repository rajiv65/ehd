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
                 if inp=='stop motor':
                    print "Stopping motor"
                    os.system('kill -9 '+str(pid))
              except sr.UnknownValueError:
                     print("Google Speech Recognition could not understand audio")
              except sr.RequestError as e:
                     print("Could not request results from Google Speech Recognition service; {0}".format(e)) 



thread.start_new_thread (thread_audio,())

''' Rpi hardware code'''

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.say("Turning on the motor, Sir.")
engine.setProperty('rate', rate-50)
engine.setProperty('voice', "english")
engine.runAndWait()
while True: time.sleep(1)





