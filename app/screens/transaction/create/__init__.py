from models.transaction import Transaction
from screens.transaction.save import TransactionSaveScreen
from services.exceptions import ConnectionError_
from uix.popups.info import InfoPopup


class TransactionCreateScreen(TransactionSaveScreen):
    screen_title = '[b]Create Category[/b]'
    submit_btn_text = '[b]Create[/b]'
    select_disabled = False

    def submit(self):
        if self.check_fields() is False:
            return
        transaction = Transaction(
            id=None,
            amount=self.amount_input.text,
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

    def reset_fields(self):
        self.amount_input.text = ""
        self.comment_input.text = ""
        self.date_picker.reset_today()
