import sounddevice as sd
from scipy.io.wavfile import write

def audioRec():
    #Audio Specs
    SAMPLE_RATE = 44100
    DURATION = 3
    FILENAME = "tmp.wav"

    #Record Audio
    print("Recording...")
    try:
        audio_data = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
        sd.wait()
    except Exception as e:
        print("Error: ", e)

    #Write audio down as .wav file
    print("Writing to file...")
    try:
        write(FILENAME, SAMPLE_RATE, audio_data)
    except Exception as e:
        print("Error: ", e)

    print("Done.")