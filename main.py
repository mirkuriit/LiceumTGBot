import telebot

from class_manager import ClassManager
from json_formatter import JsonFormatter
from markups.timetable_markup import timetable_markup, link_markup
from school_manager import SchoolManager
from timtable_timer import TimetableTimer
import re
from timetable_manager import TimeTableManager

global timetable_picture
from repository import TGBotUserRepository


bot = telebot.TeleBot('5730707714:AAEsGA4qxpTvBG0ycqgPZG_KNfTBExL2i-0')
user_repository = TGBotUserRepository('D:/DBases/liceumTGbot.db')
formatter = JsonFormatter()
timetable_manager = TimeTableManager()
class_manager = ClassManager()
school_manager = SchoolManager()
timetable_timer = TimetableTimer()


def _is_correct_sin_class(user_class_str):
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
    if _is_correct_sin_class(user_class):
        if class_manager.is_class_in_db(
                user_repository.get_user_school_id_by_id(message.from_user.id),
                user_class
        ):
            user_repository.set_user_class(message.from_user.id,
                                           class_manager.get_class_id(user_repository.get_user_school_id_by_id(message.from_user.id), user_class)
                                           )
            bot_functions_index(message)
        else:
            bot.send_message(message.from_user.id, "Не могу найти класс. Попробуйте еще раз")
            bot.register_next_step_handler(message, get_class)
    else:
        bot.send_message(message.from_user.id, "Некорректный класс. Попробуйте еще раз")
        bot.register_next_step_handler(message, get_class)


def get_school(message):
    print("get_sсhool")
    user_school = message.text
    if school_manager.is_school_in_db(user_school):
        user_repository.set_user_school(message.from_user.id, school_manager.get_school_id(user_school))
        bot.send_message(message.from_user.id, "Укажите свой класс в формате ЦифраБуква "
                                               "(Например, 9А)")
        bot.register_next_step_handler(message, get_class)
    else:
        bot.send_message(message.from_user.id, "Некорректная школа, попробуйте еще раз")
        bot.register_next_step_handler(message, get_school)


def get_name(message):
    print("get_name")
    user_name = message.text
    user_repository.add_user(user_name, message.from_user.id)
    bot.send_message(message.from_user.id, "Укажите название своего учебного заведения")
    bot.register_next_step_handler(message, get_school)


def edit_class(message):
    #TODO не трогать!!!! не работает
    user_class = message.text
    if _is_correct_sin_class(user_class):
        if class_manager.is_class_in_db(user_repository.get_user_school_id_by_id(message.from_user.id), user_repository.get_user_class_id_by_id(message.from_user.id)):
            user_repository.set_user_class(message.from_user.id,
                                           class_manager.get_class_id(
                                               user_repository.get_user_school_id_by_id(message.from_user.id))
                                           )
            bot_functions_index(message)
        else:
            bot.send_message(message.from_user.id, "Не могу найти класс. Попробуйте еще раз")
            bot.register_next_step_handler(message, get_class)
    else:
        bot.send_message(message.from_user.id, "Некорректный класс. Попробуйте еще раз")
        bot.register_next_step_handler(message, get_class)


def edit_school(message):
    #todo сделать едит скул
    pass


def edit_name(message):
    user_name = message.text
    user_repository.set_user_name(message.from_user.id, user_name)


def send_lawrence_link(message):
    bot.send_message(message.from_user.id, "Веселого путешествия", reply_markup=link_markup)


@bot.message_handler(commands=['start', 'help', 'reg', 'edit_class', 'edit_name', 'edit_school', 'func'])
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
            # отладка bot.send_message(user_id, user_repository.get_user_name_by_id(user_id))
        case "дай мое расписание шаболда":
            print(user_id)
            timetable = timetable_manager.get_timetable(
                user_repository.get_user_class_id_by_id(user_id)
            )
            timetable_human = formatter.convert_json_to_human_ol(timetable)

            bot.send_message(user_id, timetable_human)
        case "до звонка:":
            bot.send_message(user_id, timetable_timer.get_status())
        case "пойти нахуй":
            send_lawrence_link(message)


@bot.edited_message_handler(content_types=["text"])
def say_about_edit_message(message):
    print("get_text_message")
    bot.send_message(message.from_user.id, f"Вы отредактировали {message.text}")



bot.infinity_polling()

