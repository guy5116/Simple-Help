import pyttsx3

#Read text aloud and stop engine if their is an error
def readText(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(e)
        engine.stop()
        return
