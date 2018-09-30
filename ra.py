import speech_recognition as sr
import speak
#from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
import os
import random
def call():
        print('chatbot:',reply)
        reply1=str(reply)
        speak.tts(reply1,'en')
        
r=sr.Recognizer()
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['how are you','How are you?','How are you doing?','how are you doing?']

responses = ["i am fine "]
random_response = random.choice(responses)
a={'good morning':'good morning','good afternoon':'good afternoon','good evening':'good evening','good night':'good night'}





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
                             if message in greetings:
                                     reply=random_greeting
                                     call()
                             elif message in question:
                                     reply=random_response
                                     call()
                             elif message in a:
                                     reply=a[message]
                                     call()
                             else:
                                        print("I did not understand what you said")
                                        error="sorry I did not understand what you said"
                                        speak.tts(error,'en')
                                        

                            
                                
                    else:
                            print('Bye')
                            speak.tts('bye','en')
                            break
                                     
                                     
                                 
                  except Exception as e:
                      print('exception') 
                      print(e)    
except Exception as e:
    print('exception 2')
    print(e)

                
                
