import pyttsx3
import sys

args = sys.argv
actual_args = args[2:]
rate = int(args[1])

print(f"#oneone({rate}): " + ' '.join(actual_args))

def text_to_speech(text):
    engine = pyttsx3.init()
    global rate
    engine.setProperty('rate', rate)  # You can experiment with different values

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('pitch', 0.9)
    engine.say(text)
    engine.runAndWait()


text_to_speech(' '.join(actual_args))