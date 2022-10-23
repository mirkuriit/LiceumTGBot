from telebot import types

# Использование класса ReplyKeyboardMarkup
# Его конструктор может принимать следующие необязательные аргументы:
# - resize_keyboard: True/False (по умолчанию False)
# - one_time_keyboard: True/False (по умолчанию False)
# - выборочно: True/False (по умолчанию False)
# - row_width: целое число (по умолчанию 3)
# row_width используется в сочетании с функцией add().
# Он определяет, сколько кнопок помещается в каждом ряду, прежде чем переходить к следующему ряду.

timetable_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
itebtn1 = types.KeyboardButton("Дай общее расписание шаболда")
itebtn2 = types.KeyboardButton("Пойти нахуй")
itebtn3 = types.KeyboardButton("Дай мое расписание шаболда")
timetable_markup.add(itebtn1, itebtn2, itebtn3)

link_markup = types.InlineKeyboardMarkup()
itebtn_lawrence_link = types.InlineKeyboardButton("нахуй", url="https://lava-land.ru")
link_markup.add(itebtn_lawrence_link)