from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.config import ConfigService
from uix.popups.info import InfoPopup


Builder.load_file('screens/settings/settings.kv')


class SettingsScreen(Screen):
    hint_text = (
        "[i]Configure application which server to connect to\n"
        "Hint: HTTP Default Port: 80, HTTPS Default Port: 443\n"
        "[color=ff0000]Never use HTTP in production![/color][/i]")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.protocol_select.init(elements=['HTTP', 'HTTPS'])

    def on_pre_enter(self):
        protocol = ConfigService.get_protocol()
        if protocol != '':
            self.protocol_select.selected = protocol.upper()
        self.host_input.text = ConfigService.get_host()
        self.port_input.text = str(ConfigService.get_port())

    def save(self):
        error = None
        protocol = self.protocol_select.selected
        host = self.host_input.text
        port = self.port_input.text
        if protocol is None or host == '' or port == '':
            InfoPopup(title="Error", message="All fields required.").open()
            return False
        try:
            if not (0 < int(port) <= 65535):
                raise ValueError
        except ValueError:
            error = "Port must be a number between 0 and 65535."
            InfoPopup(title="Error", message=error).open()
            return False
        ConfigService.set_protocol(protocol)
        ConfigService.set_host(host)
        ConfigService.set_port(port)
        InfoPopup(title="Success",
                  message="Settings Successfully Updated").open()
        self.manager.current = 'login'
        return True
