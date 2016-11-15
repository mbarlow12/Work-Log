
import datetime

class Validator(object):

    """Basic input validation for the Work Log."""

    MENUS = {
        'main': [
            'c', 's', 'q', 'r',
            'create', 'search', 'quit', 'print'
        ],
        'search': [
            'keyword', 'duration', 'time', 'name', 'pattern', 'main',
            'p', 'k', 'd', 't', 'n', 'm'
        ],
        'task': [
            'edit', 'view', 'search', 'main',
            'e', 'v', 's', 'm'
        ],
        'edit': [
            'name', 'notes', 'duration',
            'n', 't', 'd'
        ]
    }

    def __init__(self):
        pass

    def validate_menu_option(self, option, menu_string):

        if option not in self.MENUS[menu_string]:
            raise ValueError("Please enter a valid choice from the menu.")

    def validate_duration(self, duration_string):
        try:
            minutes_spent = int(duration_string)
        except ValueError as ve:
            raise ve("You must enter an integer for the number of minutes.")

        if int(minutes_spent) > (24 * 60):
            raise ValueError("Tasks cannot be longer than 24hrs.")

    def validate_option_selection(self, selection, option_list):
        if selection <= 0:
            raise ValueError("You must select one of the above options.")
        elif selection > len(option_list):
            raise ValueError("You must select one of the above options.")

    def validate_unique_task(new_task, task_list):
        if new_task.name in [entry.name for entry in task_list]:
            raise ValueError("Task name must be unique.")
