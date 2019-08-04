import re

from kivy.uix.textinput import TextInput


class NumericInput(TextInput):

    pat = re.compile('[0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if re.match(pat, substring):
            s = substring
        else:
            s = ''
        return super().insert_text(s, from_undo=from_undo)
