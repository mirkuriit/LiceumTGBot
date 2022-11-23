from datetime import time


class JsonFormatter:
    def __init__(self):
        pass

    # convert_json_to_human_one_lesson
    def convert_json_to_human_ol(self, json_data):
        human_output = []
        print(json_data['lessons'])

        for i in json_data['lessons']:
            name = i['name']
            start_time = time(hour=i['start_time'][0], minute=i['start_time'][1]).strftime("%H:%M")
            end_time = time(hour=i['end_time'][0], minute=i['end_time'][1]).strftime("%H:%M")
            teacher = i['teacher_name']
            human_output.append(f"Урок    : {name}\n"
                                f"Время   : {start_time}-{end_time}\n"
                                f"Учитель : {teacher}\n"
                                f"---------------------\n")

        return "".join(human_output)
