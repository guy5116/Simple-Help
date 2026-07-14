from faster_whisper import WhisperModel

#Use Faster Whisper to convert audio to text and return it
def audioTranscribe():
    model = WhisperModel("base", device="cpu")

    segments, info = model.transcribe("tmp.wav")



    for segment in segments:
        return segment.text