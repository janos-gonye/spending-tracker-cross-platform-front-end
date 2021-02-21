import constants

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.actionbar import ActionBar

from events.handler import EventHandler
from services.auth import AuthService
from services.session import SessionService
from uix.popups.info import InfoPopup


Builder.load_file('uix/actionbars/app/app.kv')


class AppActionBar(ActionBar):
    screen_manager = ObjectProperty()
    user_email = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth = AuthService()
        EventHandler(event_type=constants.EVENT_LOGIN, callback=self.on_login)
        EventHandler(event_type=constants.EVENT_ON_SESSION_REFRESH, callback=self.on_session_refresh)

    def on_login(self, *args):
        self.set_email_label()

    def on_session_refresh(self, *args):
        self.set_email_label()

    def set_email_label(self):
        self.email_label.text = f"[b]{SessionService.email}[/b]"

    def logout(self):
        self.screen_manager.current = 'login'
        self.auth.logout()
        InfoPopup(title='Logout',
                  message='Successfully logged out.').open()
