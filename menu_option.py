class MenuOption(object):
    """Class to describe individual menu options"""
    def __init__(self, text, action, accepted_vals):
        self.text = text.upper()
        self.action = action.lower()
        self.accepted_vals = accepted_vals