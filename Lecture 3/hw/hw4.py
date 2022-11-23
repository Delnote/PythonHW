"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so on.
You may assume that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import itertools
from tkinter import _flatten
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    res = []
    temp = args[0]
    for i in range(len(args) - 1):
        temp = count(temp, args[i + 1])
    for val in temp:
        res.append(list(_flatten(val)))
    return res


def count(counted: List[Any], new: List[Any]) -> List[List]:
    result_collection = []
    for x in (itertools.product(counted, new)):
        result_collection.append([x[0], x[1]])
    return result_collection
