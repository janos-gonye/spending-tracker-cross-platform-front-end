from models.transaction import Transaction
from screens.transaction.save import TransactionSaveScreen
from services.exceptions import ConnectionError_
from uix.popups.info import InfoPopup


class TransactionUpdateScreen(TransactionSaveScreen):
    screen_title = '[b]Update Category[/b]'
    submit_btn_text = '[b]Update[/b]'
    transaction = None

    def on_enter(self):
        super().on_enter()
        self.amount_input.text = str(self.transaction.amount)
        self.comment_input.text = self.transaction.comment
        self.category_selector.selected = self.transaction.category
        self.date_picker.set(year=self.transaction.processed_at.year,
                             month=self.transaction.processed_at.month,
                             day=self.transaction.processed_at.day)

    def submit(self):
        if self.check_fields() == False:
            return
        transaction = Transaction(
            id=self.transaction.id,
            amount=self.amount_input.text,
            comment=self.comment_input.text,
            category=self.category_selector.selected,
            processed_at=self.date_picker.timestamp)
        try:
            created = self.service.update(transaction=transaction)
        except ConnectionError_ as err:
            InfoPopup(title='Error', message=str(err)).open()
            return None
        InfoPopup(title="Success",
                  message="Transaction Successfully Updated").open()
        self.reset_fields()
        self.manager.current = 'transaction_list'
        return created

    def reset_fields(self):
        self.amount_input.text = ""
        self.comment_input.text = ""
        self.date_picker.reset_today()
