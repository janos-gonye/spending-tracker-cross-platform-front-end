import constants

from services.api import ApiService
from services.mixins import EventEmitterMixin
from services.session import SessionService


class AuthService(ApiService):
    """Authentication Service for handling registration, login etc."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def registrate(self, email, password):
        json = {
            'email': email,
            'password': password
        }
        return super().post(path=constants.API_AUTH_REGISTRATION, json=json)

    def delete_registration(self):
        return super().delete(path=constants.API_AUTH_REGISTRATION)

    def login(self, email, password):
        json = {
            'email': email,
            'password': password,
        }
        json, error = super().post(path=constants.API_AUTH_LOGIN, json=json)
        if json:
            SessionService.create(email=email, token=json['token'])
        return json, error

    def logout(self):
        SessionService.destroy()
        return True

    def verify_stored_session(self):
        email = SessionService.email
        token = SessionService.token
        if email is None or token is None:
            return False
        json, error = super().get(path=constants.API_AUTH_VERIFY_TOKEN)
        if json:
            self.__class__._emit_event(event_type=constants.EVENT_LOGIN)
            return True
        return False

    def change_password(self, new_password):
        json = {'password': new_password}
        return super().post(path=constants.API_CHANGE_PASSWORD, json=json)
