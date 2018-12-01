from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.auth import AuthService


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
		if '' in [email, password]:
			return None, 'All fields required.'
		json, error = self.auth.login(email, password)
		if json:
			print('Successful Login')
			self.clear_fields()
			return
		# TODO: Inform User in a Popup Window about the Error
		print(error)

	def clear_fields(self):
		self.email_input.text = ''
		self.password_input.text = ''
