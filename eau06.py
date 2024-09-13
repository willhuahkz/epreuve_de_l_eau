"""
Module to convert a char into maj every 2 char
"""

import re
import sys

def is_string_correct(string):
    """
    Verify if the string contain at least one char
    """
    pattern = r'.*[a-zA-Z].*'
    return bool(re.match(pattern, string))

if len(sys.argv) == 2 and is_string_correct(sys.argv[1]):
    i = 0
    res_str = ''
    for letter in sys.argv[1]:
        if i & 1 != 0 and 'a' <= letter <= 'z':
            res_str += letter.upper()
        else:
            res_str += letter
        i += 1
    print(res_str)
else:
    print('error')
