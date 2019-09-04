import constants

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from services.auth import AuthService
from uix.popups.info import InfoPopup


Builder.load_file('screens/registration/registration.kv')


class RegistrationScreen(Screen):
    """
    Registration Screen
    The user can registrate or navigate back to <LoginScreen>
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth = AuthService()

    def registrate(self, email, password):
        valid, error = self.password_input.check()
        if '' in (email, password):
            json, error = None, 'All fields required.'
        elif not valid:
            json, error = None, error
        else:
            json, error = self.auth.registrate(email, password)
        if json:
            InfoPopup(title='Registration Info',
                      message=json[constants.API_DEFAULT_KEY]).open()
            self.reset()
            return
        InfoPopup(title='Registration Error',
                  message=error).open()

    def reset(self):
        self.email_input.text = ''
        self.password_input.reset()

    def on_leave(self, *args, **kwargs):
        self.reset()
        return super().on_leave(*args, **kwargs)
