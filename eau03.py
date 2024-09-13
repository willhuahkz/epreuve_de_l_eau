"""
Print suite of Fibonacci for n
"""

import sys
from utils.is_int import is_int

# if x >= 2
# Xn = Xn-1 + Xn-2

def recursiv_fibonacci(x, y, n, i):
    """
    Calculate fibonacci for n in recursiv
    """
    if i == 0:
        return n
    n = x + y
    return recursiv_fibonacci(y, n, n, i - 1)

if len(sys.argv) > 1 and is_int(sys.argv[1]):
    arg = int(sys.argv[1])
    if arg > -1:
        RES = recursiv_fibonacci(0, 1, 0, arg)
        print(RES)
        sys.exit(0)
print('error')
sys.exit(1)
