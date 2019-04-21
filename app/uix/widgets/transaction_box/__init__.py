from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from utils.date import timestamp2datetime


Builder.load_file('uix/widgets/transaction_box/transaction_box.kv')


class TransactionBox(BoxLayout):

	def __init__(self, transaction, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.category.text = f"[b]{transaction.category.history}[/b]"
		self.comment.text = f"[b]{transaction.comment}[/b]"
		self.amount = f"[b]{transaction.amount}[/b]"
		date = timestamp2datetime(transaction.processed_at)
		date_str = date.strftime("%Y.%m.%d.")
		self.date.text = f"[b]{date_str}[/b]"
