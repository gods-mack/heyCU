import speech_recognition as sr
from gtts import gTTS
import os



def speak(text):
    """ Convert the 'text' in audio, stores it in s'ound/audio.mp3' 
    and plays it through terminal. """
    tts = gTTS(text, 'en-IN')
    tts.save('sound/audio.mp3')
    os.system("mpg123 sound/audio.mp3")
    
def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
      r.pause_Threshold = 2
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source)

    return r.recognize_google(audio)




          		







