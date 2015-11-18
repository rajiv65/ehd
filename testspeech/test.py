import pyttsx
text="An application invokes the pyttsx.init() factory function to get a reference to a pyttsx.Engine instance. During construction, the engine initializes a pyttsx.driver.DriverProxy object responsible for loading a speech engine driver implementation from the pyttsx.drivers module. After construction, an application uses the engine object to register and unregister event callbacks; produce and stop speech; get and set speech engine properties; and start and stop event loops."
def onWord(name, location, length):
   print 'word', name, location, length
   if location > 30:
      engine.stop()
engine = pyttsx.init()
engine.connect('started-word', onWord)
engine.say(text)
engine.runAndWait()
onWord("rajiv",10,12)