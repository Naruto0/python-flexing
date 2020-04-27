from random import shuffle
from sorting import SORTING_METHODS


def register_algorythm(name):
    def decorator(func):
        SORTING_METHODS[name] = func
        return func
    return decorator


def generate(rng):
    """Make random range"""
    li = [i for i in range(*rng)]
    shuffle(li)
    return li