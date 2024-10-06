import speech_recognition as sr
import webbrowser
import pyttsx3
import songs_library
import pyjokes
from datetime import datetime
# pip install pocketsphinx
recognize =  sr.Recognizer()
engine = pyttsx3.init()
def speek(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "open google" in command.lower():
        webbrowser.open("http://google.com") 
    elif "open youtube" in command.lower():
        webbrowser.open("http://youtube.com")
    elif "open what" in command.lower():
        webbrowser.open("https://web.whatsapp.com/")  
    elif "open facebook" in command.lower():
        webbrowser.open("http://facebook.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("http://linkedin.com")  
    elif command.lower().startswith("play"):
        songs = command.lower().split(" ")[1]
        link = songs_library.musics[songs]
        webbrowser.open(link)
    elif "jokes" in command.lower():
        joke =pyjokes.get_joke()
        print(joke)
        speek(joke)
    elif "date" in command.lower():
        now = datetime.now()
        short_format = now.strftime("%m/%d/%y")
        speek(f"Today's date is {short_format}")
    elif "time" in command.lower():
        now = datetime.now()
        short_format = now.strftime("%I:%M %p")
        speek(f"Present time is {short_format}")


if __name__ =="__main__":
    speek("Initializing jarvis")
    while True:
        #listening audio from microphone
        r = sr.Recognizer()
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listining....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speek("yaa,tell me")
                with sr.Microphone() as source:
                    print("jarvis is Active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    process_command(command)   
        except Exception as e:
            print("Error; {}".format(e))



