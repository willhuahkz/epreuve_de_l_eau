"""
Module to make char upper for first char of words of a string
"""

import sys
import re

if len(sys.argv) == 2:
    PATTERN = r'\b\w+\b'
    words = re.findall(PATTERN, sys.argv[1])
    res_str = ' '.join(word.capitalize() for word in words)
    print(res_str)
else:
    print('error')
