from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from uix.actionbars.app import AppActionBar


Builder.load_file('screens/main/main.kv')


class MainScreen(Screen):
	"""
	This is the screen that the user sees
	after successfully logging in or already logged in.
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
