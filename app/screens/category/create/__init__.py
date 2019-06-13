from kivy.lang import Builder

from models.category import Category
from services.exceptions import ConnectionError_
from screens.category.base import CategoryScreen
from uix.popups.info import InfoPopup


Builder.load_file('screens/category/create/category_create.kv')


class CategoryCreateScreen(CategoryScreen):

    def on_pre_enter(self):
        super().on_pre_enter()
        if self.cat_conn_error:
            return
        self.select.init(elements=self.categories)

    def submit(self):
        category = Category(
            id=None,
            title=self.title_input.text,
            description=self.description_input.text,
            parent=self.select.selected
        )
        try:
            created = self.service.create(category=category)
        except ConnectionError_ as err:
            InfoPopup(title='Error',
                      message=str(err)).open()
            return None
        InfoPopup(title='Success',
                  message="Category Successfully Created").open()
        self.reset_fields()
        self.manager.current = 'category_list'
        return created

    def reset_fields(self):
        self.title_input.text = ""
        self.description_input.text = ""
        self.select.selected = None
