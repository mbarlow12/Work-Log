
# seriese of static methods to handle all writing and reading to/from the screen
import datetime

MAIN_MENU = [
    '[C]REATE NEW ENTRY',
    '[S]EARCH EXISTING ENTRIES',
    'PRINT [R]EPORT',
    '[Q]UIT'
]

SEARCH_MENU = [
    'SEARCH BY [K]EYWORD',
    'SEARCH BY [D]ATE',
    'SEARCH BY [T]ASK DURATION',
    'SEARCH BY [P]ATTERN'
]

MENUS = {
    'main': MAIN_MENU,
    'search': SEARCH_MENU
}

def prompt_for_action(menu_name):
    print('Please choose from the following options:')

    display_menu(MENUS[menu_name])

    return input("")

def display_menu(menu):
    for option in menu:
        print("\t" + option)

def prompt_for_new_entry():
    name = prompt_for_task_name()
    duration = prompt_for_task_duration()
    notes = prompt_for_task_notes()

    return (name, duration, notes)

def prompt_for_task_name():
    return input("What's the task name?\n")

def prompt_for_task_duration():
    return input("How long did the task take?\n")

def prompt_for_task_notes():
    return input("Would you like to add any notes to the task?\n")

def display_search_results(entry_list):
    pass

def clear_screen():
    print("\033c", end="")