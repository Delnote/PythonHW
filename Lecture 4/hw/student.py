from homework import *
from result import *


class Student:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def do_homework(self, hw: Homework, solution: str) -> Result:
        hw.check_deadline()
        res = Result(self, solution, hw)
        return res

