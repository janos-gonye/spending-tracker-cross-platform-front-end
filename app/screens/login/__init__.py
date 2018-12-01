from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file('screens/login/login.kv')


class LoginScreen(Screen):
	"""
	This is the screen that the user sees
	when opeing the application (if not logged in)

	The user can login or switch to registration screen
	"""
	pass
