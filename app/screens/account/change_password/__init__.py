from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.auth import AuthService
from services.exceptions import ConnectionError_
from uix.popups.info import InfoPopup

Builder.load_file('screens/account/change_password/change_password.kv')


class ChangePasswordScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth = AuthService()

    def change_password(self, new_password):
        valid, error = self.password_input.check()
        if not valid:
            InfoPopup(title='Field Error',
                      message=error).open()
            return
        json, error = self.auth.change_password(old_password, new_password)
        if not json:
            InfoPopup(title='Error', message=str(error)).open()
            return
        InfoPopup(title='Change Password',
                  message='Login with your new password.').open()
        self.manager.current = 'login'
        self.auth.logout()

    def reset(self):
        self.password_input.reset()

    def on_leave(self):
        self.reset()
