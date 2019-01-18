from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot =  ChatBot('Test')

bot.set_trainer(ListTrainer)

#conv = open('chat.txt' ,'r').readline()
for conv in os.listdir('conv_file'):
    chats = open('conv_file/' + conv ,'r').readline()
    bot.train(chats)

#bot.train(conv)

while True:
    user_req = input('You : ')
    bot_rsp = bot.get_response(user_req)

    print('Bot : ',bot_rsp)