from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

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

    def submit(self):
        pass
