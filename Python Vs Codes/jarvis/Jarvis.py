import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate',168) #for slow down the speed of speech



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():  # This will Greet the user like Good Morning
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour <= 12 and hour > 18:
        speak("Good Morining Sir!")
    else:
        speak("Good Evening Sir!")

    speak("I am Alisha and i am listening sir")


def taking_command():  # This will take the speech and fetch it on google and give the text form of speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening sir!")
        print("Listening....")
        r.energy_threshold = 500
        r.pause_threshold = 0.5
        audio = r.listen(source, timeout=1, phrase_time_limit=3)

    try:
        speak("Fetching information from google.")
        print("***Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Your speech: {query}")

    except Exception as e:
        # print(e)                             
        speak("Sorry sir, Network problem. Please say the speech again.")
        print("There is a problem in recognising your speech.")
        return "None"
    # query = query.lower()
    return query


if __name__ == "__main__": #this will stop the previous(in module) execution. 
    # wish()
    # speak("Wait until the complition.")
    while True:
        command = taking_command().lower()

        if 'time' in command or 'date' in command:
            time = datetime.datetime.now().strftime('%H,%M')
            print("Time")
            speak(f"The current time is {time} \n\n")
            date=datetime.datetime.today().strftime('%d/%m/%Y')
            speak("And the date is: ")

        elif 'wikipedia' in command:
            speak("Searching wkikipedia")
            query = query.replace("wikipedia", "")
            result = query.summary(wikipedia, sentence=2)
            speak("According to the wikipedia")
            print("Result is:- ")
            speak(result)

        elif 'open google' in command:
            webbrowser(chrome).open_new_tab("www.google.com")

        else:
            pass
