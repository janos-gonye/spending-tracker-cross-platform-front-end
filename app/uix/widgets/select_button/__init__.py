from functools import partial

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class SelectButton(Button):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._selected = None
        self._elements = []
        self._init_dropdown()

    def init(self, elements):
        self._elements = elements
        for elm in elements:
            text = getattr(elm, self.attr_name)
            btn = Button(text=text, size_hint_y=None, height=44)
            btn.bind(on_release=partial(self._on_select, elm=elm))
            self._dropdown.add_widget(btn)

    @property
    def selected(self):
        return self._selected

    def _init_dropdown(self):
        self._dropdown = DropDown()
        self._dropdown.bind(
            on_select=lambda instance, x: setattr(self, 'text', x))
        self.bind(on_release=self._dropdown.open)

    def _on_select(self, btn, elm):
        self._dropdown.select(btn.text)
        self._selected = elm
