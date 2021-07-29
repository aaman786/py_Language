# from pocketsphinx import LiveSpeech

# for phrase in LiveSpeech():
#     # audio_device=200
#     sampling_rate=2000
#     print((phrase))


# # import datetime
# # date= datetime.datetime.today().strftime('%d/%m/%Y')

import pyttsx3
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Who are you")