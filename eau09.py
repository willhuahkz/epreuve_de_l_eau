"""
Module to print numbers between two number
"""

import sys

ERROR_MSG = 'error'

def print_numbers_between(min_, max_):
    """
    Print numbers between two number
    """
    res_str = []
    while (min_ < max_):
        res_str += [str(min_)]
        min_ += 1
    print(' '.join(res_str))

if len(sys.argv) == 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        if num1 < num2:
            print_numbers_between(num1, num2)
        else:
            print_numbers_between(num2, num1)
    except ValueError:
        print(ERROR_MSG)
else:
    print(ERROR_MSG)
