from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from models.transaction import Transaction
from screens.category.mixins import FetchCategoriesMixin
from services.transaction import TransactionService
from services.exceptions import ConnectionError_
from uix.popups.info import InfoPopup


Builder.load_file('screens/transaction/create/transaction_create.kv')


class TransactionCreateScreen(FetchCategoriesMixin, Screen):

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

    def submit(self):
        if self.check_fields() == False:
            return
        transaction = Transaction(
            id=None,
            amount=self.number_input.text,
            comment=self.comment_input.text,
            category=self.category_selector.selected,
            processed_at=self.date_picker.timestamp)
        try:
            created = self.service.create(transaction=transaction)
        except ConnectionError_ as err:
            InfoPopup(title='Error', message=str(err)).open()
            return None
        InfoPopup(title="Success",
                  message="Transaction Successfully Created").open()
        self.reset_fields()
        self.manager.switch_back()
        return created

    def check_fields(self):
        if self.number_input.text == "" or\
           self.category_selector.selected is None:
            InfoPopup(title='Error', message="All fields required.").open()
            return False
        return True

    def reset_fields(self):
        self.number_input.text = ""
        self.comment_input.text = ""
        self.date_picker.reset_today()
