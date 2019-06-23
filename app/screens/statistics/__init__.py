from kivy.lang import Builder

from kivy.uix.screenmanager import Screen


Builder.load_file('screens/statistics/statistics.kv')


class StatisticsScreen(Screen):

    def list_statistics(self):
        pass

    def export_statistics(self):
        pass
