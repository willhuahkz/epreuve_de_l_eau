"""
Module to know if a string contains another string sequence
"""
import sys

if len(sys.argv) > 2:
    if sys.argv[2] in sys.argv[1]:
        print('True')
    else:
        print('False')
    sys.exit(0)
print('error')
