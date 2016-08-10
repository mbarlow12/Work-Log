
import datetime

class Validator(object):

    """Basic input validation for the Work Log."""

    MENUS = {
        'main': [
            'c', 's', 'q', 'r',
            'create', 'search', 'quit', 'print'
        ],
        'search': [
            'keyword', 'duration', 'time', 'name', 'pattern',
            'p', 'k', 'd', 't', 'n'
        ]
    }

    def __init__(self):
        pass

    def validate_menu_option(self, option, menu_string):

        if option not in self.MENUS[menu_string]:
            raise ValueError("Please enter a valid choice from the menu.")