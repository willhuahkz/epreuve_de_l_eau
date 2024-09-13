"""
Module to print arguments in reverse
"""

import sys

length_args = len(sys.argv)

if length_args > 1:
    for i in range (length_args - 1, 0, -1):
        print(sys.argv[i])
else:
    print('error.')
    sys.exit(1)
