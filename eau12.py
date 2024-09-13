"""
Module to sort a list via bubble sort
"""
import sys
from eau08 import is_string_only_digit

def is_sorted(_array):
    """
    Verify if an array is sorted
    """
    for i in range(len(_array) - 1):
        if _array[i] > _array[i + 1]:
            return False
    return True


def bubble_sort(array_to_sort):
    """
    Bubble sort
    """
    while not is_sorted(array_to_sort):
        for i in range(len(array_to_sort) - 1):
            if array_to_sort[i] > array_to_sort[i + 1]:
                tmp = array_to_sort[i + 1]
                array_to_sort[i + 1] = array_to_sort[i]
                array_to_sort[i] = tmp
    return array_to_sort

if __name__ == '__main__':
    if len(sys.argv) > 1 and is_string_only_digit(sys.argv[1]):
        array = []
        del sys.argv[0]
        for arg in sys.argv:
            array.append(int(arg))
        array_sorted = bubble_sort(array)
        RES_STR = ' '.join(map(str, array_sorted))
        print(RES_STR)
    else:
        print('error')
