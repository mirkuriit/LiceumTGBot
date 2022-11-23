import json
import requests

class TimeTableManager:

    def __init__(self):
        # todo сделать класс работы с лаврентьевским Api
        self.restManager = None
        #self.timatable_json = None
        self.timetable_picture = open("resourses/timetable.jpg", "rb")

    def __get_class_id(self, user_class):
        # todo сделать запросом к бд
        if user_class.lower() == '10б':
            return 1
        return 1

    def __move_from_json_to_domain(self, timetable_json):
        print(timetable_json)
        timetable_domain = json.dumps(timetable_json).encode('utf-8')
        timetable_domain = json.loads(timetable_domain.decode('utf-8'))
        print(timetable_domain)
        return timetable_domain

    def __get_timetable_json(self, user_class):
        user_class_id = self.__get_class_id(user_class)
        timetable_json = requests.get(f'https://async-api.lava-land.ru/class/{user_class_id}/lesson').json()
        return timetable_json

    def get_timetable(self, user_class):
        return self.__move_from_json_to_domain(
            self.__get_timetable_json(
                user_class
            )
        )
