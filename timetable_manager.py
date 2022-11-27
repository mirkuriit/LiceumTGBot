import json
import requests

class TimeTableManager:
    def __init__(self):
        self.timetable_picture = open("resourses/timetable.jpg", "rb")

    def __move_from_json_to_domain(self, timetable_json):
        print(timetable_json)
        timetable_domain = json.dumps(timetable_json).encode('utf-8')
        timetable_domain = json.loads(timetable_domain.decode('utf-8'))
        print(timetable_domain)
        return timetable_domain

    def __get_timetable_json(self, user_class_id):
        #TODO !!!! эта штука должна работать с группами
        timetable_json = requests.get(f'https://lava-land.ru/api/subgroup/{user_class_id}/lesson').json()
        return timetable_json

    def get_timetable(self, user_class_id):
        return self.__move_from_json_to_domain(
            self.__get_timetable_json(
                user_class_id
            )
        )
