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

if r.recognize_google(audio) == "can you hear me":
    tts = gTTS(text='Absolutely!', lang='en')
    tts.save("abs.mp3")
    os.system("abs.mp3")
if r.recognize_google(audio) == 'light up':
    tts = gTTS(text='Turning lights on!', lang='en')
    tts.save("on.mp3")
    os.system("on.mp3")
    conn.write(b'2')
if r.recognize_google(audio) == 'turn lights off':
    tts = gTTS(text='Turrning lights off!', lang='en')
    tts.save("off.mp3")
    os.system("off.mp3")
    conn.write(b'3')

if r.recognize_google(audio) == 'thank you':
    tts = gTTS(text='You are welcome!', lang='en')
    tts.save("yaw.mp3")
    os.system("yaw.mp3")

if r.recognize_google(audio) == 'fuck you':
    tts = gTTS(text='Watch your mouth, asshole.', lang='en')
    tts.save("fucku.mp3")
    os.system("fucku.mp3")

