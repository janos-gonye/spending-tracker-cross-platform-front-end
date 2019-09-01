from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.exceptions import ConnectionError_
from services.auth import AuthService
from uix.popups.info import InfoPopup


Builder.load_file('screens/account/account.kv')


class AccountScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth = StatisticsService()
