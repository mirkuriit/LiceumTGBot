import telebot
from markups.timetable_markup import markup
global timatable_picture


bot = telebot.TeleBot('5730707714:AAEsGA4qxpTvBG0ycqgPZG_KNfTBExL2i-0')


def get_class(message):
    print(get_class)
    class_number = int(message.text)
    bot.send_message(message.from_user.id, "Укажите свое имя")
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    name = message.text
    bot.send_message(
        message.from_user.id,
        f"Привет, {name}, если ты читаешь это, твоя мать умрет через пять минут",
        reply_markup=markup
    )




@bot.message_handler(commands=['start', 'help'])
def index(message):
    print("index")
    bot.reply_to(message, f"Приветствуем тебя, {message.from_user}, в нашем уютном лицее")


@bot.message_handler(content_types=["text"])
def get_text_message(message):
    print("get_text_message")
    if message.text.lower() == "/registration":
        bot.send_message(message.from_user.id, "Укажите свой класс")
        bot.register_next_step_handler(message, get_class)
    elif message.text.lower() == "дай расписание шаболда":
        timatable_picture = open("timetable.jpg", "rb")
        bot.send_photo(message.from_user.id, timatable_picture)


@bot.edited_message_handler(content_types=["text"])
def say_about_edit_message(message):
    print("get_text_message")
    bot.send_message(message.from_user.id, f"Вы отредактировали {message.text}")



bot.infinity_polling()

