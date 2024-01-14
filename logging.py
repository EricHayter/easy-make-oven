'''
Collection of functions used for logging errors in the program
'''


import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
