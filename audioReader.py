from findAction import findAction
from audioTranscribe import audioTranscribe
from audioRec import audioRec


def audioReader(debug):
    #Record Audio and Convert it to an array
    audioRec()
    text = audioTranscribe().lower().split()

    #Search for action and find correct case
    findAction(debug, text)
