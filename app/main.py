import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition

from screens.category.list import CategoryListScreen
from screens.category.create import CategoryCreateScreen
from screens.login import LoginScreen
from screens.main import MainScreen
from screens.registration import RegistrationScreen


class SpendingTrackerApp(App):

	def build(self):
		screen_manager = ScreenManager(transition=SwapTransition())
		screen_manager.add_widget(LoginScreen(name='login'))
		screen_manager.add_widget(RegistrationScreen(name='registration'))
		screen_manager.add_widget(MainScreen(name='main'))
		screen_manager.add_widget(CategoryListScreen(name='category'))
		screen_manager.add_widget(CategoryCreateScreen(name='category_create'))
		return screen_manager


if __name__ == '__main__':
	SpendingTrackerApp().run()
