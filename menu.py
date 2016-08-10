class Menu(object):
    def __init__(self, prev, name, options):
        self.prev = prev
        self.name = name
        self.options = options.sort()

    def navigate_up(self):
        pass

    def navigate_down(self, option):
        pass

