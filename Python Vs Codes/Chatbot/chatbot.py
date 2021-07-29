from nltk.chat.MineModule.util1 import Chat, reflections

# from chatbotResponse import response_pairs as 

pairs = [
    ["Recognise Me",["I had recognise ypou has an Admin, So giving your information."]],
    ["My name is (.*)", ["As Salamu Aleikum %1. I am Alisha an AI."]],
    ["what is it",["sorry, What is what? if you need to ask something ask in the pattern, What is dash?"]],
    ["tell me about ai?|what is  an ai?|what is ai|what was ai?|ai waht?",["Ai generally stans for Artificial Intelligence. It gives an a smart and own thinking to machine or device"]],
    ["Myself (.*)", ["As Salamu Aleikum %1. I am Alisha an AI."]],
    ["Nice|Beautiful", ["Thank You"]],
    ["how are you?|what about you?",["I am good. And what about you?"]],
    ["I am also good|i am good|good|Fine|i am fine|I am also fine",["That's Great!"]],
    ["what are you doing?| what do you used to do?", ["what do you think? What could I have to do?"]],
    ["Nothing|Nothing, I am just asking.|i am just asking",["oky! I had many works here."]],
    ["what's up?|whatup|what up|what app|whatapp|What'sapp|whatsapp|whats app|what's app|what's up|Whatsgoing on?",["Nothing, And what about you?"]],
    ["making a talk with you|talking with you","Good"],
    ["Tell about Cpu|tell about performance of cpu|what about the peerformance of cpu|How was the perrformance of cpu","Not yet Developments"],

    ["Who are ?|introduce yourself|speak about you", ["I am Alisha and I am a AI bot which is made using some advance modules and libraries to talk like an human."]],

    ["oky|Alright|Good", ["Alright","Good","Okk"]],
    ["I want an recognization as Admin|recognize me|i want recognization as admin|recognize me as an admin", 
    ["As Salamu Aleikum sir, Your voice had deen recognised as an Admin. . How are you?."]],
    ["Who am I|recognize me", ["You are the one who created me."]]
    # [, []],
]


def firstChatBot():
    print("Chat Bot using the nlt module")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()


if __name__ == '__main__':
    firstChatBot()
