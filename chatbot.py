from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/Ayush/Desktop/test/english/'):
	data = open('C:/Users/Ayush/Desktop/test/english/'+ files,'r').readlines()
	bot.train(data)
	
while True:
	message=input('You:')
	if message.strip()!='bye':
		reply=bot.get_response(message)
		print('chatbot:',reply)
	if message.strip()=='bye':
		print('chatbot: Bye')
		break
