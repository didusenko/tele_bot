import telebot
bot = telebot.TeleBot("899922977:AAG1ZDDF7byjl96pPZIqS_yB37t8us0n_Fs")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я твой личный бот\n' + '\n' + 'Чем могу помочь?')
    msg = bot.send_message(message.chat.id, '/help - список доступных комманд')
    markup = telebot.types.InlineKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text='help', switch_inline_query_current_chat='/help')
    markup.add(button_1)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)

bot.polling(none_stop=True, interval=0)