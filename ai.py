import pyttsx3
import datetime
import speech_recognition as sr
#import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening boss!")
    speak(" i am siri. please tell me how may i help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning.....")
        r.pause_threshold = 1
        audio=r.listen(source)
        #self.pyaudio_module = self.get_pyaudio()
        #audio = self.pyaudio_module.PyAudio()
    try:
        import pyaudio
        print("recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
if  __name__ =="__main__":
    wishMe()
    takeCommand()
