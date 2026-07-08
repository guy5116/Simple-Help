import urllib.parse
import webbrowser
from wikiAPI import wikiAPI
import string
from loadActionTarget import loadAction, loadTarget
from textReader import readText

def findAction(debug, text):

    #Loads Actions from text files
    actions = loadAction(debug)
    targets = loadTarget(debug)

    #Finds which action is needed
    action = next((word for word in text if word in actions), None)

    match action:
        case "open":
            # Find target in array and loads website based on the target
            target = next((word for word in text if word.strip(string.punctuation) in targets), None)
            if target == 'None':
                print("NULL Target")
                return
            print(f"The Action is {action} and the Target is {target}")
            webbrowser.open(f"https://www.{target}.com/")
            return
        case "explain":
            # Find target and search WikiAPI to find associated article, return summary, and read it with TTS
            position = text.index(action) + 1
            target = "".join(text[position:]).strip(string.punctuation)
            if debug: print(f"The Action is '{action}' and the Target is '{target}'")
            summary = wikiAPI(debug, target, 0)
            #readText(summary)
            print("The Summary is ", summary)
            return
        case "search":
            position = text.index(action) + 1
            if text[position] == 'for':
                position += 1
            target = "".join(text[position:]).strip(string.punctuation)
            if debug: print(f"The Action is '{action}' and the Target is '{target}'")
            url = f"https://www.google.com/search?q={urllib.parse.quote(target)}"
            webbrowser.open(url)
