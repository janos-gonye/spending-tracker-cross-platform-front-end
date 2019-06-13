from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from screens.category.base import CategoryScreen
from uix.popups.info import InfoPopup


Builder.load_file('screens/transaction/list/transaction_list.kv')


class TransactionListScreen(CategoryScreen):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.init_scroll_list()

	def on_enter(self):
		super().on_enter()
		if not self.cat_conn_error:
			self.filter.init(categories=self.categories)

	def init_scroll_list(self):
		# Necessary to scroll
		self.list.bind(minimum_height=self.list.setter('height'))
