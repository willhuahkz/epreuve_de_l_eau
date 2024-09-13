"""
Module to define if a parameter is an int
"""

def is_int(value):
    """
    Verify if value is a number
    """
    try:
        int(value)
        return True
    except ValueError:
        return False
