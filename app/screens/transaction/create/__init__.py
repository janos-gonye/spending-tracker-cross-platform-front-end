from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file('screens/transaction/create/transaction_create.kv')


class TransactionCreateScreen(Screen):

    def submit(self):
        pass
