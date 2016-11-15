import sys

import config
from entry_log import EntryLog
import interface
from work_log import WorkLog

if __name__ == '__main__':

    

    if len(sys.argv) > 2:
        log = EntryLog(sys.argv[1])
    else:
        log = EntryLog()

    init_vars = {
        'main_menu': config.MAIN_MENU,
        'search_menu': config.SEARCH_MENU,
        'date_menu': config.DATE_SEARCH_MENU,
        'duration_menu': config.DURATION_SEARCH_MENU,
        'task_menu' : config.TASK_MENU,
        'edit_menu' : config.EDIT_MENU,
        'log': log
    }
    
    work_log = WorkLog(**init_vars)

    while True:

        if work_log.action in ('main', 'search', 'date', 'duration', 'edit'):

            

            if work_log.action != 'edit':
                work_log.entry_to_display = None

            work_log.menu()

        elif work_log.action == 'create':

            work_log.create_new_entry()

        elif work_log.action == 'report':

            work_log.print_report()

        elif work_log.action == 'kw':

            prompt = {'prompt': 'enter a keyword or phrase (enter [<] to return to search menu):'}

            work_log.search_by_pattern(prompt, 'keyword search')
            
        elif work_log.action == 'pattern':

            prompt = {'prompt': 'enter a regex pattern (enter [<] to return to search menu):'}

            work_log.search_by_pattern(prompt, 'regex pattern search')

        elif work_log.action == 'date_r':

            action_prompts = [
                {'prompt': 'enter a start date (mm-dd-yy): '},
                {'prompt': 'enter an end date (mm-dd-yy): '}
            ]

            work_log.search_by_date(action_prompts, 'search by date range')

        elif work_log.action == 'date_s':
            #import pdb; pdb.set_trace()
            action_prompts = [
                {'prompt': 'select a date from above (mm-dd-yyyy): '}
            ]

            work_log.search_by_date(action_prompts, 'search by task date')

        elif work_log.action == 'duration_r':

            action_prompts = [
                {'prompt': 'enter a minimum time in minutes: '},
                {'prompt': 'enter a maximum time in minutes: '}
            ]

            work_log.search_by_duration(action_prompts, 'search by time range')

        elif work_log.action == 'duration_s':

            action_prompts = [
                {'prompt': 'enter a time (in minutes) to search'}
            ]

            work_log.search_by_duration(action_prompts, 'search by task time')

        elif work_log.action == 'results':

            work_log.process_results()

        elif work_log.action == 'e_name':
            prompt = {
                'prompt': 'enter new task name (or [<] to return to entry menu):',
                'attr' : 'title'
            }

            work_log.update_entry_att('edit entry', prompt)

        elif work_log.action == 'e_date':

            prompt = {
                'prompt': 'enter new task date (or [<] to return to entry menu):',
                'attr' : 'date'
            }

            work_log.update_entry_att('edit entry', prompt)

        elif work_log.action == 'e_duration':
            
            prompt = {
                'prompt': 'enter new task duration (or [<] to return to entry menu):',
                'attr' : 'duration'
            }

            work_log.update_entry_att('edit entry', prompt)

        elif work_log.action == 'e_notes':
            prompt = {
                'prompt': 'enter new task notes (or [<] to return to entry menu):',
                'attr' : 'notes'
            }

            work_log.update_entry_att('edit entry', prompt)

        elif work_log.action == 'save':

            work_log.save_entry()

        elif work_log.action == 'del':

            work_log.delete_entry()

        elif work_log.action == 'quit':
            try:
                file = work_log.log.save_data_to_csv()
            except IOError as ioe:
                work_log.err_msg = str(ioe)
                work_log.action = 'main'
                continue

            print('Data saved to ' + file)
            print('Exiting the log...')
            break

        else:
            work_log.reset_vars()









