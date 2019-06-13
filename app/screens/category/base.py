from kivy.uix.screenmanager import Screen

from screens.category.mixins import FetchCategoriesMixin
from services.category import CategoryService
from uix.popups.info import InfoPopup


class CategoryScreen(FetchCategoriesMixin, Screen):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = CategoryService()

    def on_pre_enter(self):
        self.fetch_categories()

    def on_enter(self):
        self.show_if_error()

    def show_if_error(self):
        if self.cat_conn_error:
            InfoPopup(title='Error',
                      message=str(self.cat_conn_error)).open()
