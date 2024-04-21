from telebot import types
import telebot
token = '6745774274:AAETb5EcKXrs_rJAlyNfU3wkrvfuo3PQwTM'


bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_dice(message.chat.id)
    bot.send_message(message.chat.id, "Привет, я родился! ")
    bot.send_message(message.chat.id, "Если хочешь узнать список команд, которые я умею, напечатай /help")

@bot.message_handler(commands = ['help'])
def help_message(message):
    bot.send_message(message.chat.id, "/main - основной сайт студентов ФПМИ ")
    bot.send_message(message.chat.id, "/inst - инстаграмм студентов ФПМИ ")
    bot.send_message(message.chat.id, "/tiktok - тикток студентов ФПМИ ")
    bot.send_message(message.chat.id, "/science - тг научки")
    bot.send_message(message.chat.id, "/news - тг с новостями ФПМИ")

@bot.message_handler(commands=['menu'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
    button_phone = types.KeyboardButton(text = "Отправить номер телефона", reques_contact = True)
    button_geo = types.KeyboardButton(text = "Отправить местоположение", request_location = True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местопожением", reply_markup = keyboard)


@bot.message_handler(commands = ['science'])
def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text = "Перейти в телеграмм научки", url = "https://t.me/famcsForTeapots")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми на кнопку и разберись с тем что не понимаешь.", reply_markup = keyboard)

@bot.message_handler(commands = ['news'])
def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text = "Перейти в телеграмм с новостями", url = "https://t.me/dean_fpmi_bsu")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми на кнопку и узнаешь новости про ФПМИ.", reply_markup = keyboard)

@bot.message_handler(commands = ['inst'])
def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text = "Перейти на инсту ФПМИ", url = "https://www.instagram.com/famcs_bsu/?ysclid=lszb2h6vxs763828425")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми на кнопку и пролайкай все посты.", reply_markup = keyboard)

@bot.message_handler(commands = ['tiktok'])
def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text = "Перейти на тикток ФПМИ", url = "https://www.tiktok.com/@onlyfamcs")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми на кнопку и залипни на несколько часов.", reply_markup = keyboard)


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
   bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()