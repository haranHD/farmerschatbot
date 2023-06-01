import pyttsx3
from googletrans import Translator
import datetime
import pywhatkit
import pymongo as go

a = go.MongoClient("mongodb://localhost:27017/")

data = a.chat1
col = data.bot1
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",140)
trans = Translator()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def call():

    mydata = col.find()
    user_input = input("YOU :")
    for i in mydata:
        if "good soil for paddy" in user_input:
            print("BOT :", i["q2"])
            talk(i["q2"])
        elif "correct time for planting paddy" in user_input:
            print("BOT :", i["q3"])
            talk(i["q3"])
            talk(i["q3"])
        elif "plant a crop" in user_input:
            print("BOT :", i["q1"])
            talk(i["q1"])
        elif 'time' in user_input:
            time = datetime.datetime.now().strftime("%H : %M %p")
            print("BOT :",time)
            talk(time)
        elif "best condition for growing onions in TN" in user_input:
            print("BOT :",i["q5"])
            talk(i["q5"])
        elif "pest control in maize" in user_input:
            print("BOT :",i["q6"])
            talk(i["q6"])
        elif "manure for coconut tree" in user_input:
            print("BOT :",i["q7"])
            talk(i["q7"])
        elif "sugarcane need high rainfall" in user_input:
            print("BOT :",i["q8"])
            talk(i["q8"])
        elif "okay bye" in user_input:
            bye=print("BOT :BYEE")
            talk(bye)
        elif "play" in user_input:
            song = user_input.replace("play", ' ')
            talk("playing" + song)
            pywhatkit.playonyt(song)
            print("Playing video")
while True:
    call()