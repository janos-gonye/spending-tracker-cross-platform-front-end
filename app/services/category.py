import constants

from models.category import Category
from services.api import ApiService
from services.exceptions import ConnectionError_


class CategoryService(ApiService):
	"""Category Service for handling CRUD operations on categories"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def create(self, category):
		pass

	def get_all(self):
		response = super().get(path=constants.API_CATEGORIES)
		payload = response[0]
		if payload is None:
			raise ConnectionError_(response[1])
		result = []
		for cat_json in payload['categories']:
			result += [Category.from_json(json=cat_json)]
		return result

	def get(self, id):
		pass

	def update(self, category):
		pass

	def delete(self, category):
		pass
