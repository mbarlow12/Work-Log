# holds all the data for a single log entry. usually generated after processing
# the csv file
import datetime

class Entry(object):
    def __init__(self, task_name, start_datetime, duration, notes):
        self.task_name = task_name
        self.start_datetime = start_datetime
        self.duration = duration
        self.notes = notes
