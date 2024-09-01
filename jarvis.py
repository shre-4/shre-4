import pyttsx3
import speech_recognition as sr
import webbrowser
import pyjokes
import datetime
import os
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recogninzing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("not understanding")

def speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    if sptext().lower() == "hey shreya":
           while True:   
              data1=sptext().lower()
              if "your name" in data1:
                  name= "my name is peter"
                  speech(name)
              elif "old are you" in data1:
                   age= "I have no age "
                   speech(age)
              elif "time" in data1:
                    time=   datetime.datetime.now().strftime("%I%M%p")
                    speech(time) 
              elif "youtube" in data1:
                     webbrowser.open("https://www.youtube.com/")
              elif "linkedin" in data1:
                     webbrowser.open("https://www.linkedin.com/")   
              elif "joke" in data1:
                    joke_1=pyjokes.get_jokes(language="en",category="neutral")
                    speech(joke_1)
   
              elif "exit" in data1:
                    speech("thank you have a nice day")
                    break
    
                
else:
     print("thanks")


