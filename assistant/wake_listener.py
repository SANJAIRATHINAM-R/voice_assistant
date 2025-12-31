from listener import listen_command
from tts import speak
import speech_recognition as sr

WAKE_WORDS = ["hey darling", "darling"]

def start_wake_listener():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)

    while True:
        with mic as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            if any(w in text for w in WAKE_WORDS):
                speak("Yes darling")
                listen_command()
        except:
            pass
