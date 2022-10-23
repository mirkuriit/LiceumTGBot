import json
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



data = json.dumps({'lessons': [{'id': 1, 'name': 'Математика', 'required': True, 'teacher': 'Мария Александровна Зубакова',
                      'times': {'10Б': {'Monday': [[8, 0, 8, 30]]}}}]},
                    ).encode("utf-8")
d = json.loads(data.decode("utf-8"))
print(d)