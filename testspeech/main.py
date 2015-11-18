import speech_recognition as sr
import os
import subprocess
import time
import signal
# obtain audio from the microphone
r = sr.Recognizer()
inp=""
pid=0
proc=0
pid=os.getpid()

#print pid

while True:
     with sr.Microphone() as source:
          print("Say something!")
          audio = r.listen(source)
          try:
             inp=str(r.recognize_google(audio))
             print("You said "+inp)
             if inp=="news":
                os.system('python news.py &')
             if inp=="weather":
                os.system('python weather.py &')
             if inp=="weather":
                os.system('python weather.py &')
             if 'alarm' in inp:
             	alarmstring=""
             	alarmtime=""
             	alarmevent=""
             	timecount=0
             	for i in range(6,len(inp)):
                    if inp[i]!=" ":
                       alarmtime+=inp[i]
                       timecount+=1
                    if inp[i]==" ":
                       break   
                alarmtime+='!'
             	
             	for i in range(timecount+6,len(inp)):
                    if inp[i]!=" ":
                       alarmevent+=inp[i]
                #print alarmtime
                #print alarmevent       
                alarmstring='python alarm.py '+alarmtime+alarmevent+' &'
                #print alarmstring   
                os.system(alarmstring)
             if 'read' in inp:
                 pdfname=""
                 pdfmode=""
                 namelength=0
                 pdfstring=""
                 for i in range(5,len(inp)):
                 	 if(inp[i]!=" "):
                 	 	pdfname+=inp[i]
                 	 	namelength+=1
                 	 else: break	
                 for i in range(namelength+6,len(inp)):
                 	 pdfmode+=inp[i]
                 #print pdfname
                 #print pdfmode
                 pdfstring='python pdf.py '+pdfname+"!"+pdfmode+" &"
                 print pdfstring
                 os.system(pdfstring)
             if inp=="fan on":
                os.system("python fan.py &")     

          except sr.UnknownValueError:
                 print("Google Speech Recognition could not understand audio")
          except sr.RequestError as e:
                 print("Could not request results from Google Speech Recognition service; {0}".format(e))
          

    