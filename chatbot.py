import random
import telebot
from telebot import types

TOKEN = '8584678330:AAGCAIPAhqsVG_g4MfxeRGGdcZV3SV-oPfo'

bot  = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("Play Game🎲")
    btn2 = types.KeyboardButton("Predict Future🔮")
    btn3 = types.KeyboardButton("Send a cute cat photo🐱")

    markup.add(btn1, btn2 , btn3)

    bot.reply_to(message, text = "Hello, we can chat, predict future.\nOr type /game to play, or /send a cute cat photo.", reply_markup=markup)




def start_game(message):
        msg = bot.send_message(message.chat.id, "🎶guess a number between 1 n' 10.")
        bot.register_next_step_handler(msg, check_guess)

def check_guess(message):
        secret_number = random.randint(1, 10)
        if message.text.isdigit():
            user_guess = int(message.text)
            if user_guess == secret_number:
                bot.reply_to(message, "You guessed correctly!")
            else:
                bot.reply_to(message, f"Wrong , it was {secret_number}")
        else:
            bot.reply_to(message, "not a num.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Play Game🎲":
        start_game(message)

    elif message.text == "Predict Future🔮":
        answers = ["Yes, definitely!", "Sure", "Okay"]
        reply = random.choices(answers)
        bot.reply_to(message, reply)


    elif message.text == "Send a cute cat photo🐱":
        bot.send_message(message.chat.id, "Looking for a cat... 🐾")
        bot.send_photo(
            message.chat.id,
            photo="https://placekitten.com/400/300"
        )


    else:
        replies = ["idk u", "I see", "try clicking a btn"]
        bot.reply_to(message, random.choice(replies))


# @bot.message_handler(content_types=['text'])
# def magic(message):
#     answers = [
#         "yes",
#         "no",
#         "maybe",
#         "idk u",
#         "sorry?",
#         "idk",
#         "hello"
#     ]
#     reply = random.choice(answers)
#     bot.reply_to(message, reply)

print("---------------------------------------------------")
print("Bot is ready to help >_<")
print("---------------------------------------------------")
bot.infinity_polling(timeout=60, long_polling_timeout=5)
