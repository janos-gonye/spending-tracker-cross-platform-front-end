from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.auth import AuthService
from uix.popups.error import ErrorPopup


Builder.load_file('screens/registration/registration.kv')


class RegistrationScreen(Screen):
	"""
	Registration Screen
	The user can registrate or navigate back to <LoginScreen>
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.auth = AuthService()

	def registrate(self, email, password, confirm_password):
		if '' in (email, password, confirm_password):
			json, error = None, 'All fields required.'
		elif password != confirm_password:		
			json, error = None, "Passwords don't match!"
		else:
			json, error = self.auth.registrate(email, password)
		if json:
			self.reset()
			self.manager.current = 'main'
			return
		ErrorPopup(title='Registration Error',
			       error=error).open()

	def reset(self):
		self.email_input.text = ''
		self.password_input.text = ''
		self.confirm_password_input.text = ''

	def on_leave(self, *args, **kwargs):
		self.reset()
		return super().on_leave(*args, **kwargs)
