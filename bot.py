import random
import telebot
from telebot import types

TOKEN = "8056712660:AAG9NrJZTTaKfApL1JudjDXBsFfjekDFn4M"
bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
# 
#     btm1 = types.KeyboardButton("lets play a game❗")
#     btm2 = types.KeyboardButton("say a joke (because i am bored)")
# 
#     markup.add(btm1,btm2)
#     bot.reply_to(message, "hi what i can help you with? and if you want to play a hard game type /game")
#     reply_markup=markup
# 
# 
# @bot.message_handler(commands=['game'])
# def start_game(message):
#     msg = bot.send_message(message.chat.id, " ok👍 guess my number between 1 and 100")
#     bot.register_next_step_handler(msg, check_guess)
# 
# def check_guess(message):
#     secret_number = random.randint(1, 100)
#     user_guess = int(message.text)
#     for i in range(i==0,i=i+1)
#     if user_guess == secret_number:
#         bot.reply_to(message, "you guessed my number")
# 
#         if user_guess  >= secret_number:
#             bot.reply_to(message, "the number is too high try lower")
# 
#         if user_guess <= secret_number:
#             bot.reply_to(message, "the number is too low try high")
# 
#     else:
#         bot.reply_to(message, "try again")
# 
# def joke(message):
#     a=["nah","i am bad at jokes","nope","what do you call someone without a body and a nose? nobodynose🤣","nuh uh"]
# 
#     joke_reply = random.choice(a)
#     bot.reply_to(message,joke_reply)
# 
#


import random
import telebot
from telebot import types

TOKEN = "8056712660:AAG9NrJZTTaKfApL1JudjDXBsFfjekDFn4M"
bot = telebot.TeleBot(TOKEN)

# խաղերի պահոց
games = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btm1 = types.KeyboardButton("lets play a game❗")
    btm2 = types.KeyboardButton("say a joke (because i am bored)")

    markup.add(btm1, btm2)

    bot.send_message(
        message.chat.id,
        "hi 👋 what can i help you with?\nif you want to play the game type /game",
        reply_markup=markup
    )

@bot.message_handler(commands=['game'])
def start_game(message):
    games[message.chat.id] = {
        "number": random.randint(1, 100),
        "tries": 7
    }

    msg = bot.send_message(
        message.chat.id,
        "🎮 I picked a number between 1 and 100\nYou have 7 tries. Send your guess!"
    )
    bot.register_next_step_handler(msg, check_guess)

def check_guess(message):
    chat_id = message.chat.id

    if chat_id not in games:
        bot.reply_to(message, "type /game to start again")
        return

    if not message.text.isdigit():
        msg = bot.reply_to(message, "send a NUMBER between 1 and 100!")
        bot.register_next_step_handler(msg, check_guess)
        return

    user_guess = int(message.text)

    if user_guess < 1 or user_guess > 100:
        msg = bot.reply_to(message, "number must be between 1 and 100!")
        bot.register_next_step_handler(msg, check_guess)
        return

    game = games[chat_id]
    secret_number = game["number"]
    game["tries"] -= 1

    if user_guess == secret_number:
        bot.reply_to(message, "🎉 u guessed my number!!!")
        del games[chat_id]
        return

    if game["tries"] == 0:
        bot.reply_to(
            message,
            f"😢 no tries left! my number was {secret_number}\nType /game to play again"
        )
        del games[chat_id]
        return

    if user_guess > secret_number:
        msg = bot.reply_to(
            message,
            f"⬇️ too high! tries left: {game['tries']}"
        )
    else:
        msg = bot.reply_to(
            message,
            f"⬆️ too low! tries left: {game['tries']}"
        )

    bot.register_next_step_handler(msg, check_guess)

@bot.message_handler(func=lambda message: message.text == "say a joke (because i am bored)")
def joke(message):
    jokes = [
        "Why don’t programmers like nature? 🌳 Because it has too many bugs 🐛",
        "I told my computer I needed a break… now it won’t stop sending me KitKat ads 😅",
        "Why did the programmer quit his job? Because he didn’t get arrays 😂",
        "What do you call someone without a body and a nose? Nobodynose 🤣",
        "I’m not lazy, I’m just on energy-saving mode 😎"
    ]

    bot.reply_to(message, random.choice(jokes))

print("i am awake type something")

bot.infinity_polling(timeout=60, long_polling_timeout=5)
