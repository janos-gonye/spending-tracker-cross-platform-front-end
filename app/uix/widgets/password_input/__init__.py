from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('uix/widgets/password_input/password_input.kv')


class PasswordInput(BoxLayout):

    def check(self):
        pwd = self.password_input.text
        confirm = self.confirm_password_input.text
        if '' in (pwd, confirm):
            return False, 'All fields required.'
        elif pwd != confirm:
            return False, "Passwords don't match!"
        return True, None

    @property
    def password(self):
        return self.password_input.text

    def reset(self):
        self.password_input.text = ''
        self.confirm_password_input.text = ''
