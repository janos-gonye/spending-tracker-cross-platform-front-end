from kivy.uix.screenmanager import Screen

from services.category import CategoryService
from services.exceptions import ConnectionError_
from uix.popups.info import InfoPopup


class CategoryScreen(Screen):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = CategoryService()

    def on_pre_enter(self):
        self.fetch_categories()

    def on_enter(self):
        self.show_if_error()

    def fetch_categories(self):
        try:
            self.categories = self.service.get_all()
            self.cat_conn_error = None
        except ConnectionError_ as err:
            self.cat_conn_error = err
            self.categories = []

    def show_if_error(self):
        if self.cat_conn_error:
            InfoPopup(title='Error',
                      message=str(self.cat_conn_error)).open()
