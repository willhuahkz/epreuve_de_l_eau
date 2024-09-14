"""
Module to find the next prime number
"""
import sys
from utils.is_int import is_int

def square_root_of(number):
    """
    Get square root of a number
    Same resultat of math.sqrt
    """
    i = 0
    limit = 500
    # there is no overflow in python
    while i < limit:
        res = i * i
        if res >= number:
            return i
        i += 1
    return None

def is_prime(value):
    """
    Verify if a number is prime
    """
    if value > 3:
        if value & 1 == 0 or value % 3 == 0:
            return False
        sqr = square_root_of(value)
        if sqr is None:
            return False
        limit = sqr + 1
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
print('-1')
sys.exit(1)
