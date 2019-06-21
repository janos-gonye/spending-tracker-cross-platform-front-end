from abc import ABCMeta
from abc import abstractmethod

from kivy.lang import Builder

from services.exceptions import ConnectionError_
from screens.category.base import CategoryScreen


Builder.load_file('screens/category/create/category_save.kv')


class CategorySaveScreen(CategoryScreen):
    __metaclass__ = ABCMeta
    screen_title = None
    submit_btn_text = None

    def on_pre_enter(self):
        super().on_pre_enter()
        if self.cat_conn_error:
            return
        self.select.init(elements=self.categories)

    @abstractmethod
    def submit(self):
        pass
