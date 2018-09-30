import speech_recognition as sr
import speak
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


bot=ChatBot('Bot')
bot.set_trainer(ListTrainer)
r=sr.Recognizer()


try:
    while True:
        with sr.Microphone() as source:
            print('Say Something !')
            audio=r.listen(source)
            print('Done!')
        try:
            message=r.recognize_google(audio)
            print('Google thinks you said:\n' + message)
            if message!='bye':
                reply=bot.get_response(message)
                print('chatbot:',reply)
                reply1=str(reply)
                speak.tts(reply1,'en')
            if message=='bye':
                print('chatbot: Bye')
                speak.tts('bye','en')
                break
        except Exception as e:
            print('exception') 
            print(e)    
except Exception as e:
    print('exception 2')
    print(e)
