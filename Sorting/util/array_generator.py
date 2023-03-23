from util.array_type_enums import *
from random import randint

MIN_ARRAY_VALUE = 0
MAX_ARRAY_VALUE = 1000

def generate_array(array_type, array_length):
    assert array_length > 0

    array = [randint(MIN_ARRAY_VALUE, MAX_ARRAY_VALUE)]

    for i in range(array_length):
        if array_type == ARRAY_IDENTICAL:
            array.append(array[-1])
        elif array_type == ARRAY_ASCENDING:
            array.append(randint(array[-1], MAX_ARRAY_VALUE))
        elif array_type == ARRAY_DESCENDING:
            array.append(randint(MIN_ARRAY_VALUE, array[-1]))
        else:
            array.append(randint(MIN_ARRAY_VALUE, MAX_ARRAY_VALUE))
    return array