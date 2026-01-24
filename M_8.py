import telebot

TOKEN = "8494397916:AAFhrFO-XyPFVrICCGUUyuJjaFslLSX9nNU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'hello')

    # reply_markup=markup)

print("Bot is awake and listening...")
bot.infinity_polling(timeout=60, long_polling_timeout=5)

@bot.message_handler(commands=['game'])
def start_game(message):
    msg = bot.send_message(message.chat.id, """GUess a number 1 at 10:  """  )
    # bot.register_next_step_handler(msg, check_guess)

