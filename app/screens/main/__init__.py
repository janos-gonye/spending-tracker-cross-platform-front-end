from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from uix.actionbars.app import AppActionBar

from screens.mixins import AdaptiveCancelForTransactionCreateScreenMixin


Builder.load_file('screens/main/main.kv')


class MainScreen(AdaptiveCancelForTransactionCreateScreenMixin, Screen):
	"""
	This is the screen that the user sees
	after successfully logging in or already logged in.
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
