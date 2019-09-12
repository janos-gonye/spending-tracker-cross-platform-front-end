from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('screens/forgot_password/forgot_password.kv')


class ForgotPasswordScreen(Screen):
    pass

    def on_leave(self):
        self.reset()

    def reset(self):
        self.email_input.text = ''
