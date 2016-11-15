
# seriese of static methods to handle all writing and reading to/from the screen
import datetime

from entry import Entry
from menu import Menu
from menu_option import MenuOption

DATE_FMT = '%m-%d-%Y'
TIME_FMT = '%Hh%Mm%Ss'

# test data
t_date = datetime.date.today()
t_dur = datetime.timedelta(minutes=44)
t_name = 'test name'
t_notes = 'herer are some notes, I have not spelled them very wyll. I also need to make them longer'
t_entry = Entry(id_num=444, title=t_name, date=t_date, duration=t_dur, notes=t_notes)

def display_menu(menu, entry_to_display=None):

    if entry_to_display:
        print(entry_to_display.string_format() + '\n')

    # menu is list of MenuOptions
    for option in menu:
        print('\t' + option.text)

def get_action_option(options):
    '''@param options - list of MenuOption objects
       @return string/None - corresponding action string or None

       Returns the action from the menu item based on the provided user
       selection.'''

    selection = input()

    for option in options:
        if selection in option.accepted_vals:
            return option.action, selection

    return None, selection

def get_action_input(action_opt, entry_to_display=None):
    # action_opt is a single dict of prompt and the attributes to which they correspond

    if entry_to_display:
        print(entry_to_display.string_format())

    return input(action_opt['prompt'].upper() + '\n')

def write_header(header_text, err_msg=None):
    '''Displays formatted header text
    ------------------------------------------------------------
        TEXT FOR DISPLAY HERE
    ------------------------------------------------------------
    '''
    clear_screen()

    print('-' * 60)
    print('\t' + header_text.upper())
    print('-' * 60)

    if err_msg:
        print('\t*** ERROR: ' + err_msg + ' ***\n')

def get_entry_from_results(results, header_text, options):
    '''@param list - list of returned search results
       @param string - format string do display in header
       @param list - list of MenuOption objects
       @return tuple(string, mixed) - action string and mixed object (usu. Entry)

       Fully renders/refreshes screen while iterating through each result in
       provided list. Returns the selected result and corresponding action.'''

    idx = 0
    err_msg = None

    while True:

        display_options = options

        write_header(header_text.format((idx + 1), len(results)), err_msg)

        if idx == 0:
            display_options = [opt for opt in options if opt.action != 'prev']

        if idx == len(results) - 1:

            display_options = [opt for opt in options if opt.action != 'next']

            if idx == 0:

                display_options = [opt for opt in display_options if opt.action != 'prev']

        display_menu(display_options, results[idx])

        action, sel = get_action_option(display_options)

        if action == 'next':
            idx += 1
        elif action == 'prev':
            idx -= 1
        elif not action:
            err_msg = '{} not available. Select again.'.format(sel)
            continue
        else:
            return action, results[idx]

def display_list_results(result_list, result_type='date'):
    # result_list could be list of dates or entries

    for result in result_list:
        if result_type == 'date':
            result = '\t' + result.strftime(DATE_FMT)
        print('{}\n'.format(result))

def clear_screen():
    print("\033c", end="")







