import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyaudio
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():  
    hour=int(datetime.datetime.now().hour)
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
        #speak('sir please spell loudly')
        print("Listning.....")
        r.pause_threshold = 1
        r.energy_threshold=500
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
            speak("you are HIMANSHU my creater")
        elif "open google" in query:
            #speak('searching google sir please wait')
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir="F:\\NOKIA 2\\SD CARD\\Music"
            music=os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir,music[0]))
        
            
