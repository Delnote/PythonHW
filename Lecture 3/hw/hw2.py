"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable


def cache(func: Callable) -> Callable:
    return cache_wrapper(func)


cache_dict = {}


def cache_wrapper(func):
    if func not in cache_dict:
        cache_dict[func] = {}

    def cached_func(*args):
        if args in cache_dict[func]:
            return cache_dict[func][args]

        value = func(*args)
        cache_dict[func][args] = value
        return value

    return cached_func
