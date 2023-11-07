from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r"C:\Gebaerdenstuff\vosk\vosk-model-de-0.21") 
recog = KaldiRecognizer(model, 16000)
print("done")

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if len(data) == 0:
        break
    if recog.AcceptWaveform(data):
        print(recog.Result())

