import json
import requests


class ClassManager:
    def __init__(self):
        pass

    def __get_class_let_num(self, user_class):
        return [user_class[-1], user_class[:-1]]

    def is_class_in_db(self, school_id, user_class):
        all_classes = self.__move_from_json_to_domain(
            self.__get_all_classes_in_school(school_id)
        )
        user_class_letter, user_class_number = self.__get_class_let_num(user_class)

        for c in all_classes['classes']:
            if str(c['number']) == user_class_number and c['letter'] == user_class_letter:
                return True
        return False

    def __get_all_classes_in_school(self, school_id) -> json:
        url = f"https://lava-land.ru/api/school/{school_id}/class"
        classes_json = requests.get(url).json()
        return classes_json

    def __move_from_json_to_domain(self, classes_json):
        classes_domain = json.dumps(classes_json).encode('utf-8')
        classes_domain = json.loads(classes_domain.decode('utf-8'))
        return classes_domain

    def get_class_id(self, school_id, user_class) -> int:
        all_classes = self.__move_from_json_to_domain(
            self.__get_all_classes_in_school(school_id)
        )
        user_class_letter, user_class_number = self.__get_class_let_num(user_class)

        for c in all_classes['classes']:
            if str(c['number']) == user_class_number and c['letter'] == user_class_letter:
                return c['class_id']
        return None


