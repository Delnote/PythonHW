# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
import string
from typing import List


def custom_range(*args) -> List[str]:
    res = []
    test_val = list(args[0])
    if len(args) == 2:
        res = range_char(test_val, 'a', args[1], 1)
    elif len(args) == 3:
        res = range_char(test_val, args[1], args[2], 1)
    elif len(args) == 4:
        res = range_char(test_val, args[1], args[2], args[3])
    return res


def range_char(test_val, start, stop, step):
    res = []
    result = []
    test_val_char_index = [ord(i) for i in test_val]
    for n in range(ord(start), ord(stop), step):
        res.append(test_val_char_index.index(n))
    for i in res:
        result.extend(test_val[i])
    return result
