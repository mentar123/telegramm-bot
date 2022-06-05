import os
import telebot

API_KEY = os.getenv('api-key')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])

def greet(message):
  bot.reply_to(message,'how are you ?')

bot.polling()