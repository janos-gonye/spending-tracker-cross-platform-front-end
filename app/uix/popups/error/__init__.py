from kivy.lang import Builder
from kivy.uix.popup import Popup


Builder.load_file('uix/popups/error/errorpopup.kv')


class ErrorPopup(Popup):

	def __init__(self, error, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.title = kwargs['title']
		self.label.text = "[i]{error}[/i]".format(error=error)
