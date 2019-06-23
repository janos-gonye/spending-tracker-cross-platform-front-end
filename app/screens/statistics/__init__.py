from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from screens.mixins import ListScreenMixin
from services.exceptions import ConnectionError_
from services.statistics import StatisticsService
from uix.popups.info import InfoPopup


Builder.load_file('screens/statistics/statistics.kv')


class StatisticsScreen(ListScreenMixin, Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = StatisticsService()

    def list_statistics(self):
        from_ = self.from_selector.timestamp
        to = self.to_selector.timestamp
        try:
            statistics = self.service.get_statistics(from_=from_, to=to)
        except ConnectionError_ as err:
            InfoPopup(title="Error", message=str(err)).open()
            return
        print(statistics)

    def export_statistics(self):
        from_ = self.from_selector.timestamp
        to = self.to_selector.timestamp
        try:
            message = self.service(from_=from_, to=to)
        except ConnectionError_ as err:
            InfoPopup(title="Error", message=str(err)).open()
            return
        InfoPopup(title="Success", message=message).open()
