"""
Module to determine if a string given in parameter in only digits
"""

import sys
import re

if len(sys.argv) == 2:
    PATTERN = r'^\d+$'
    if re.match(PATTERN, sys.argv[1]):
        print('true')
    else:
        print('false')
else:
    print('error')
