from kivy.uix.screenmanager import Screen

from services.category import CategoryService
from services.exceptions import ConnectionError_
from uix.popups.info import InfoPopup


class CategoryScreen(Screen):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = CategoryService()
        self.conn_error = None

    def on_pre_enter(self):
        try:
            self.categories = self.service.get_all()
        except ConnectionError_ as err:
            self.conn_error = err
    
    def on_enter(self):
        if self.conn_error:
            InfoPopup(title='Connection Error',
                      message=str(self.conn_error)).open()
