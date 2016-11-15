

from menu_option import MenuOption

# menu initialization/configuration
MAIN = MenuOption('[m] - main menu', 'main', ('m', 'main'))

CREATE = MenuOption('[c] - create new entry', 'create', ('c', 'create'))
SEARCH = MenuOption('[s] - search menu', 'search', ('s', 'search'))
PRINT_REPORT = MenuOption('[p] - print report', 'report', ('p', 'r', 'print', 'report', 'print report'))
QUIT = MenuOption('[q] - quit', 'quit', ('q', 'quit'))

KW_SEARCH = MenuOption('[k] - search by keyword', 'kw', ('k', 'keyword'))
PATTERN_SEARCH = MenuOption('[p] - search by regex pattern', 'pattern', ('p', 'r', 'pattern', 'regex', 'regex pattern'))
DATE_SEARCH = MenuOption('[d] - search by date', 'date', ('date', 'd'))
DURATION_SEARCH = MenuOption('[r] - search by task duration', 'duration', ('duration', 'r'))

S_DATE_SEARCH = MenuOption('[d] - search by single date', 'date_s', ('single date', 'd'))
R_DATE_SEARCH = MenuOption('[g] - search by date range', 'date_r', ('date range', 'range', 'g'))

S_DURATION_SEARCH = MenuOption('[d] - search by single duration', 'duration_s', ('single duration', 'd'))
R_DURATION_SEARCH = MenuOption('[g] - search by duration range', 'duration_r', ('g', 'duration range'))

DEL_TASK = MenuOption('[d] - delete task', 'del', ('d', 'delete'))
EDIT_TASK = MenuOption('[e] - edit task details', 'edit', ('e', 'edit'))
NEXT = MenuOption('[n] - next result', 'next', ('n', 'next'))
PREV = MenuOption('[p] - previous result', 'prev', ('p', 'prev'))

UPDATE_NAME = MenuOption('[t] - update task name', 'e_name', ('name', 't'))
UPDATE_DATE = MenuOption('[d] - update task date', 'e_date', ('date', 'd'))
UPDATE_DURATION = MenuOption('[r] - update task duration', 'e_duration', ('r', 'duration'))
UPDATE_NOTES = MenuOption('[n] - update task notes', 'e_notes', ('n', 'note'))
SAVE = MenuOption('[s] - save details', 'save', ('s', 'save'))

MAIN_MENU = [
    CREATE,
    SEARCH,
    PRINT_REPORT,
    QUIT
]

SEARCH_MENU = [
    KW_SEARCH,
    DATE_SEARCH,
    DURATION_SEARCH,
    PATTERN_SEARCH,
    MAIN,
    QUIT
]

DATE_SEARCH_MENU = [
    S_DATE_SEARCH,
    R_DATE_SEARCH,
    SEARCH,
    MAIN,
    QUIT
]

DURATION_SEARCH_MENU = [
    S_DURATION_SEARCH,
    R_DURATION_SEARCH,
    SEARCH,
    MAIN,
    QUIT
]

TASK_MENU = [
    EDIT_TASK,
    DEL_TASK,
    NEXT,
    PREV,
    SEARCH,
    MAIN,
    QUIT
]

EDIT_MENU = [
    UPDATE_NAME,
    UPDATE_DATE,
    UPDATE_DURATION,
    UPDATE_NOTES,
    SEARCH,
    MAIN,
    QUIT
]