import telebot
from markups.timetable_markup import timetable_markup, link_markup
import re
from timetable_manager import TimeTableManager

global timatable_picture
from repository import TGBotUserRepository

bot = telebot.TeleBot('5730707714:AAEsGA4qxpTvBG0ycqgPZG_KNfTBExL2i-0')
user_repository = TGBotUserRepository('D:/DBases/liceumTGbot.db')
timetable_manager = TimeTableManager()


def _is_correct_class(user_class_str):
    pattern1011 = r'1[0-1][А-Ва-в]'
    pattern89 = r'[8-9][А-Ва-в]'
    if len(user_class_str) > 3:
        return False
    elif len(user_class_str) == 3:
        return bool(re.fullmatch(pattern1011, user_class_str))
    else:
        return bool(re.fullmatch(pattern89, user_class_str))


def bot_functions_index(message):
    bot.send_message(
        message.from_user.id,
        "Чего тебе надобно?",
        reply_markup=timetable_markup
    )


def get_class(message):
    print("get_class")
    user_class = message.text
    if _is_correct_class(user_class):
        user_repository.set_user_class(message.from_user.id, message.text)
        bot_functions_index(message)
    else:
        bot.send_message(message.from_user.id, "Некорректный класс. Попробуйте еще раз")
        bot.register_next_step_handler(message, get_class)


def get_name(message):
    print("get_name")
    user_name = message.text
    user_repository.add_user(user_name, message.from_user.id)
    bot.send_message(message.from_user.id, "Укажите свой класс в формате ЦифраБуква "
                                            "(Например, 9А)")
    bot.register_next_step_handler(message, get_class)


def edit_class(message):
    user_class = message.text
    if _is_correct_class(user_class):
        user_repository.set_user_class(message.from_user.id, user_class)
    else:
        bot.send_message(message.from_user.id, "Некорректный класс. Попробуйте еще раз")
        bot.register_next_step_handler(message, edit_class)


def edit_name(message):
    user_name = message.text
    user_repository.set_user_name(message.from_user.id, user_name)


def send_lawrence_link(message):
    bot.send_message(message.from_user.id, "Веселого путешествия", reply_markup=link_markup)


@bot.message_handler(commands=['start', 'help', 'reg', 'edit_class', 'edit_name', 'func'])
def index(message):
    user_id = message.from_user.id
    match message.text:
        case "/start":
            bot.reply_to(message, f"Приветствуем тебя, {message.from_user.username}, "
                                  "в нашем уютном лицее. Для "
                                  "продолжения используй /reg")
        case "/help":
            bot.send_message(user_id, "Тут будут все команды")
        case "/reg":
            if user_repository.is_user_exists(user_id):
                bot.send_message(message.from_user.id,
                                 "Вы уже прошли регистрацию. "
                                 "Для изменения профиля используйте команду, которая еще не реализована",
                                 reply_markup=timetable_markup)
            else:
                bot.send_message(user_id, "Введите свое имя")
                bot.register_next_step_handler(message, get_name)
        case "/edit_class":
            if user_repository.is_user_exists(message.from_user.id):
                bot.send_message(user_id, "Введите свой новый класс")
                bot.register_next_step_handler(message, edit_class)
        case "/edit_name":
            bot.send_message(user_id, "Введите новое имя")
            bot.register_next_step_handler(message, edit_name)
        case "/func":
            bot_functions_index(message)


@bot.message_handler(content_types=["text"])
def to_react(message):
    user_id = message.from_user.id
    print("get_text_message")
    match message.text.lower():
        case "дай общее расписание шаболда":
            timetable_picture = open("resourses/timetable.jpg", "rb")
            bot.send_photo(user_id, timetable_picture)
            bot.send_message(user_id, user_repository.get_user_name_by_id(user_id))
        case "дай мое расписание шаболда":
            print(user_id)
            timetable_str = timetable_manager.get_timetable(
                user_repository.get_user_class_by_id(user_id)
            )
            bot.send_message(user_id, timetable_str.values())
        case "пойти нахуй":
            send_lawrence_link(message)


@bot.edited_message_handler(content_types=["text"])
def say_about_edit_message(message):
    print("get_text_message")
    bot.send_message(message.from_user.id, f"Вы отредактировали {message.text}")



bot.infinity_polling()

