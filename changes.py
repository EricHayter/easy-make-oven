"""
check for changes in files to see if a recompile is necessary

All data should be located inside of the "changes.csv" file written as a csv
with a ' ' delimiter. For example the document should follow the format:

foo.c 2131231
bar.h 9923131

In this example the first entry in each column should be the name of a file
and the second entry will be the last time of modification provided by the
operating system.
"""


import os
import csv


CHANGE_FILE_NAME = 'changes.csv'
FILENAME = 0
TIME_OF_MODIFICATION = 1


def get_change_file_entry(change_file: str, entry_name: str):
    '''
    returns an entry from the change file with the with corresponding 
    entry name. Otherwise, returns None.
    '''
    with open(change_file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        for row in csvreader:
            if row[FILENAME] == str:
                return row
    return None


def create_changes_file():
    ''' creates a change file '''
    file = os.open(CHANGE_FILE_NAME)
    file.close()


def change_file_add(change_file: str, entry_name: str, time: float):
    with open(CHANGE_FILE_NAME):
        # search if it's already in the csv file 
        return 


def change_file_update(change_file: str, entry_name: str, time: float):
    if get_change_file_entry(change_file, entry_name) is None:
        change_file_add(change_file, entry_name, time)
        return

    with open(change_file):
        csvwritter = csv.writer(change_file, delimitor=' ')


def change_file_pop():
    return  


def has_changed(change_file: str, entry_name: str):
    '''checks if a file has been changed'''
    # check if the file even exists
    last_update_time = os.stat(entry_name).st_mtime

    print(f'Last change was {last_update_time} seconds ago')

    # get the stat of the object

    # check the history file

    # return if the dates of change are later than in the history file
    return
