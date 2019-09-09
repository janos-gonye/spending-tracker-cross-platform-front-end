from abc import ABCMeta
from abc import abstractmethod

from kivy.lang import Builder

from services.exceptions import ConnectionError_
from screens.category.base import CategoryScreen


Builder.load_file('screens/category/merge/category_merge.kv')


class CategoryMergeScreen(CategoryScreen):

    def on_pre_enter(self):
        super().on_pre_enter()
        if self.cat_conn_error:
            return
        self.cat_subject.init(elements=self.categories)
        self.cat_target.init(elements=self.categories)

    def merge(self):
        print("works!")
