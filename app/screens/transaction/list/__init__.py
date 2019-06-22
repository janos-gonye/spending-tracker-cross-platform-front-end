from functools import partial

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from screens.category.mixins import FetchCategoriesMixin
from services.transaction import TransactionService
from services.exceptions import ConnectionError_
from uix.popups.confirm.helpers import confirm
from uix.popups.info import InfoPopup
from uix.widgets.transaction_box import TransactionBox


Builder.load_file('screens/transaction/list/transaction_list.kv')


class TransactionListScreen(FetchCategoriesMixin, Screen):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.init_scroll_list()
		self.service = TransactionService()

	def on_pre_enter(self):
		self.fetch_categories()
		self.list.clear_widgets()
		if self.cat_conn_error:
			InfoPopup(title='Error',
					  message=str(self.cat_conn_error)).open()
		else:
			self.filter.init(categories=self.categories)

	def delete_transaction(self, widget, transaction):
		def delete():
			try:
				self.service.delete(transaction=transaction)
			except ConnectionError_ as err:
				InfoPopup(title='Error', message=str(err)).open()
			else:
				self.list.remove_widget(widget)
		confirm(title='Delete Transaction',
				question=f"Are you sure?",
				confirmed=delete)

	def update_transaction(self, transaction):
		self.manager.get_screen('transaction_update').transaction = transaction
		self.manager.current = 'transaction_update'

	def list_transactions(self):
		category = self.filter.selected_category
		from_, to = self.filter.timerange
		try:		
			transactions = self.service.get_all(
				category=category, from_=from_, to=to)
		except ConnectionError_ as err:
			InfoPopup(title='Error', message=str(err)).open()
			return
		transactions.sort(key=lambda t: t.processed_at)
		self.list.clear_widgets()
		for trans in transactions:
			trans_box = TransactionBox(transaction=trans)
			trans_box.remove_btn.on_release = partial(self.delete_transaction,
													  widget=trans_box,
													  transaction=trans)
			trans_box.update_btn.on_release = partial(self.update_transaction,
													  transaction=trans)
			self.list.add_widget(trans_box)

	def init_scroll_list(self):
		# Necessary to scroll
		self.list.bind(minimum_height=self.list.setter('height'))
