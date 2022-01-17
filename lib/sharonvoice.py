from gtts import gTTS
import time
import os
import playsound

def sharonVoice(texttospeak):
    tts = gTTS(text=texttospeak, lang='en', tld='co.uk')
    voiceFile = "data/sharon.mp3"
    tts.save(voiceFile)
    
    time.sleep(1)
    print(texttospeak)
    playsound.playsound(voiceFile)

    os.remove(voiceFile)
