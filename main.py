import telebot
from markups.timetable_markup import markup
import re
global timatable_picture

bot = telebot.TeleBot('5730707714:AAEsGA4qxpTvBG0ycqgPZG_KNfTBExL2i-0')


def get_class(message):
    print(get_class)
    if is_correct_class(message.text):
        bot.send_message(message.from_user.id, "Чего тебе надобно?", reply_markup=markup)
        #bot.register_next_step_handler(message, choose_action)
    else:
        bot.send_message(message.from_user.id, "Некорректный класс. Попробуйте еще раз")
        bot.register_next_step_handler(message, get_class)


def choose_action(message):
    pass
    #bot.send_message(message.from_user.id, "Чего тебе надобно?", reply_murkup=markup)


def is_correct_class(user_class):
    if len(user_class) > 3:
        return False
    else:
        if len(user_class) == 3:
            pattern = r'1[0-1][А-Ва-в]'
            return True if re.fullmatch(pattern, user_class) else False
        else:
            pattern = r'[8-9][А-Ва-в]'
            return True if re.fullmatch(pattern, user_class) else False


@bot.message_handler(commands=['start', 'help', 'reg'])
def index(message):
    match message.text:
        case "/start":
            bot.reply_to(message, f"Приветствуем тебя, {message.from_user.username}, "
                                  "в нашем уютном лицее. Для "
                                  "продолжения используй /reg")
        case "/help":
            bot.send_message(message.from_user.id, "Тут будут все команды")
        case "/reg":
            bot.send_message(message.from_user.id, "Укажите свой класс в формате ЦифраБуква "
                                                   "(Например, 9А)")
            bot.register_next_step_handler(message, get_class)



@bot.message_handler(content_types=["text"])
def get_text_message(message):
    print("get_text_message")
    if message.text.lower() == "дай расписание шаболда":
        timatable_picture = open("timetable.jpg", "rb")
        bot.send_photo(message.from_user.id, timatable_picture)


@bot.edited_message_handler(content_types=["text"])
def say_about_edit_message(message):
    print("get_text_message")
    bot.send_message(message.from_user.id, f"Вы отредактировали {message.text}")



bot.infinity_polling()

