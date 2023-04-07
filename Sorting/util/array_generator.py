from util.array_type_enums import *
from random import randint

MIN_ARRAY_VALUE = 0
MAX_ARRAY_VALUE = 1000000

def generate_array(array_type, array_length, min_array_value=MIN_ARRAY_VALUE, max_array_value=MAX_ARRAY_VALUE):
    assert array_length > 0

    array = [randint(min_array_value, max_array_value)]

    for i in range(array_length):
        if array_type == ARRAY_IDENTICAL:
            array.append(array[-1])
        elif array_type == ARRAY_ASCENDING:
            array.append(i)
        elif array_type == ARRAY_DESCENDING:
            array.append(array_length - i)
        else:
            array.append(randint(min_array_value, max_array_value))
    return array