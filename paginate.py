def paginate_list_display(a_list):

    idx = 0
    action_list = ['N for next','P for previous','S to select the current option.']

    while not True:
        print(a_list[idx])
        if idx == 0:
            print(", ".join([action for index, action in enumerate(action_list) if index != 1]))
        elif idx == len(a_list) - 1:
            print(", ".join(action_list[1:]))
        else:
            print(", ".join(action_list))

        action = input().lower()

        if action == 'n' or action == 'next':
            idx += 1
        elif action == 'p' or action == 'previous':
            idx -= 1
        elif action == 's' or action == 'select':
            return a_list[idx]