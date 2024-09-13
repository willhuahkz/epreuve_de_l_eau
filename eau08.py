"""
Module to determine if a string given in parameter in only digits
"""

import sys
import re

def is_string_only_digit(string):
    """
    Return if string contains only digit
    """
    pattern = r'^\d+$'
    return re.match(pattern, string)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("true" if is_string_only_digit(sys.argv[1]) else "false")
    else:
        print('error')
