import datetime
import textwrap


class Entry(object):

    def __init__(self, **kwargs):
        '''@param id_num -- int
           @param title -- string
           @param date -- python date
           @param duration -- python timedelta
           @param notes -- string'''
        self.id_num = 0
        self.title = ''
        self.date = None
        self.duration = None
        self.notes = ''

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def is_complete(self):
        res = False
        if self.id_num != 0 and self.title and self.date and self.duration and self.notes:
            res = True

        return res

    def string_format(self):
        '''format for clean screen display

           TITLE:       DATE:       TIME SPENT:
           title    task_date   duration
           --------------------------------------------
           ADDITIONAL NOTES:
           task_notes (limited to 45 chars)
        '''
        try:
            date_str = self.date.strftime('%m-%d-%Y')
        except AttributeError as ae:
            date_str = self.date.__str__()

        duration_str = self.duration.__str__()
        entry_array = [self.title, date_str, duration_str]

        fmt_string = '''
        TITLE:                                  TIME SPENT:
        {0:<40}{2:<20}
        
        DATE:
        {1:<20}

        ADDITIONAL NOTES:
        '''

        formatted_notes = textwrap.fill(
            self.notes, width=45, subsequent_indent='\t')

        return fmt_string.format(*entry_array) + formatted_notes

    def __str__(self):

        entry_str = ''

        for key in sorted(self.__dict__.keys(), reverse=True):
            if key != 'notes':
                entry_str += '%s: %s\t' % (key.upper(), self.__dict__[key])

        entry_str += '\n%s: %s\n' % ('NOTES', self.notes)

        return entry_str
