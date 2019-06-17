from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('uix/widgets/transaction_box/transaction_box.kv')


class TransactionBox(BoxLayout):

	def __init__(self, transaction, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.category.text = f"[b]{transaction.category.history}[/b]"
		self.comment.text = f"[b]{transaction.comment}[/b]"
		self.amount = f"[b]{transaction.amount}[/b]"
		date = transaction.processed_at.strftime("%Y.%m.%d.")
		self.date.text = f"[b]{date}[/b]"
