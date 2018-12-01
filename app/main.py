import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition

from screens.login import LoginScreen
from screens.registration import RegistrationScreen


class SpendingTrackerApp(App):

	def build(self):
		screen_manager = ScreenManager(transition=SwapTransition())
		screen_manager.add_widget(LoginScreen(name='login'))
		screen_manager.add_widget(RegistrationScreen(name='registration'))
		return screen_manager


if __name__ == '__main__':
	SpendingTrackerApp().run()
