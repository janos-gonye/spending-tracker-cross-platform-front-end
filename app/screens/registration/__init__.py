from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.auth import AuthService


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
		if '' in [email, password, confirm_password]:
			return None, 'All fields required.'
		if password != confirm_password:		
			return None, "Passwords don't match!"
		json, error = self.auth.registrate(email, password)
		if json:
			print('Email Sent')
			return
		# TODO: Inform User in a Popup Window about the error
		print(error)
