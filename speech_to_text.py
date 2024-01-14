# speech_recognition_module.py
from vosk import Model, KaldiRecognizer
import pyaudio

# Initialisiere das Vosk-Modell als globalen Parameter
MODEL_PATH = r"C:\Gebaerdenstuff\vosk-model-small-de-zamia-0.3"
MODEL = Model(MODEL_PATH)
RECOG = KaldiRecognizer(MODEL, 16000)

def speech_to_text():
    print('start.py - using preloaded model')

    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        if RECOG.AcceptWaveform(data):
            return RECOG.Result().split(('"'))[3]

if __name__ == "__main__":
    # Beispielcode hier hinzufügen
    pass