from vosk import Model, KaldiRecognizer
import pyaudio


def speech_to_text():
    print('start.py - start loading model')
    #model = Model(r"D:\Dokumente\Schule\Klasse 10\Franzosisch\forschung\vosk-model-de-0.21")
    model = Model(r"D:\Dokumente\Schule\Klasse 10\Franzosisch\forschung\vosk-model-small-de-zamia-0.3")
    recog = KaldiRecognizer(model, 16000)
    print("start.py - loaded model successfully")

    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        if recog.AcceptWaveform(data):
            
            return(recog.Result().split(('"'))[3])


