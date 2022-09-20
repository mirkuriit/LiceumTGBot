import re
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


print(is_correct_class("11A"))
print(is_correct_class("10d"))
print(is_correct_class("12B"))
print(is_correct_class("10A"))
#Русские
print(is_correct_class("10д"))
print(is_correct_class("9в"))
print(is_correct_class("8и"))
print(is_correct_class("90а"))

