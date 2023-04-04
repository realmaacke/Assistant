import os
import config

# assistant
import Assistant.functions as functions
import Assistant.operations.os.Close as close
import Assistant.operations.os.Open as open
import Assistant.operations.assistant.browse as browse

# sys tray
import SYSTRAY.mainTray as tray



while config.VOICE_ACTIVATED:
        query = functions.takeCommand().lower()

            # Settings for assistant
        if 'change my name' in query:
                functions.username()

        elif 'change your voice' in query:
                functions.changeVoice()

        elif 'debug' in query:
                functions.speak("Debug mode enable")
                print(query)

            # about assistant
        elif "what's your name" in query or "what is your name" in query:
            functions.speak("My creator calls me bladestorm")
            functions.speak("But you can call me Ivy 1.0")

        elif "who made you" in query or "who created you" in query:
            functions.speak("My creator is Marcus Pettersson")

            # Time & date & location

        elif "search for" in query:
            print(len(query))
            if len(query) >= 11:
                browse.searchFor(query, 2)
            else:
                browse.whatToSearchFor()

        elif "look up" in query:
            if len(query) >= 8:
                browse.searchFor(query, 2)
            else:
                browse.whatToSearchFor()

        elif "google" in query:
            if len(query) >= 7:
                browse.searchFor(query, 1)
            else:
                browse.whatToSearchFor()

            # os manipulation

        elif "close application" in query or "close app" in query:
            try:
                functions.speak("what app should i close")
                content = functions.takeCommand()
                functions.speak(close.close_app(content.lower()))
            except Exception as e:
                functions.speak("I am not able to close the application")


        elif "open application" in query or "open app" in query:
            try:
                functions.speak("what app should i open")
                content = functions.takeCommand()
                functions.speak(open.open_app(content.lower()))
                
            except Exception as e:
                functions.speak("I am not able to close the application")


        elif "close computer" in query or "shut down computer" in query or "shutdown computer" in query:
            os.system("shutdown /s /t 1")

        # quit app
        elif 'quit' in query:
            exit()
            
        elif 'exit' in query:
            exit()
            