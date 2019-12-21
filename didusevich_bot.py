import telebot

bot = telebot.TeleBot("*************************************")

link1 = 'https://my.tec.cn.ua/wb4tecls/login/auth'
link2 = 'https://stat.water.cn.ua/wb2abvdk/login/auth'
link3 = 'https://chernigivoblenergo.com.ua/abon_cabinet/'

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text='Начать!!!', callback_data='main_page')
    markup.add(button_1)
    bot.send_message(message.chat.id, text='Привет Хозяин! Я твой личный помощник', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def process_callback(call):
    if call.data == 'main_page':
        markup = telebot.types.InlineKeyboardMarkup()
        button_0 = telebot.types.InlineKeyboardButton(text='Главная Страница', callback_data='main_page')
        button_1 = telebot.types.InlineKeyboardButton(
            text='Передать показания счетчиков (вода, електричество)', callback_data='btm1')
        markup.add(button_0)
        markup.add(button_1)
        bot.send_message(
            call.message.chat.id, text='Преветствую в главном меню, Выберите нужное действие!', reply_markup=markup)

    elif call.data == 'btm1':
        markup = telebot.types.InlineKeyboardMarkup()
        button_0 = telebot.types.InlineKeyboardButton(text='Главная Страница', callback_data='main_page')
        button_1 = telebot.types.InlineKeyboardButton(text='Обленерго', url=link1)
        button_2 = telebot.types.InlineKeyboardButton(text='Водоканал', url=link2)
        button_3 = telebot.types.InlineKeyboardButton(text='Тец', url=link3)
        markup.add(button_0)
        markup.add(button_1, button_2, button_3)
        bot.send_message(call.message.chat.id, text='Выберите нужный ресурс:', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
