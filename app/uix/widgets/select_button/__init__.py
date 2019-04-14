from functools import partial

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class SelectButton(Button):

    def init(self, elements):
        self._elements = elements
        dropdown = DropDown()
        for elm in elements:
            text = getattr(elm, self.attr_name)
            btn = Button(text=text, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        dropdown.bind(on_select=lambda instance, x: setattr(self, 'text', x))
        self.bind(on_release=dropdown.open)

    @property
    def selected(self):
        for elm in self._elements:
            if getattr(elm, self.attr_name) == self.text:
                return elm
        return None
