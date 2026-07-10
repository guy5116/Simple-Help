import json

def loadAction(debug):
    with open('actions', 'r') as file:
        actions = file.read().splitlines()
        if debug: print(actions)

    return actions


def loadTarget(debug):
    with open('links.json', 'r') as file:
        targets = json.load(file)
        if debug: print(targets)

    return targets