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
            SessionService.create(email=email,
                                  access_token=json['access_token'],
                                  refresh_token=json['refresh_token'])
        return json, error

    def logout(self):
        SessionService.destroy()
        return True

    def change_password(self, old_password, new_password):
        json = {
            'old_password': old_password,
            'new_password': new_password
        }
        return super().post(path=constants.API_AUTH_CHANGE_PASSWORD, json=json)

    def forgot_password(self, email):
        return super().post(path=constants.API_AUTH_FORGOT_PASSWORD, json={
            'email': email,
        })

    def refresh_session(self):
        refresh_token = SessionService.refresh_token
        if refresh_token:
            json = {'refresh_token': refresh_token}
            json, error = super().post(path=constants.API_AUTH_REFRESH,
                                       json=json)
            if not error:
                SessionService.refresh(access_token=json['access_token'])
                return True
            else:
                return False
        else:
            return False
