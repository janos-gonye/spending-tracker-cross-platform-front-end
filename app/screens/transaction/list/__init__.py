from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from screens.category.mixins import FetchCategoriesMixin
from services.transaction import TransactionService
from services.exceptions import ConnectionError_
from uix.popups.info import InfoPopup


Builder.load_file('screens/transaction/list/transaction_list.kv')


class TransactionListScreen(FetchCategoriesMixin, Screen):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.init_scroll_list()
		self.service = TransactionService()

	def on_pre_enter(self):
		self.fetch_categories()

	def on_enter(self):
		if self.cat_conn_error:
			InfoPopup(title='Error',
					  message=str(self.cat_conn_error)).open()
		else:
			self.filter.init(categories=self.categories)

	def list_transactions(self):
		cat = self.filter.selected_category
		print(self.fetch_transactions(category=cat))

	def fetch_transactions(self, category):
		try:
			return self.service.get_all(category=category)
		except ConnectionError_ as err:
			InfoPopup(title='Error', message=str(err)).open()

	def init_scroll_list(self):
		# Necessary to scroll
		self.list.bind(minimum_height=self.list.setter('height'))
