import settings
import speech_recognition as sr
#https://realpython.com/python-speech-recognition/

def listen_for_speech(microphone, speechrecognizer):
    with microphone as source:
        #speechrecognizer.adjust_for_ambient_noise(source)
        audio = speechrecognizer.listen(source)

    return audio

def speech_transcript_api(audio, speechrecognizer):
    response = {
        "success": True,
        "error": None,
        "transcript": None
        }
    
    try:
        response["transcript"] = speechrecognizer.recognize_wit(audio, settings.WITKEY)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "Can't reach API"
    except sr.UnknownValueError:
        response["error"] = "Speech Unrecognizable"

    return response


def sharon_voicerecognition():
    mic = sr.Microphone()
    r = sr.Recognizer()

    audio = listen_for_speech(mic,r)
    response = speech_transcript_api(audio,r)
        
    if not response["error"]:
        if response["transcript"]:
            return response["transcript"]
