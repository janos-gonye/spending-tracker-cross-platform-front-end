import calendar
from datetime import datetime
from functools import partial

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout

from utils.date import datetime2timestamp
from utils.date import timestamp2datetime


Builder.load_file('uix/widgets/date_picker/date_picker.kv')
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


class DatePicker(BoxLayout):
    dt = datetime.now()
    year = NumericProperty(dt.year)
    month = NumericProperty(dt.month)
    day = NumericProperty(dt.day)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self._init, 0)

    def _init(self, dt):
        self._create_lists()
        self._set_values()
        self._bind_callbacks()

    def reset_today(self):
        self.year = self.dt.year
        self.month = self.dt.month
        self.day = self.dt.day

    def _create_lists(self):
        dt = datetime.now()
        self.year_select.init(elements=range(2016, dt.year + 1))
        self.month_select.init(elements=MONTHS)

    def _set_values(self):
        self.year_select.selected = self.year
        self.month_select.selected = MONTHS[self.month - 1]
        self._update_day_list()
        self.day_select.selected = self.day

    def _bind_callbacks(self):
        self.year_select._dropdown.on_select = partial(self._set_year)
        self.month_select._dropdown.on_select = partial(self._set_month)
        self.day_select._dropdown.on_select = partial(self._set_day)

    def _set_year(self, value):
        self.year = int(value)

    def _set_month(self, value):
        self.month = MONTHS.index(value) + 1

    def _set_day(self, value):
        self.day = int(value)

    def on_year(self, instance, value):
        self.year_select.selected = self.year
        self._update_day_list()

    def on_month(self, instance, value):
        self.month_select.selected = MONTHS[self.month - 1]
        self._update_day_list()

    def on_day(self, instance, value):
        self.day_select.selected = self.day

    def _update_day_list(self):
        days = calendar.monthrange(self.year, self.month)[1]
        self.day_select.init(elements=range(1, days + 1))
        if self.day > days:
            self.day = days

    def set(self, year=None, month=None, day=None):
        if year:
            self._set_year(year)
        if month:
            self._set_month(MONTHS[month - 1])
        if day:
            self._set_day(day)

    @property
    def timestamp(self):
        return int(datetime2timestamp(
            datetime(self.year, self.month, self.day)))
