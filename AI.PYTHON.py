import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyaudio
import os
import sys
import pywhatkit
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():  
    hour=int(datetime.datetime.now().hour)
    speak("initializing network configuring system information crystal is now ready to respond")
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak(" i am crystal please tell me how may i help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak('sir please spell loudly')
        print("Listning.....")
        r.pause_threshold = 0.5
        r.energy_threshold=1000
        audio=r.listen(source)
    try:
        speak('i am recognizing speech')
        print("recognizing....")
        query=r.recognize_google(audio,language='eng-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
if  __name__ =="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia sir')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "who am i" in query:
            speak("you are HIMANSHU my creator")
        elif "open google" in query:
            speak('searching google sir please')
            webbrowser.open("google.com")
        elif "stop" in query:
            speak("ok stopping crystal sir ")
            sys.exit()
        elif "shutdown" in query:
            speak("ok shutting down crystal sir ")
            sys.exit()
        elif "youtube" in query:
            song=query.replace('play','')
            print("playing" + song)
            pywhatkit.playonyt(song)
        elif "okay" in query:
            speak(" alright sir ")
            print("alright")
        elif "wait" in query:
            speak("waitng sir")
            print("waiting sir")

            
        elif "where do you live" in query:
            speak("i live in panagarh near railway east cabin")
            print("i live in panagarh near railway east cabin")
            
        elif "where is your home town" in query:
            speak("my home town is in panagarh near railway east cabin")
            print("my hime town is in panagarh near railway east cabin")
            
            
        elif'google' in query:
            speak('searching google sir')
            query=query.replace('google','')
            results=wikipedia.summary(query,sentences=3)
            speak('according to google')
            print(results)
            speak(results)
        elif "time" in query:
            time=datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            speak(' sir current time is ' +time)
        elif "play music" in query:
            music_dir="F:\\NOKIA 2\\SD CARD\\Music"
            music=os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir,music[(random.randint(1,165))]))
        
            
