from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from screens.mixins import ListScreenMixin
from services.exceptions import ConnectionError_
from services.statistics import StatisticsService
from uix.popups.info import InfoPopup
from utils.date import timestamp2datetime


Builder.load_file('screens/statistics/statistics.kv')


class StatisticsScreen(Screen):

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
        self.statistics_lbl.text = ""
        from_ = timestamp2datetime(timestamp=from_)
        to = timestamp2datetime(timestamp=to)
        all_cost = self.calc_all_cost(statistics=statistics)
        fmt = "%Y-%m-%d"
        text = "[i]" + from_.strftime(fmt) + " -> " + to.strftime(fmt) + "\n\n"
        text += f"All spending: {all_cost}\n\n"
        # List main categories
        for category in statistics:
            text += self.statistics_for(category=category,
                                        include_children=False)
        text += "\n"
        # List categories with their children detailed
        for category in statistics:
            text += self.statistics_for(category=category) + "\n"
        self.statistics_lbl.text = text + '[/i]'

    def export_statistics(self):
        from_ = self.from_selector.timestamp
        to = self.to_selector.timestamp
        try:
            message = self.service(from_=from_, to=to)
        except ConnectionError_ as err:
            InfoPopup(title="Error", message=str(err)).open()
            return
        InfoPopup(title="Success", message=message).open()

    def statistics_for(self, category, indent=0, include_children=True):
        key = list(category.keys())[0]
        sum_ = int(category[key]['sum'])
        text = ""
        if sum_ != 0:
            text = "{indent}{key}: {sum_}\n".format(indent=" " * indent,
                                            key=key, sum_=sum_)
        if include_children is True:
            for child in category[key]['children']:
                text += " " * indent + self.statistics_for(category=child,
                                                           indent=indent+4)
        return text

    def calc_all_cost(self, statistics):
        all_cost = 0
        for category in statistics:
            key = list(category.keys())[0]
            all_cost += int(category[key]['sum'])
        return all_cost
