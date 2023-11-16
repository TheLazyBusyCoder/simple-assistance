import soundcard as sc
import soundfile as sf
import speech_recognition as sr
import subprocess 
import warnings
import os
import time

warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")


class SpeechRecognizer:
    def __init__(self, mic_index=0, samplerate=16000, duration=5):
        self.mics = sc.all_microphones(include_loopback=True)
        self.selected_mic = self.mics[mic_index]
        self.samplerate = 16000
        self.temp_audio_file = "temp_audio.wav"

    def record_audio(self , duration):
        numframes = int(duration * self.samplerate)
        with self.selected_mic.recorder(samplerate=self.samplerate) as mic:
            print("Recording...")
            audio = mic.record(numframes)
            print("Done.")
            sf.write(self.temp_audio_file, audio[:], self.samplerate)

    def recognize_speech(self):
        r = sr.Recognizer()
        try:
            with sr.AudioFile(self.temp_audio_file) as source:
                audio_data = r.record(source)
                return r.recognize_google(audio_data)
        except sr.UnknownValueError:
            print("Could not understand audio")
            return -1
        except sr.RequestError as e:
            return "Error: {0}".format(e)

    def speak(self ,text , rate = 160):
        command = f'python speak.py {rate} {text}'
        subprocess.run(command, shell=True)
    
    def takequery(self):
        self.record_audio(5)
        text = self.recognize_speech()
        return text


oneone = SpeechRecognizer(mic_index=3, samplerate=16000, duration=5)

os.system('cls')
oneone.speak("Program started")
while True:
    query = oneone.takequery()
    if query == -1:
        continue
    print("#query: " + str(query))
    time.sleep(1)

    parts = query.split(maxsplit=1)
    if len(parts) >= 2 and parts[0].lower() == "calculate":
        expression_to_calculate = parts[1]
        import mathh
        Math = mathh.Math()
        Math.calculate_expression(expression_to_calculate, oneone)
    elif len(parts) >= 2 and parts[0].lower() == "open":
        x = parts[1].replace("and search for ", "")
        import openn
        openn.open_youtube(x)
    elif "exit" in query.lower():
        oneone.speak("shutting down....")
        break
    elif "Wikipedia".lower() in query.lower():
        import wikiClass
        wikiclass = wikiClass.Wiki()
        wikiclass.start(oneone)
    elif "joke" in query.lower():
        import pyjokes
        joke = pyjokes.get_joke(language='en', category='all')
        oneone.speak(joke , 140)




