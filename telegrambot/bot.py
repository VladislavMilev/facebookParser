import CONFIG as conf
import telebot
import os

def path(path):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, path)

bot = telebot.TeleBot(conf.API_TOKEN, parse_mode=None)

def send_file_to_telegrambot():
    file = open(path(f'../files/{conf.DATA_FILE}'))
    bot.send_document(chat_id=conf.ID, data=file)
