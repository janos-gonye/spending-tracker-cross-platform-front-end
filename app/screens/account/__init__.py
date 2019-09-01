from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.exceptions import ConnectionError_
from services.auth import AuthService
from uix.popups.confirm.helpers import confirm
from uix.popups.info import InfoPopup


Builder.load_file('screens/account/account.kv')


class AccountScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth_service = AuthService()

    def delete_account(self):
        confirm(
            title='Delete Account',
            question=('Are you sure you want to permanently '
                      'delete your account?'),
            confirmed=self._delete_account)

    def _delete_account(self):
        try:
            self.auth_service.delete_registration()
        except ConnectionError_ as err:
            InfoPopup(title='Error', message=str(err)).open()
        InfoPopup(title='Delete Account',
                  message='Confirmation Email Sent.').open()
