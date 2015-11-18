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

def call_the_articles_business():
    url = "http://api.nytimes.com/svc/topstories/v1/business.json?api-key=f2534c05939f85bd82ab204e8a9005b9:19:73425794 "
    return loads(urlopen(url).read())

def call_the_articles_world():
    url = "http://api.nytimes.com/svc/topstories/v1/world.json?api-key=f2534c05939f85bd82ab204e8a9005b9:19:73425794"
    return loads(urlopen(url).read())

def call_the_articles_sports():
    url = "http://api.nytimes.com/svc/topstories/v1/sports.json?api-key=f2534c05939f85bd82ab204e8a9005b9:19:73425794 "
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
engine.setProperty('rate', rate-50)
engine.setProperty('voice', "english")



articles_business = call_the_articles_business()
articles_world = call_the_articles_world()
articles_sports = call_the_articles_sports()

title=[]
abstract=[]

for i in range(0,5):

	title.append(articles_business["results"][i]['title'].encode('ascii', 'replace'))
	abstract.append(articles_business["results"][i]['abstract'].encode('ascii', 'replace'))
     

for i in range(0,5):

	title.append(articles_world["results"][i]['title'].encode('ascii', 'replace'))
	abstract.append(articles_world["results"][i]['abstract'].encode('ascii', 'replace'))
     

for i in range(0,5):

	title.append(articles_sports["results"][i]['title'].encode('ascii', 'replace'))
	abstract.append(articles_sports["results"][i]['abstract'].encode('ascii', 'replace'))
     

for i in range(0,15):
    if i==0:
        engine.say('business news')
    if i==5:
        engine.say('world news')
    if i==10:
        engine.say('sports news')   
    engine.say(title[i])
    engine.say(abstract[i])

engine.runAndWait()  

     
