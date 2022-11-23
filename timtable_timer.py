from datetime import time, timedelta
import datetime

class TimetableTimer:
    def __init__(self):
        self.default_timetable_calls = [
            timedelta(hours=8, minutes=0),
            timedelta(hours=8, minutes=40),
            timedelta(hours=8, minutes=50),
            timedelta(hours=9, minutes=30),
            timedelta(hours=9, minutes=45),
            timedelta(hours=10, minutes=25),
            timedelta(hours=10, minutes=45),
            timedelta(hours=11, minutes=25),
            timedelta(hours=11, minutes=40),
            timedelta(hours=12, minutes=20),
            timedelta(hours=12, minutes=30),
            timedelta(hours=13, minutes=10),
            timedelta(hours=13, minutes=20),
            timedelta(hours=14, minutes=0),
            timedelta(hours=14, minutes=5),
            timedelta(hours=14, minutes=45),
        ]

    def get_status(self):

        def nearest(now, pivot):
            for i in range(len(pivot)):
                print(now_time, " --- ", pivot[i])
                print(now_time - pivot[i])
                print()
                if now > pivot[i]:
                    continue
                else:
                    return pivot[i] - now
            return pivot[0] - now_time

        now_time = datetime.datetime.now().time()
        now_time = timedelta(hours=now_time.hour, minutes=now_time.minute)

        status = nearest(now_time, self.default_timetable_calls)

        return str(status)[8:] if len(str(status)) > 10 else str(status)


