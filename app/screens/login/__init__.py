from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.auth import AuthService
from uix.popups.info import InfoPopup


Builder.load_file('screens/login/login.kv')


class LoginScreen(Screen):
	"""
	This is the screen that the user sees
	when opeing the application (if not logged in)

	The user can login or switch to registration screen
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.auth = AuthService()

	def login(self, email, password):
		if '' in (email, password):
			json, error = None, 'All fields required.'
		else:
			json, error = self.auth.login(email, password)
		if json:
			# self.manager.current = 'main'
			self.reset()
			return
		InfoPopup(title='Login Error',
				  message=error).open()

	def reset(self):
		self.email_input.text = ''
		self.password_input.text = ''

	def on_leave(self, *args, **kwargs):
		self.reset()
		return super().on_leave(*args, **kwargs)
