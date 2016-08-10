# endeavor to convert all captured times to utc prior to processing
# another issue is to handle navigation around the actions
# individual csv files are saved based on the day they're created
    # at instantiation

import csv
import datetime

import entry
import interface

# from switch import switch

class WorkLog(object):

    DATE_FMT = '%Y-%m-%d'
    TIME_FMT = '%H:%M:%S'

    def __init__(self):
        # entries is a dict with the start times as keys and entry objects as values
        self.entries = {}

    def get_data_from_csv(self):
        # create list or dict of entries from each row in the csv
        with open(self.filename, newline='') as csvfile:
            eventreader = csv.DictReader(csvfile, delimiter=',')
            rows = list(eventreader)
        pass

    # work on manipulating single lines of a csv
    def save_data_to_csv(self):
        # when saving, ensure to create csv header line
        pass

    def process_single_csv(self, filename):

        with open(filename, newline='') as csvfile:
            eventreader = csv.DictReader(csvfile, delimiter=",")
            entries = list(eventreader)

            for entry in entries:
                self.entries[entry['start_datetime']] = Entry(entry['task_name'], entry['start_datetime'], entry['duration'], entry['notes'])

    # CRUD?
    def add_entry(self):
        pass

    def delete_entry(self):
        pass

    def update_entry(self):
        pass

    def search_by_string(self, needle):
        pass

    def search_by_patten(self, needle):
        pass

    def search_by_date(self, needle_date):
        pass

    def create_new_entry(self):
        pass

if __name__ == '__main__':

    main_log = WorkLog()
    # As a user of the script, I should be able to choose whether to add a new entry or lookup previous entries.
    # display options
    # capture user response
    menu = 'main'
    action = interface.prompt_for_action(menu).lower()

    for case in switch(action):
        if case('c') or case('create'):
            # prompt user for new entry
                # capture task name, duration, and notes
                # validate input
            # get local current time
                # convert to UTC
            # create new entry with the captured data
            # return to original/main menu
        elif case('s') or case('search'):
            # prompt for new selection from search menu
            # based on selection
            pass
        elif case('r') or case('print'):
            # print formatted report to the screen
            # return to main menu
            pass
        elif case('k') or case('keyword'):
            pass
        elif case('p') or case('pattern'):
            pass
        elif case('d') or case('duration'):
            pass
        elif case('t') or case('time'):
            pass
        elif case('n') or case('name'):
            pass
        else:
            # quit
            pass













