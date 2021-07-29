import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

# print(voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am David, How can I help you?")


def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am Listening...")
        print("Listening....")
        r.energy_threshold=1100
        r.pause_thresold = 0.5
        audio = r.listen(source)

    try:
        print("Reconitizing....")
        query = r.recognize_google(audio)
        print(f"User Speach: {query}\n")

    except Exception as e:
        # print(e) this will print an error
        speak("Sorry Sir, You had to say that again. I am facing Network Problem")
        print("say that again, please...")
        return "None"
    return query


if __name__ == "__main__":
    # wish()
    take_commands()
