import json
import re
import datetime
from datetime import time
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
#d = json.loads(data.decode("utf-8"))
#print(d)
def aaaaaaaaa():
    t = datetime.time(hour=1, minute=10, second=0).strftime("%Y-%m-%d, %H:%M")
    print(t)


aaaaaaaaa()