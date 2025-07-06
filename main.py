import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
   if "open google" in command.lower() :
      webbrowser.open("https://www.google.com/")
   elif "open youtube" in command.lower() :
      webbrowser.open("https://www.youtube.com/")
   elif command.lower().startswith("play"):
      song = command.lower().split(" ")[1]   
      link = musiclibrary.music[song]
      webbrowser.open(link)
if __name__ == "__main__" :
  speak("initialize jarvis.....")
  #listen for the wake word jarvis
  while True :
    r = sr.Recognizer()
    

    print("recognizing....")
    try:
        with sr.Microphone() as source:
          print("listening!")
          audio = r.listen(source,timeout=2,phrase_time_limit=1)
        word = r.recognize_google(audio)
        if (word.lower() == "jarvis"):
           speak("ya")
           with sr.Microphone() as source:
            print("jarvis active")
            audio = r.listen(source)
            command = r.recognize_google(audio)
            process_command(command)
    except Exception as e:
        print("error; {0}".format(e))