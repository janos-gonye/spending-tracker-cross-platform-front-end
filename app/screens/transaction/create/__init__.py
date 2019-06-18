from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from models.transaction import Transaction
from screens.category.mixins import FetchCategoriesMixin
from uix.popups.info import InfoPopup


Builder.load_file('screens/transaction/create/transaction_create.kv')


class TransactionCreateScreen(FetchCategoriesMixin, Screen):

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

    def submit(self):
        self.check_fields()

    def check_fields(self):
        if self.number_input.text == "" or self.comment_input.text == "" or\
           self.category_selector.selected is None:
            InfoPopup(title='Error', message="All fields required.").open()

    def on_leave(self):
        self.number_input.text = ""
        self.comment_input.text = ""
        self.date_picker.reset_today()
