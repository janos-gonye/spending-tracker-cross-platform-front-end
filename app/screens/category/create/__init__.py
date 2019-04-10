from kivy.lang import Builder

from screens.category.base import CategoryScreen

Builder.load_file('screens/category/create/category_create.kv')


class CategoryCreateScreen(CategoryScreen):

    def on_enter(self):
        super().on_enter()
        if self.conn_error:
            return
        self.select.init(elements=self.categories)
