import constants

from events.handler import EventHandler
from models.category import Category
from services.api import ApiService
from services.exceptions import ConnectionError_


class CategoryService(ApiService):
    """Category Service for handling CRUD operations on categories"""
    categories = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for event_type in (constants.EVENT_LOGIN,
                           constants.EVENT_LOGOUT,
                           constants.EVENT_SETTINGS_CHANGE):
            EventHandler(event_type=event_type,
                         callback=self._uncache_categories)

    def create(self, category):
        payload, error = super().post(path=constants.API_CATEGORIES,
                                      json=category.as_json())
        if payload is None:
            raise ConnectionError_(error)
        self._uncache_categories()
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
        self._uncache_categories()
        return Category.from_json(json=payload['category'])

    def delete(self, category):
        path = self._get_path(category=category)
        payload, error = super().delete(path=path)
        if payload is None:
            raise ConnectionError_(error)
        self._uncache_categories()
        return Category.from_json(json=payload['category'])

    def _get_path(self, category):
        return f"{constants.API_CATEGORIES}/{category.id}"

    def _uncache_categories(self, *args):
        CategoryService.categories = None

    def merge(self, subject, target, remove_merged):
        json = {
            'subject_id': subject.id,
            'target_id': target.id,
            'remove_merged': remove_merged,
        }
        payload, error = super().post(path=constants.API_MERGE_CATEGORIES,
                                      json=json)
        if payload is None:
            raise ConnectionError_(error)
        self._uncache_categories()
        return True
