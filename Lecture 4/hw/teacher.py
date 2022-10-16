from typing import List

from homework import *
from result import *


class Teacher:
    homework_done = {}

    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    @staticmethod
    def create_homework(title: str, deadline: int):
        return Homework(title, deadline)

    @staticmethod
    def store_done_homework(res: Result):
        if not res.is_done:
            Teacher.homework_done[res.hw] = []
        else:
            Teacher.homework_done[res.hw] = [res]

    def check_homework(self, res: Result) -> bool:
        if len(res.solution) > 5:
            res.is_done = True
        else:
            res.is_done = False
        res.reviewer = self
        Teacher.store_done_homework(res)
        return res.is_done

    @staticmethod
    def reset_results():
        Teacher.homework_done.clear()


