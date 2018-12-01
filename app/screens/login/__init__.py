from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.auth import AuthService
from services.token import TokenService


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
		if self.auth.login(email, password):
			print('Successful Login')
		# TODO: Inform User in a Popup Window about the Error
