import pyttsx
import thread
import os
import speech_recognition as sr

text="An application invokes the pyttsx.init() factory function to get a reference to a pyttsx.Engine instance. During construction, the engine initializes a pyttsx.driver.DriverProxy object responsible for loading a speech engine driver implementation from the pyttsx.drivers module. After construction, an application uses the engine object to register and unregister event callbacks; produce and stop speech; get and set speech engine properties; and start and stop event loops."
pid=0
pid=os.getpid()
r = sr.Recognizer()

def audioo():
	while True:
         with sr.Microphone() as source:
              print("Say something!")
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


thread.start_new_thread (audioo,())

engine = pyttsx.init()
engine.say(text)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
engine.setProperty('voice', "english")
engine.runAndWait()


