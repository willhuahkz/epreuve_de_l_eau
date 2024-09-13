"""
Module to find the next prime number
"""
import sys
import math
from utils.is_int import is_int

def is_prime(value):
    """
    Verify if a number is prime
    """
    if value > 3:
        if value & 1 == 0 or value % 3 == 0:
            return False
        limit = int(math.sqrt(value)) + 1
        # to avoid number divisable by 2 and 3
        for i in range(5, limit, 6):
            if value % i == 0 or value % (i + 2) == 0:
                return False
        return True
    else:
        return True

def get_next_prime(value):
    """
    Get next prime
    """
    if value < 2:
        return 2
    if value == 2:
        return 3
    prime = value
    if value & 1 == 0:
        prime += 1
    else:
        prime += 2
    while not is_prime(prime):
        prime += 2
    return prime

if len(sys.argv) > 1 and is_int(sys.argv[1]):
    arg = int(sys.argv[1])
    NEXT_PRIME = get_next_prime(arg)
    print(NEXT_PRIME)
    sys.exit(0)
print('error')
sys.exit(1)
