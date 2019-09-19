from gtts import *
from playsound import playsound
t=gTTS('hello how r u')
t.save('speak.mp3')
playsound('speak.mp3')
