from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.actionbar import ActionBar

from events.handler import EventHandler
from services.auth import AuthService
from uix.popups.info import InfoPopup


Builder.load_file('uix/actionbars/app/app.kv')


class AppActionBar(ActionBar):
	screen_manager = ObjectProperty()
	user_email = ""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.auth = AuthService()
		EventHandler(event_type='on_login', callback=self.on_login)

	def on_login(self, *args):
		self.email_label.text = f"[b]{args[0]}[/b]"

	def logout(self):
		self.screen_manager.current = 'login'
		self.auth.logout()
		InfoPopup(title='Logout',
				  message='Successfully logged out.').open()
