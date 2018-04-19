import speech_recognition as sr
from gtts import gTTS
import os
import serial
import time

conn = serial.Serial('COM4', 9600)
r = sr.Recognizer()
with sr.Microphone() as source:
    print("I'm listenning")
    audio = r.listen(source)

print("You: " + r.recognize_google(audio) + "\n")

if r.recognize_google(audio) == 'light up':
    tts = gTTS(text='Turning lights on!', lang='en')
    tts.save("on.mp3")
    os.system("on.mp3")
    conn.write(b'2')
