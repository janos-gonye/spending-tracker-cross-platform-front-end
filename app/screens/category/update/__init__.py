from kivy.lang import Builder

from models.category import Category
from services.exceptions import ConnectionError_
from screens.category.base import CategoryScreen
from uix.popups.info import InfoPopup


Builder.load_file('screens/category/update/category_update.kv')


class CategoryUpdateScreen(CategoryScreen):

    def on_pre_enter(self):
        super().on_pre_enter()
        if not self.conn_error:
            self.title_input.text = self.category.title
            self.description_input.text = self.category.description
            self.select.selected = self.category.parent

    def on_enter(self):
        super().on_enter()
        if self.conn_error:
            return
        self.select.init(elements=self.get_elements())

    def submit(self):
        category = Category(
            id=self.category.id,
            title=self.title_input.text,
            description=self.description_input.text,
            parent=self.select.selected
        )
        try:
            updated = self.service.update(category=category)
        except ConnectionError_ as err:
            InfoPopup(title='Error',
                      message=str(err)).open()
            return None
        InfoPopup(title='Success',
                  message="Category Successfully Updated").open()
        self.manager.current = 'category_list'
        return updated

    def get_elements(self):
        """
        Filter out elements that are descendents
        of the category being updated.
        """
        elements = []
        for category in self.categories:
            if category.id == self.category.id:
                continue
            ancestors_id = map(lambda cat: cat.id, category.get_ancestors())
            if self.category.id not in ancestors_id:
                elements.append(category)
        return elements
