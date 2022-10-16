from homework import *


class Teacher:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    @staticmethod
    def create_homework(title: str, deadline: int):
        return Homework(title, deadline)
