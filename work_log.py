import csv
import datetime
import re


from entry import Entry
from entry_log import EntryLog
import interface
from menu_option import MenuOption

class WorkLog(object):
    """Class for managing the Work Log application.
    
    Controls the parts of the log including the display, I/O, and maintaining 
    state.
    """
    def __init__(self, **kwargs):

        self.entry_to_display = None
        self.action = 'main'
        self.err_msg = ''
        self.results = []

        if kwargs:
            for attr, val in kwargs.items():
                setattr(self, attr, val)

    def menu(self):

        menu_to_display = self.main_menu

        if self.action == 'search':
            menu_to_display = self.search_menu
        elif self.action == 'date':
            menu_to_display = self.date_menu
        elif self.action == 'duration':
            menu_to_display = self.duration_menu
        elif self.action == 'edit':
            menu_to_display = self.edit_menu

        interface.write_header('{} menu'.format(self.action), self.err_msg)

        interface.display_menu(menu_to_display, self.entry_to_display)

        action, selection = interface.get_action_option(menu_to_display)

        if not action:
            self.err_msg = "'{}' not found. Select again.".format(selection)
            return

        self.action = action
        self.err_msg = ''

    def create_new_entry(self):
        
        self.entry_to_display = Entry(id_num=self.log.next_id)

        action_prompts = [
            {'prompt': 'enter task name:', 'attr' : 'title'},
            {'prompt': 'enter task duration:', 'attr': 'duration'},
            {'prompt': 'enter task date (MM-DD-YYYY) or "today":', 'attr' : 'date'},
            {'prompt': 'enter task notes:', 'attr': 'notes'}
        ]
        
        while not self.entry_to_display.is_complete():

            interface.write_header('create new entry', self.err_msg)

            prompt = action_prompts[0]

            value = interface.get_action_input(prompt, self.entry_to_display)

            if prompt['attr'] == 'duration':

                try:
                    value = int(value)
                    value = datetime.timedelta(minutes=value)
                except ValueError as ve:
                    self.err_msg = str(ve)
                    continue

            elif prompt['attr'] == 'date':

                if value.lower() != 'today':

                    try:
                        value = datetime.datetime.strptime(value, self.log.DATE_FMT).date()
                    except ValueError as ve:
                        self.err_msg = str(ve)
                        continue

                else:
                    value = datetime.date.today()

            if not value:
                self.err_msg = '{} cannot be empty'.format(prompt['attr'])
                continue

            setattr(self.entry_to_display, prompt['attr'], value)
            action_prompts.remove(prompt)
            self.err_msg = ''


        self.action = 'save'
        self.err_msg = ''
    
    def search_by_pattern(self, prompt, header_text):

        interface.write_header(header_text, self.err_msg)

        pattern = interface.get_action_input(prompt)

        if pattern == '<':
            self.action = 'search'
            self.err_msg = ''
            return

        self.results = self.log.get_entries_by_keyword(pattern)

        if self.action == 'pattern':
            self.results = self.log.get_entries_by_regex(pattern)
            pattern = 'that pattern'

        if not self.results:
            self.err_msg = "No entries found containing {}.".format(pattern)
            return

        self.action = 'results'
        self.err_msg = ''

    def search_by_duration(self, action_prompts, header_text):

        crit_list = []

        interface.write_header(header_text, self.err_msg)

        for prompt in action_prompts:

            try:
                crit = int(interface.get_action_input(prompt))
                crit = datetime.timedelta(minutes=crit)
            except ValueError as ve:
                self.err_msg = str(ve).upper()
                return

            crit_list.append(crit)

        self.results = self.log.get_entries_by_duration_range(*crit_list)

        if not self.results:
            self.err_msg = 'No entries found.'
            return

        self.action = 'results'
        self.err_msg = ''

    def search_by_date(self, action_prompts, header_text):

        crit_list = []

        interface.write_header(header_text, self.err_msg)
        
        if 'date_s' in self.action:

            date_list = sorted(self.log.get_dates())

            interface.display_list_results(date_list)

        for prompt in action_prompts:

            crit_str = interface.get_action_input(prompt)

            try:
                crit = datetime.datetime.strptime(crit_str, self.log.DATE_FMT)
            except ValueError as ve:
                self.err_msg = str(ve).upper()
                return

            crit_list.append(crit.date())

        self.results = self.log.get_entries_by_date_range(*crit_list)

        if not self.results:
            self.err_msg = 'No entries found.'
            return

        self.action = 'results'
        self.err_msg = ''

    def process_results(self):

        header_text = 'showing entry {} of {}'

        self.action, self.entry_to_display = interface.get_entry_from_results(
            self.results,
            header_text,
            self.task_menu
        )

        self.err_msg = ''
        self.results = []

    def update_entry_att(self, header_text, prompt):
        
        interface.write_header(header_text, self.err_msg)

        input_val = interface.get_action_input(prompt, self.entry_to_display)

        if input_val == '<':
            self.action = 'edit'
            self.err_msg = ''
            return
        elif input_val == '':
            self.err_msg = '{} cannot be empty'.format(prompt['attr'])
            return

        if 'date' in self.action:
            try:
                date = datetime.datetime.strptime(input_val, self.log.DATE_FMT)
                input_val = date.date()
            except ValueError as ve:
                self.err_msg = str(ve)
                return

        elif 'duration' in self.action:
            try:
                time_int = int(input_val)
                input_val = datetime.timedelta(minutes=time_int)
            except ValueError as ve:
                self.err_msg = str(ve)
                return


        setattr(self.entry_to_display, prompt['attr'], input_val)
        self.action = 'edit'
        self.err_msg = ''

    def save_entry(self):
        prompt = {'prompt': '[y/n]'}

        interface.write_header('save entry?', self.err_msg)

        selection = interface.get_action_input(prompt, self.entry_to_display)

        if selection in ('n', 'no'):
            print('ENTRY NOT SAVED')
        elif selection in ('y', 'yes'):
            self.log.add_entry(self.entry_to_display)
        else:
            self.err_msg = 'Please select y or n.'
            return

        self.reset_vars()

    def delete_entry(self):
        prompt = {'prompt': '[y/n]'}

        interface.write_header('confirm delete?', self.err_msg)

        selection = interface.get_action_input(prompt, self.entry_to_display)

        if selection in ('n', 'no'):
            print('ENTRY NOT DELETED')
        elif selection in ('y', 'yes'):
            self.log.delete_entry(self.entry_to_display)
        else:
            self.err_msg = 'Please select y or n.'
            return

        self.reset_vars('search')

    def print_report(self):

        prompt = {'prompt': 'enter [x] to exit'}
            
        interface.write_header('log report', self.err_msg)

        interface.display_list_results(self.get_entries(), 'entry')

        response = interface.get_action_input(prompt)

        if response != 'x':
            self.err_msg = 'you must enter [x] to exit'
        else:
            self.reset_vars()

    def get_entries(self):
        return self.log.entries.values()

    def reset_vars(self, action='main'):
        self.action = action
        self.entry_to_display = None
        self.err_msg = ''
