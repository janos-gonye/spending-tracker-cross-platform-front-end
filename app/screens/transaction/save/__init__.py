from abc import ABCMeta
from abc import abstractmethod

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from screens.category.mixins import FetchCategoriesMixin
from services.transaction import TransactionService
from uix.popups.info import InfoPopup


Builder.load_file('screens/transaction/save/transaction_save.kv')


class TransactionSaveScreen(FetchCategoriesMixin, Screen):
    __metaclass__ = ABCMeta
    screen_title = None
    submit_btn_text = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = TransactionService()

    def on_pre_enter(self):
        self.fetch_categories()

    def on_enter(self):
        if self.cat_conn_error:
            InfoPopup(title='Error', message=str(self.cat_conn_error)).open()
        else:
            self.category_selector.init(elements=self.categories)
            try:
                self.category_selector.selected = self.categories[0]
            except IndexError:
                pass

    @abstractmethod
    def submit(self):
        pass

    def check_fields(self):
        if self.amount_input.text == "" or\
           self.category_selector.selected is None:
            InfoPopup(title='Error', message="Amount and category is required.").open()
            return False
        return True
