import random
import types

import telebot

TOKEN = '8273871050:AAEMKpHAiqv0N5lJtcBI_YxvRr7foLq9nzg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("GAMES")
    btn2 = types.KeyboardButton("Guess my future")

    markup.add(btn1, btn2)

    bot.reply_to(message,"Hi! Ask me anything and i will predict yor future\nOr type /game to play!.",
                 reply_markup=markup)


def start_game(message):
    msg = bot.send_message(message.chat.id, " Guess a number between 1 and 10:")
    bot.register_next_step_handler(msg, check_guess)


def check_guess(message):
    secret_number = random.randint(1, 10)
    if message.text.isdigit():
        user_guess = int(message.text)
        if user_guess == secret_number:
            bot.reply_to(message, "Correct!")
        else:
            bot.reply_to(message, "Wrong! It was {secret_number}.")
    else:
        bot.reply_to(message, "That's not a number!")



    bot.reply_to(message, "Welcome! I'm here to help you!" )



@bot.message_handler(content_types=['text'])
def magic(massage):
    answers = [
        "yes",
        "no",
        "maybe",
        "i will think",
    ]
    reply =  random.choice(answers)
    bot.reply_to(massage, reply)

@bot.message_handler(commands=['game'])
def start_game(message):
    msg = bot.send_message(message.chat.id, "🎲 Guess a number between 1 and 10:")
    bot.register_next_step_handler(msg, check_guess)

def check_guess(message):
    secret_number = random.randint(1, 10)
    try:
        user_guess = int(message.text)
        if user_guess == secret_number:
            bot.reply_to(message, "🎉 Correct!")
        else:
            bot.reply_to(message, f"❌ Wrong! It was {secret_number}.")
    except ValueError:
        bot.reply_to(message, "⚠️ Please send a number!")


print("Bot is ready to help with!")
bot.infinity_polling(timeout=60, long_polling_timeout=5)