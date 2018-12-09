from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.actionbar import ActionBar

from services.auth import AuthService
from uix.popups.info import InfoPopup


Builder.load_file('uix/actionbars/app/app.kv')


class AppActionBar(ActionBar):
	screen_manager = ObjectProperty()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.auth = AuthService()

	def logout(self):
		self.screen_manager.current = 'login'
		self.auth.logout()
		InfoPopup(title='Logout',
				  message='Successfully logged out.').open()
