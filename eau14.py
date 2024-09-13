"""
Module to print a list in ascii order
"""

import sys

def ord_string_array(array):
    """
    Get an array of value of char (in ascii)
    """
    return [[ord(char) for char in string] for string in array]

def char_string_array(array):
    """
    Get an array of char from an array of values
    """
    return [[chr(char) for char in string] for string in array]

def is_sorted(_array):
    """
    Verify if an array is sorted
    """
    for i in range(len(_array) - 1):
        if compare_two_words_ascii(_array[i], _array[i + 1]):
            return False
    return True

def compare_two_words_ascii(word1, word2):
    """
    Method to compare two words with their ascii values
    Return true if the word1 > word2 in ascii
    """
    for letter1, letter2 in zip(word1,  word2):
        if letter1 < letter2:
            return False
    return True

def bubble_sort(array_to_sort):
    """
    Bubble sort
    """
    while not is_sorted(array_to_sort):
        for i in range(len(array_to_sort) - 1):
            if compare_two_words_ascii(_array[i], _array[i + 1]):
                _array[i], _array[i + 1] = _array[i + 1], _array[i]
    return array_to_sort

if len(sys.argv) > 1:
    del sys.argv[0]
    _array = ord_string_array(sys.argv)
    _sorted_array = bubble_sort(_array)
    _sorted_array_str = char_string_array(_sorted_array)
    # print('_sorted_array_str = ', _sorted_array_str)
    RES = ' '.join(''.join(string) for string in _sorted_array_str)
    print(RES)

else:
    print('error')
