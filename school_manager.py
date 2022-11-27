import json
import requests

class SchoolManager:
    def __init__(self):
        self.all_schools = self.__move_from_json_to_domain(
            self.__get_schools()
        )

    def get_school_id(self, school):
        for s in self.all_schools['schools']:
            if s['name'] == school:
                return s['school_id']
        return None

    def is_school_in_db(self, school):
        for s in self.all_schools['schools']:
            print(s)
            print(s['name'],  school)
            print(type(s['name']))
            print(type(school))
            if s['name'] == school:
                return True
        return False

    def __move_from_json_to_domain(self, schools_json):
        schools_domain = json.dumps(schools_json).encode('utf-8')
        schools_domain = json.loads(schools_domain.decode('utf-8'))
        print(schools_domain)
        return schools_domain


    def __get_schools(self) -> json:
        url = "https://lava-land.ru/api/school"
        schools_json = requests.get(url).json()
        return schools_json

