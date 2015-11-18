import pyPdf
import pyttsx
import sys
import time
from urllib2 import urlopen
from json import loads
import codecs
import os
import speech_recognition as sr
import thread

pid=0
pid=os.getpid()
rec = sr.Recognizer()
arg=""
first_arg=""
second_arg=""
name_length=0
inp=""

def thread_audio():
    while True:
         with sr.Microphone() as source:
              audio = rec.listen(source)
              try:
                 inp=str(rec.recognize_google(audio))
                 print("You said "+inp)
                 if inp=='stop':
                    os.system('kill -9 '+str(pid))
              except sr.UnknownValueError:
                     print("Google Speech Recognition could not understand audio")
              except sr.RequestError as e:
                     print("Could not request results from Google Speech Recognition service; {0}".format(e))         


 
thread.start_new_thread (thread_audio,())

arg = sys.argv[1]

for i in range(0,len(arg)):
    if arg[i]!='!':
       first_arg+=arg[i]
       name_length+=1
    else: break

for i in range(name_length+1,len(arg)):
    second_arg+=arg[i]    

#f = open('myfile.txt','w')
#f.write("hello")

def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content



def onStart(name):
   print 'starting reading'
def onWord(name, location, length):
   f = open(first_arg+'.txt','w')
   f.write(str(location)+" "+str(length)+"\n")
   f.close()

def onEnd(name, completed):
   print 'Done reading'
   


engine = pyttsx.init()


if second_arg=='start':
   f = open(first_arg+'.txt','w')
   f.write("0 0")
   f.close() 



try:
    content= getPDFContent(first_arg+'.pdf').encode("ascii", "ignore")
except IOError:
    print "no such file"
    engine.say("Sorry. No such file.")
    engine.runAndWait()
    sys.exit()

newcontent=""

r=open(first_arg+'.txt','r+')
filecontent=r.read()

location=""
length=""
offset=0

for char in filecontent:
    if char!=" ":
       location+=char
       offset+=1
    else:
         break 

#print location
#print len(filecontent)
offset+=1


for x in range(offset,len(filecontent)-2):
    length+=filecontent[x]


location=int(location)


for i in range(location,len(content)-location):
    newcontent+=content[location+i-1]



rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.setProperty('voice', "english")
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say(newcontent)
engine.runAndWait()
