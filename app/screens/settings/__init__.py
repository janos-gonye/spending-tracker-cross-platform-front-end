from kivy.lang import Builder

from kivy.uix.screenmanager import Screen


Builder.load_file('screens/settings/settings.kv')


class SettingsScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.protocol_select.init(elements=['HTTP', 'HTTPS'])
        self.protocol_select.selected = 'HTTPS'

    def save(self):
        pass
