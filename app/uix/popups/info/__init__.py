from kivy.lang import Builder
from kivy.uix.popup import Popup


Builder.load_file('uix/popups/info/info.kv')


class InfoPopup(Popup):

    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = kwargs['title']
        self.label.text = "[i]{message}[/i]".format(message=message)
