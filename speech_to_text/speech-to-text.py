import pyaudio
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Sag etwas!")
    audio = r.listen(source)

try:
    print("Du sagtest " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Konnte dich nicht verstehen")
except sr.RequestError as e:
    print("Konnte die Abfrage nicht senden; {0}".format(e))