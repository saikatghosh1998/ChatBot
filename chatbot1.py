from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('DemoBot')
bot.set_trainer(ListTrainer)

for _file in os.listdir('botfiles'):
    chats=open('botfiles/'+_file,'r').readlines()
    bot.train(chats)
    
while True:
    request=input('you: ')
    response=bot.get_response(request)
    print('Bot: ',response)