import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

response_pairs = [
            ["my name is (.*)",speak(["As Salamu Aleikum %1. How are you?"])],
            ["I am Aaman", ["Your voice had deen recognised as an Admin. As Salamu Aleikum sir. How are you. As admin you can also take over on me as an Pivate mode. So, Can I switch to Admin mode?"]],
        ]