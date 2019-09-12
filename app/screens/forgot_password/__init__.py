from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.auth import AuthService
from uix.popups.info import InfoPopup

Builder.load_file('screens/forgot_password/forgot_password.kv')


class ForgotPasswordScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth = AuthService()

    def submit(self):
        email = self.email_input.text
        if email == '':
            InfoPopup(title='Error', message='Email field required.').open()
            return
        json, error = self.auth.forgot_password(email)
        if not json:
            InfoPopup(title='Error', message=str(error)).open()
            return
        InfoPopup(title='Forgot Password',
                  message='Email to reset your password sent.').open()
        self.manager.current = 'login'

    def on_leave(self):
        self.reset()

    def reset(self):
        self.email_input.text = ''
