import random
import telebot
from telebot import types

TOKEN = "8056712660:AAG9NrJZTTaKfApL1JudjDXBsFfjekDFn4M"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    btm1 = types.KeyboardButton("lets play a game❗")
    btm2 = types.KeyboardButton("say a joke (because i am bored)")

    markup.add(btm1,btm2)
    bot.reply_to(message, "hi what i can help you with? and if you want to play a hard game type /game")
    reply_markup=markup


@bot.message_handler(commands=['game'])
def start_game(message):
    msg = bot.send_message(message.chat.id, " ok👍 guess my number between 1 and 100")
    bot.register_next_step_handler(msg, check_guess)

def check_guess(message):
    secret_number = random.randint(1, 100)
    user_guess = int(message.text)
    try:
        if user_guess == secret_number:
            bot.reply_to(message, "you guessed my number")


    except ValueError:
         bot.reply_to(message, "type a number not a letter or something like that")

    if user_guess  >= secret_number:
        bot.reply_to(message, "the number is too high try lower")

    if user_guess <= secret_number:
        bot.reply_to(message, "the number is too low try high")

def joke(message):
    a=["nah","i am bad at jokes","nope","what do you call someone without a body and a nose? nobodynose🤣","nuh uh"]

    joke_reply = random.choice(a)
    bot.reply_to(message,joke_reply)

# def handle_text(message):


@bot.message_handler(content_types=['text'])
def answer(message):
    answers = [
        "doctor",
        "programmer",
        "who even are you?",
        "who are you?",
        "what do you mean?"
    ]

    reply = random.choice(answers)
    bot.reply_to(message, reply)

print("i am awake type something")



bot.infinity_polling(timeout=60, long_polling_timeout=5)