from pocketsphinx import LiveSpeech

for phrase in LiveSpeech():
    # audio_device=200
    # sampling_rate=2000
    print((phrase))


# import datetime
# date= datetime.datetime.today().strftime('%d/%m/%Y')
