'''
simple C/C++ build tool made in python
'''


import changes

change_file = 'testing/changes.csv'
test_file = 'testing/testing.py'


def main():
    changes.change_file_add(change_file, 'char.c', 25)
    return


if __name__ == '__main__':
    main()
