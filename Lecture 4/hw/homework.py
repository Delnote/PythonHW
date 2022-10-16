from datetime import datetime, timedelta
from deadlineError import *


class Homework:
    def __init__(self, title, deadline):
        ini_time_for_now = datetime.now()
        self.title = title
        self.deadline = ini_time_for_now + timedelta(days=deadline)

    def check_deadline(self):
        if self.deadline <= datetime.now():
            raise DeadlineError('You are late')
