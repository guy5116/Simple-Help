from loadActionTarget import *
import webbrowser
from fuzzywuzzy import process
import string


def open(debug, target):
    targets = loadTarget(debug)

    # Find target in array and loads website based on the target
    best_match = process.extractOne(target, targets)
    if target == 'None':
        print("NULL Target")
        return
    print(f"The Action is Open and the Target is {target}")
    webbrowser.open(best_match[0])
    if debug: print(f"Score is {best_match[1]}")
    return

