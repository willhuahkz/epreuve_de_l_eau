"""
Find an index of first occurence
"""

import sys

if len(sys.argv) > 2:
    occurence = sys.argv[-1]
    del sys.argv[0]
    del sys.argv[-1]
    try:
        print(sys.argv.index(occurence))
    except ValueError:
        print(-1)
else:
    print('error')
