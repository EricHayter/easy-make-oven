'''
simple C/C++ build tool made in python
'''


import changes


def main():
    changes.has_changed('changed.csv', 'testing.py')
    return


if __name__ == '__main__':
    main()
