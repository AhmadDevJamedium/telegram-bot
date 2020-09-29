import telebot
import time
import random

pi = '3.1415926535897932384626'
bot_token = 'Place your Token here'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')

@bot.message_handler(commands=['pi'])
def send_pi(message):
    for d in pi:
        bot.reply_to(message, d)
        time.sleep(2)

@bot.message_handler(commands=['help'])
def send_start(message):
    bot.reply_to(message, "Welcome! This is the test \ntelegram bot from Ahmad\nYou can use the following commands:\n/fakemessage{number of fake messages 0-5}\n/pi\n/help")

@bot.message_handler(commands=['fakemessage1'])
def send_1_fake_message(message):
    for _ in range(1):
        bot.reply_to(message, "This is a fake message, don't show it to anyone")
        time.sleep(random.randint(1, 20))

@bot.message_handler(commands=['fakemessage2'])
def send_2_fake_messages(message):
    for _ in range(2):
        bot.reply_to(message, "This is a fake message, don't show it to anyone")
        time.sleep(random.randint(1, 20))

@bot.message_handler(commands=['fakemessage3'])
def send_3_fake_messages(message):
    for _ in range(3):
        bot.reply_to(message, "This is a fake message, don't show it to anyone")
        time.sleep(random.randint(1, 20))

@bot.message_handler(commands=['fakemessage4'])
def send_4_fake_messages(message):
    for _ in range(4):
        bot.reply_to(message, "This is a fake message, don't show it to anyone")
        time.sleep(random.randint(1, 20))

@bot.message_handler(commands=['fakemessage5'])
def send_5_fake_messages(message):
    for _ in range(5):
        bot.reply_to(message, "This is a fake message, don't show it to anyone")
        time.sleep(random.randint(1, 20))

bot.polling()
