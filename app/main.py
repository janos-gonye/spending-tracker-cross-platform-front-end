import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.screenmanager import SwapTransition

from screens.category.create import CategoryCreateScreen
from screens.category.list import CategoryListScreen
from screens.category.update import CategoryUpdateScreen
from screens.login import LoginScreen
from screens.settings import SettingsScreen
from screens.main import MainScreen
from screens.registration import RegistrationScreen
from screens.transaction.create import TransactionCreateScreen
from screens.transaction.list import TransactionListScreen
from screens.transaction.update import TransactionUpdateScreen
from screens.transaction.create import TransactionCreateScreen
from uix.widgets.adaptive_screen_manager import AdaptiveScreenManager


class SpendingTrackerApp(App):

	def build(self):
		screen_manager = AdaptiveScreenManager(transition=SwapTransition())
		screen_manager.add_widget(LoginScreen(name='login'))
		screen_manager.add_widget(SettingsScreen(name='settings'))
		screen_manager.add_widget(RegistrationScreen(name='registration'))
		screen_manager.add_widget(MainScreen(name='main'))
		screen_manager.add_widget(CategoryListScreen(name='category_list'))
		screen_manager.add_widget(CategoryCreateScreen(name='category_create'))
		screen_manager.add_widget(CategoryUpdateScreen(name='category_update'))
		screen_manager.add_widget(TransactionListScreen(name='transaction_list'))
		screen_manager.add_widget(TransactionCreateScreen(name='transaction_create'))
		screen_manager.add_widget(TransactionUpdateScreen(name='transaction_update'))
		return screen_manager


if __name__ == '__main__':
	SpendingTrackerApp().run()
