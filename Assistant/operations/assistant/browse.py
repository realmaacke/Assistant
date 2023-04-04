import webbrowser
import Assistant.functions as functions

def searchFor(query, startIndex):

    splitString = query.split()

    resultString = ""

    for words in range(startIndex, len(splitString)):
        resultString = resultString + " " +splitString[words]

    webbrowser.open("https://www.google.com/search?q=" + resultString)
    functions.speak("Searching for " + resultString)

def whatToSearchFor():

    functions.speak("what should i search for")
    content = functions.takeCommand()

    webbrowser.open("https://www.google.com/search?q=" + content.lower())