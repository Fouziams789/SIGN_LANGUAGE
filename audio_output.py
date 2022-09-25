from gtts import gTTS
import pygame
import time
import os

def text_to_speech(text,cnt):
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    file1 = str(text + str(cnt) + ".mp3") #Yes11.mp3
    # myobj.save('detection_sound.mp3')
    myobj.save(file1)
    pygame.init()
    # pygame.mixer.music.load('detection_sound.mp3')
    pygame.mixer.music.load(file1)
    pygame.mixer.music.play()
    time.sleep(1)