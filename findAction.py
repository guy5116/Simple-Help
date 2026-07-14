from wikiAPI import wikiAPI
import string
from loadActionTarget import loadAction, loadTarget
from openAction import open
from searchAction import search

def findAction(debug, text):

    #Loads Actions from text files
    actions = loadAction(debug)
    targets = loadTarget(debug)

    #Finds which action is needed
    action = next((word for word in text if word in actions), None)

    match action:
        case "open":
            open(debug, "".join(text[text.index(action) + 1:]).strip(string.punctuation))
            return
        case "explain":
            # Find target and search WikiAPI to find associated article, return summary, and read it with TTS
            position = text.index(action) + 1
            wikiAPI(debug, " ".join(text[position:]).strip(string.punctuation), 0)
            return
        case "search":
            position = text.index(action) + 1
            if text[position] == 'for':
                position += 1
            search(debug," ".join(text[position:]))
            return
    print("No Action Found")
