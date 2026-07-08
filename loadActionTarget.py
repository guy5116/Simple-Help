def loadAction(debug):
    with open('actions', 'r') as file:
        actions = file.read().splitlines()
        if debug: print(actions)

    return actions


def loadTarget(debug):
    with open('targets', 'r') as file:
        targets = file.read().splitlines()
        if debug: print(targets)

    return targets