from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


Builder.load_file('uix/widgets/transaction_filter/transaction_filter.kv')


class TransactionFilter(BoxLayout):

	def init(self, categories):
		self.category_selector.init(elements=categories)

	@property
	def timerange(self):
		return (
			self.from_selector.timestamp,
			self.to_selector.timestamp + 24 * 3600 - 1,  # +1 day - 1 second
		)

	@property
	def selected_category(self):
		return self.category_selector.selected

	@property
	def filters(self):
		return {
			'category': self.selected_category,
			'timerange': self.timerange,
		}
