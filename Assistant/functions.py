import Assistant.libraryImports as libraryImports
import config

engine = libraryImports.pyttsx3.init(config.TTS_ENGINE)
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[config.ASSISTANT_VOICE].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# config functions

def username():
    speak("What should i call you")
    uname = takeCommand()
    speak("i should call you" + uname)


def changeVoice():

    if config.ASSISTANT_VOICE == 1:
        config.ASSISTANT_VOICE = 0
        engine.setProperty('voice', voices[config.ASSISTANT_VOICE].id)
        print(config.ASSISTANT_VOICE)

        speak("Do you prefer this voice")

    elif config.ASSISTANT_VOICE == 0:
        config.ASSISTANT_VOICE = 1
        engine.setProperty('voice', voices[config.ASSISTANT_VOICE].id)
        print(config.ASSISTANT_VOICE)

        speak("Do you prefer this voice")

def takeCommand():

    r = libraryImports.sr.Recognizer()
     
    with libraryImports.sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = config.WAIT_TIME_TILL_RECOGNIZE
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language =config.LANGUAGE)
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    
    return(query)