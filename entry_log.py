import csv
import datetime
import re
import random
import sys

from entry import Entry
import interface
import switch
import entry_finder
from validator import Validator

# from switch import switch

class EntryLog(object):

    DATE_FMT = '%m-%d-%Y'
    TIME_FMT = '%Hh%Mm%Ss'

    def __init__(self, filename="work-log-records.csv"):
        # entries is a dict with the start times as keys and entry objects as values
        self.entries = {}
        self.filename = filename
        self.next_id = random.randint(0,300)

        try:
            self.process_single_csv(self.filename)
        except OSError as ose:
            print(ose)
            print(self.filename + " will be created upon exit.")
        except ValueError as ve:
            print(ve)

    def save_data_to_csv(self):
        today = datetime.date.today()

        entry_keys = list(self.entries.values())[0].__dict__.keys()

        with open(self.filename, 'w') as csvfile:
            fields = entry_keys
            task_writer = csv.DictWriter(csvfile, fieldnames=fields)

            task_writer.writeheader()

            for entry_name, entry_value in self.entries.items():
                task_writer.writerow(entry_value.__dict__)

        return self.filename


    def process_single_csv(self, filename):

        with open(filename, newline='') as csvfile:
            eventreader = csv.DictReader(csvfile, delimiter=",")
            entries = list(eventreader)

            for entry in entries:

                try:
                    task_datetime = datetime.datetime.strptime(entry['date'], '%Y-%m-%d')
                    task_duration = self.parse_duration(entry['duration'], delimiter='colon')
                    id_num = int(entry['id_num'])
                except ValueError as ve:
                    raise(ve)

                task_date = task_datetime.date()
                new_entry = Entry(id_num=id_num, title=entry['title'], date=task_date, duration=task_duration, notes=entry['notes'])
                self.add_entry(new_entry)

    def add_entry(self, entry):
        if entry.id_num in self.entries.keys():
            raise ValueError("Task must be unique.")

        self.entries[entry.id_num] = entry
        self.next_id += 1

    def delete_entry(self, entry_data):
        if not isinstance(entry_data, (int, Entry)):
            raise ValueError('Must use an integer or Entry object for deletion.')

        if isinstance(entry_data, int):
            id_check = entry_data
        else:
            id_check = entry_data.id_num

        try:
            del self.entries[id_check]
        except KeyError as ke:
            print('No task found.')
            print(ke)

    def get_dates(self):
        return set([entry.date for entry in self.entries.values()])

    def get_entry_by_id(self, id_num):
        return self.entries[id_num]

    def get_entries_by_date(self, date_to_search):
        return self.get_entries_by_date_range(date_to_search, None)

    def get_entries_by_date_range(self, start_date, end_date=None):
        # accept one or two arguments
        if not end_date:
            # only single date provided
            return [entry for entry in self.entries.values() if entry.date == start_date]

        else:
            # two dates given
            return [entry for entry in self.entries.values() if start_date <= entry.date <= end_date]

    def get_entries_by_duration(self, duration):
        return self.get_entries_by_duration_range(duration, None)

    def get_entries_by_duration_range(self, min_time, max_time=None):
        # accepts one or two args
        if not max_time:
            return [entry for entry in self.entries.values() if entry.duration == min_time]
        else:
            return [entry for entry in self.entries.values() if min_time <= entry.duration <= max_time]

    def get_entries_by_keyword(self, keyword):
        returned_list = []

        for entry in self.entries.values():
            if keyword in entry.title or keyword in entry.notes:
                returned_list.append(entry)
        return returned_list

    def get_entries_by_regex(self, expression):
        pattern = re.compile(r'{}'.format(expression))
        returned_list = []

        for entry in self.entries.values():
            if pattern.search(entry.title) or pattern.search(entry.notes):
                returned_list.append(entry)

        return returned_list

    def parse_duration(self, time_str, delimiter='letters'):
        # TODO: adjust regex to allow for other formats
            # want to allow (integer) + (h or :) + (integer) + (m or :) + (integer) + (optional s)
            # must be consistent across whole string (e.g. can't use 4h05:99)
        if delimiter == 'letters':
            regex = re.compile(r'((?P<hours>\d+?)h)?((?P<minutes>\d+?)m)?((?P<seconds>\d+?)?s)?')
        else:
            regex = re.compile(r'((?P<hours>\d+?):)?((?P<minutes>\d+?):)?((?P<seconds>\d+?)\b)?')

        parts = regex.match(time_str)

        if not parts:
            raise ValueError("Invalid time string.")

        parts = parts.groupdict()
        time_params = {}

        for (name, param) in parts.items():
            if param:
                time_params[name] = int(param)

        return datetime.timedelta(**time_params)
