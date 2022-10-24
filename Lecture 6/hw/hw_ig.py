# 1. Implement a function that flatten incoming data (non-iterables and elements from iterables) 
# and returns an iterator
import sys


def merge_elems(*elems):
    res = []
    for el in elems:
        if isinstance(el, str):
            res.append(list(el))
        else:
            res.append(el)
    return iter(flatten_data(res))


def flatten_data(data):
    res = ()
    for elem in data:
        if isinstance(elem, (tuple, list)):
            res = res + flatten_data(elem)
        elif elem is not None:
            res = res + (elem,)
    return res

# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')

# output: 1 2 3 6 z h a b a 1 2 3 4

# 2. Implement a map-like function that returns an iterator 
# (extra functionality: if arg function can't be applied, return element as is + text exception)


def map_like(fun, *elems):
    res = []
    for el in elems:
        try:
            hasattr(el, '__getitem__')
            res.append(fun(el))
        except:
            res.append('{}: {}'.format(el, sys.exc_info()[1]))

    return res
    # pass


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