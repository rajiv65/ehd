import time
import sys
from urllib2 import urlopen
from json import loads
import codecs
import time
import pyttsx
import os
import speech_recognition as sr
import thread

pid=0
pid=os.getpid()
r = sr.Recognizer()
arg=""

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


count=0
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.setProperty('voice', "english")

response=""
event=""

arg = sys.argv[1]


for c in range(0,len(arg)):
    if arg[c]!='!':
       response=response+arg[c]
       count+=1
    else:
        break    


for index in range(count+1,len(arg)):
	event+=arg[index]


print response
print event

'''

#import RPi.GPIO as GPIO
#from buzzer import buzz

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#response = raw_input("Please input the time for the alarm in format HHMM: \n")
response=first_arg
event=second_arg

print response
print event
'''

print("Reminder has been set for %s hrs" % response)
#buzz(500,0.1)

alarm = int(response)
awake = 0
    # Loop to continuously check time, buzz the buzzer for the set alarm time
while True:
            # Continually get's the time as an integer value
    curr_time = int(time.strftime("%H%M"))

            # Buzzes the buzzer when the time reaches the set alarm time
    if curr_time == alarm:
    	engine.say("You've set an alarm. It's time for"+event+".")
        break

engine.runAndWait()
print ("Done")
os.system('kill -9 '+str(pid))
