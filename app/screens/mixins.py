class AdaptiveCancelForTransactionCreateScreenMixin:

    def switch_to_transaction_create_screen(self):
        trans_create_screen = self.manager.get_screen('transaction_create')
        trans_create_screen.back_to_screen = self.manager.current
        self.manager.current = 'transaction_create'
