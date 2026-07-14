import json

def loadAction(debug):
    with open('actions', 'r') as file:
        actions = file.read().splitlines()
        if debug: print(f"Actions:  {actions}")

    return actions


def loadTarget(debug):
    with open('links.json', 'r') as file:
        targets = json.load(file)
        if debug: print(f"Targets:  {targets}")

    return targets