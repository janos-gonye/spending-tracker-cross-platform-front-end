from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.exceptions import ConnectionError_
from services.statistics import StatisticsService
from uix.popups.info import InfoPopup


Builder.load_file('screens/statistics/statistics.kv')


class StatisticsScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = StatisticsService()

    def list_statistics(self):
        pass

    def export_statistics(self):
        try:
            message = self.service.export_statistics()
        except ConnectionError_ as err:
            InfoPopup(title="Error", message=str(err)).open()
            return
        InfoPopup(title="Success", message=message).open()
