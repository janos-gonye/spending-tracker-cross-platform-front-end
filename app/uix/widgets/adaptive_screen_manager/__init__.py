import constants

from kivy.uix.screenmanager import ScreenManager

from events.handler import EventHandler


class AdaptiveScreenManager(ScreenManager):
    history = []

    def on_current(self, instance, value):
        self.history.append(self.current)
        # Don't consume memory unnecessarily
        self.history = self.history[-2:]
        super().on_current(instance, value)
        EventHandler(event_type=constants.EVENT_SESSION_EXPIRE,
                     callback=self.on_session_expire)

    def switch_back(self):
        """
        Switch back to previously active screen.
        Useful if you want adaptive back/cancel buttons.
        !!!Only works if the user is only able to go back from the screen!!!
        """
        self.current = self.history[-2]

    def on_session_expire(self, *args):
        self.current = 'login'
