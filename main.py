import telebot
from flask import Flask
from threading import Thread

# BotFather wala Token yahan dalo
TOKEN = '8662309343:AAFwuG4qs1ebTLNCqn8zZkIpFJuLVUvPJmg'
bot = telebot.TeleBot(TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Syed Cheats VIP Bot is Online!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salam Syed Jani! Bot Live hai Render par. 🚀\n\nAbhi main mazeed features add kar raha hoon.")

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.infinity_polling()
