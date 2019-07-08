import constants

from models.category import Category
from services.api import ApiService
from services.exceptions import ConnectionError_


class CategoryService(ApiService):
	"""Category Service for handling CRUD operations on categories"""
	categories = None

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def create(self, category):
		payload, error = super().post(path=constants.API_CATEGORIES,
									  json=category.as_json())
		if payload is None:
			raise ConnectionError_(error)
		CategoryService.categories = None
		return Category.from_json(json=payload['category'])

	def get_all(self):
		if CategoryService.categories:
			return CategoryService.categories
		payload, error = super().get(path=constants.API_CATEGORIES)
		if payload is None:
			raise ConnectionError_(error)
		result = []
		for cat_json in payload['categories']:
			result += [Category.from_json(json=cat_json)]
		CategoryService.categories = result
		return result

	def get(self, id):
		path = self._get_path(category=category)
		payload, error = super().get(path=path)
		if payload is None:
			raise ConnectionError_(error)
		return Category.from_json(json=payload['category'])

	def update(self, category):
		path = self._get_path(category=category)
		payload, error = super().patch(path=path,
									   json=category.as_json())
		if payload is None:
			raise ConnectionError_(error)
		CategoryService.categories = None
		return Category.from_json(json=payload['category'])

	def delete(self, category):
		path = self._get_path(category=category)
		payload, error = super().delete(path=path)
		if payload is None:
			raise ConnectionError_(error)
		CategoryService.categories = None
		return Category.from_json(json=payload['category'])

	def _get_path(self, category):
		return f"{constants.API_CATEGORIES}/{category.id}"
