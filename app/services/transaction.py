import constants

from models.transaction import Transaction
from services.api import ApiService
from services.exceptions import ConnectionError_


class TransactionService(ApiService):
	"""Transaction Service for handling CRUD operations on transactions"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def create(self, transaction):
		path = self._get_path(cat_id=transaction.category.id)
		payload, error = super().post(path=path,
									  json=transaction.as_json())
		if payload is None:
			raise ConnectionError_(error)
		return Transaction.from_json(json=payload['transaction'])

	def get_all(self, category):
		cat_id = '*' if category is None else category.id
		path = self._get_path(cat_id=cat_id)
		payload, error = super().get(path=path)
		if payload is None:
			raise ConnectionError_(error)
		result = []
		for trans_json in payload['transactions']:
			result += [Transaction.from_json(json=trans_json)]
		return result

	def get(self, category, transaction_id):
		pass

	def update(self, transaction):
		pass

	def delete(self, transaction):
		path = self._get_path(cat_id=transaction.category.id,
							  trans_id=transaction.id)
		payload, error = super().delete(path=path)
		if payload is None:
			raise ConnectionError_(error)
		return Transaction.from_json(json=payload['transaction'])

	def _get_path(self, cat_id, trans_id=None):
		path = constants.API_TRANACTIONS.format(cat_id=cat_id)
		if trans_id:
			path += f"/{trans_id}"
		return path
