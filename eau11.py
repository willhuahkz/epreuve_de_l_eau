"""
Module to print the min absolu in an array of int
"""

import sys

ERROR_MSG = 'error'

if len(sys.argv) > 3:
    numbers = []
    del sys.argv[0]
    for arg in sys.argv:
        try:
            number = int(arg)
            numbers.append(number)
        except ValueError:
            print(ERROR_MSG)
    min_ = abs(numbers[0] - numbers[1])
    for i, number_i in enumerate(numbers):
        for j, number_j in enumerate(numbers):
            if i != j:
                tmp = abs(number_i - number_j)
                if tmp < min_:
                    min_ = tmp
    print(min_)
else:
    print(ERROR_MSG)
