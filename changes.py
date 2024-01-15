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
import tempfile
from logging import eprint


CHANGE_FILE_NAME = 'changes.csv'
FILENAME = 0
TIME_OF_MODIFICATION = 1


def get_change_file_entry(change_file: str, entry_name: str):
    '''
    returns an entry from the change file with the with corresponding
    entry name. Otherwise, returns None.
    '''
    try:
        with open(change_file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=' ')
            for row in csvreader:
                if row[FILENAME] == str:
                    return row
        return None
    except FileNotFoundError:
        eprint(f'[ERROR] file {change_file} not found.')


def create_changes_file():
    ''' creates a change file to store most recent modification of files'''
    file = os.open(CHANGE_FILE_NAME)
    file.close()


def change_file_add(change_file: str, entry_name: str, time: float):
    if get_change_file_entry(change_file, entry_name) is not None:
        eprint(f'[ERROR] entry {entry_name} is already in change file.')
        return

    with open(CHANGE_FILE_NAME) as csvfile:
        csvwritter = csv.writer(csvfile, delimiter=' ')
        csvwritter.writerow((entry_name, time))


def change_file_update(change_file: str, entry_name: str, time: float):
    '''
    updates the time of an existing entry in the change file
    '''
    if get_change_file_entry(change_file, entry_name) is None:
        eprint(f'''[WARNING] entry {entry_name} does not exist in the change
            file. An entry for {entry_name} has been created with the given
            time {time}.''')
        change_file_add(change_file, entry_name, time)
        return

    fp = tempfile.TemporaryFile()  # create a temporary file
    with open(change_file, mode='w+r') as file: 
        csvreader = csv.reader(file, delimitor=' ')
        for row in csvreader:
            if row[CHANGE_FILE_NAME] == entry_name:
                row[TIME_OF_MODIFICATION] == time
            fp.write(' '.join(row))
        file.writelines(fp.readlines())  # is writelines cooked?
    fp.close()


def change_file_pop(change_file: str, entry_name: str):
    '''
    removes a file entry in the change file
    '''
    if get_change_file_entry(change_file, entry_name) is None:
        eprint(f'''[WARNING] entry {entry_name} does not exist in the change
            file. An entry for {entry_name} has been created with the given
            time {time}.''')
        change_file_add(change_file, entry_name, time)
        return

    fp = tempfile.TemporaryFile()  # create a temporary file
    with open(change_file, mode='w+r') as file: 
        csvreader = csv.reader(file, delimitor=' ')
        for row in csvreader:
            if row[CHANGE_FILE_NAME] != entry_name:
                fp.write(' '.join(row))
        file.writelines(fp.readlines())  # is writelines cooked?
    fp.close()


def has_changed(change_file: str, entry_name: str):
    '''checks if a file has been changed'''
    # check if the file even exists
    try:
        last_update_time = os.stat(entry_name).st_mtime
    except FileNotFoundError:
        eprint(f'[ERROR] file {entry_name} not found.')
        return

    last_recorded_modification = get_change_file_entry(change_file, entry_name)
    if last_recorded_modification is None:
        return True
    elif last_recorded_modification[TIME_OF_MODIFICATION] == last_update_time:
        return True
    else:
        return False
