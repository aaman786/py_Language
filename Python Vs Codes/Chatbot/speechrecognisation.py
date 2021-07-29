# not working good
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate',180) #for slow down the speed of speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
r = sr.Recognizer()

# speak("As Salamu Aleikum sir. Your voice had deen recognised as an Admin. How are you. As admin you can also take over on me as an Pivate mode. So, Can I switch to Admin mode?")

# with sr.Microphone() as source:
#     while True:
        
#         audio = r.listen(source,timeout=1, phrase_time_limit=5)
#         print(r.recognize_sphinx(audio))

def taking_command():  # This will take the speech and fetch it on google and give the text form of speech
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("listening sir!")
            print("Listening....")
            r.energy_threshold = 900
            r.pause_threshold = 0.5
            audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            speak("Fetching information from google.")
            print("***Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Your speech: {query}")

        except Exception as e:
            # print(e)                             
            # speak("Sorry sir, Network problem. Please say the speech again.")
            print("There is a problem in recognising your speech.")
            return "None"
        # query = query.lower()
        return query

if __name__ == '__main__':
    taking_command()