from functools import partial

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty


class SelectButton(Button):
    allow_null = BooleanProperty(False)
    attr_name = StringProperty('id')
    null_text = StringProperty('None')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._selected = None
        self._elements = []
        self._init_dropdown()

    def init(self, elements):
        self._dropdown.clear_widgets()
        self._elements = elements
        if self.allow_null:
            self._add_null_btn()
        for elm in elements:
            text = getattr(elm, self.attr_name)
            btn = Button(text=text, size_hint_y=None, height=44)
            btn.bind(on_release=partial(self._on_select_elm, elm=elm))
            self._dropdown.add_widget(btn)

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, element):
        if element is None:
            self._select(text=self.null_text, elm=None)
            return
        for elm in self._elements:
            attr_value = getattr(elm, self.attr_name)
            if attr_value == getattr(element, self.attr_name):
                self._select(text=attr_value, elm=elm)
                return

    def _init_dropdown(self):
        self._dropdown = DropDown()
        self._dropdown.bind(
            on_select=lambda instance, x: setattr(self, 'text', x))
        self.bind(on_release=self._dropdown.open)

    def _select(self, text, elm):
        self._dropdown.select(text)
        self._selected = elm

    def _on_select_elm(self, btn, elm):
        self._select(text=btn.text, elm=elm)

    def _add_null_btn(self):
        btn = Button(text=self.null_text, size_hint_y=None, height=44)
        btn.bind(on_release=self._on_null_select)
        self._dropdown.add_widget(btn)

    def _on_null_select(self, btn):
        self._select(text=btn.text, elm=None)
