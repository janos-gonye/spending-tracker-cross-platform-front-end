from utils.date import timestamp2datetime
from utils.date import datetime2timestamp

from models.category import Category


class Transaction:

	def __init__(self, id, amount, comment, category, processed_at):
		"""
		Category can be both 'Category' instance or JSON object.
		"""
		self.id = id
		self.amount = int(amount)
		self.comment = comment
		if isinstance(category, Category):
			self.category = category
		else:
			self.category = Category.from_json(json=category)
		self.processed_at = timestamp2datetime(timestamp=processed_at)

	def as_json(self):
		return {
			'id': self.id,
			'amount': self.amount,
			'comment': self.comment,
			'processed_at': datetime2timestamp(date=self.processed_at),
		}

	@staticmethod
	def from_json(json):
		return Transaction(
			id=json['id'],
			comment=json['comment'],
			amount=json['amount'],
			category=json['category'],
			processed_at=json['processed_at'],
		)
