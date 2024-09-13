"""
Module to sort an array by select sort
"""

import sys
from eau08 import is_string_only_digit



def select_sort(_array):
    """
    Sort an array by select sort
    """
    for i, _ in enumerate(_array):
        min_ = min(_array[i:])
        index = _array.index(min_)
        _array[index], _array[i] = _array[i], _array[index]
    return _array



if __name__ == '__main__':
    if len(sys.argv) > 1 and is_string_only_digit(sys.argv[1]):
        array = []
        del sys.argv[0]
        for arg in sys.argv:
            array.append(int(arg))
        array_sorted = select_sort(array)
        RES_STR = ' '.join(map(str, array_sorted))
        print(RES_STR)
    else:
        print('error')
