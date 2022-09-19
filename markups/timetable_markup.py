from telebot import types

# Использование класса ReplyKeyboardMarkup
# Его конструктор может принимать следующие необязательные аргументы:
# - resize_keyboard: True/False (по умолчанию False)
# - one_time_keyboard: True/False (по умолчанию False)
# - выборочно: True/False (по умолчанию False)
# - row_width: целое число (по умолчанию 3)
# row_width используется в сочетании с функцией add().
# Он определяет, сколько кнопок помещается в каждом ряду, прежде чем переходить к следующему ряду.

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
itebtn1 = types.KeyboardButton("Дай расписание шаболда")
markup.add(itebtn1)