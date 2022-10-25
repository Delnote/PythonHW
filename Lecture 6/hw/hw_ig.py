# 1. Implement a function that flatten incoming data (non-iterables and elements from iterables) 
# and returns an iterator
import sys


def merge_elems(*elems):
    return flatten_data(elems)


def flatten_data(data):
    for elem in data:
        if isinstance(elem, (tuple, list)):
            yield from flatten_data(elem)
        elif isinstance(elem, dict):
            yield from elem.keys()
            yield from elem.values()
        elif isinstance(elem, str):
            yield from tuple(elem)
        elif elem is not None:
            yield elem


# example input
a = [1, 2, 3, 'prince']
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]
e = {1: 2, 3: 4}

for _ in merge_elems(a, b, c, d, e):
    print(_, end=' ')
print('\n')

# output: 1 2 3 6 z h a b a 1 2 3 4
# output: 1 2 3 p r i n c e 6 z h a b a 1 2 3 4 1 3 2 4

# 2. Implement a map-like function that returns an iterator 
# (extra functionality: if arg function can't be applied, return element as is + text exception)


def map_like(fun, *elems):
    for el in elems:
        try:
            hasattr(el, '__getitem__')
            yield fun(el)
        except:
            yield '{}: {}'.format(el, sys.exc_info()[1])


# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]

for _ in map_like(fun, a, b, c, d):
    print(_)

# output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable