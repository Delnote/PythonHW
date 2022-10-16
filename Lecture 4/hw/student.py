from homework import *


class Student:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    @staticmethod
    def do_homework(hw: Homework, solution: str):
        hw.check_deadline()
