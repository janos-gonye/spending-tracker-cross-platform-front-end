from kivy.storage.jsonstore import JsonStore

from constants import CONFIG_FILENAME
from constants import EVENT_LOGIN
from constants import EVENT_LOGOUT
from constants import EVENT_ON_SESSION_REFRESH
from services.mixins import EventEmitterMixin
from utils.lang import classproperty


class SessionService(EventEmitterMixin):
    _email = None
    _access_token = None
    _refresh_token = None

    @classmethod
    def create(cls, email, access_token, refresh_token):
        cls._email = email
        cls._access_token = access_token
        cls._store.put("email", value=email)
        cls._store.put("access_token", value=access_token)
        cls._store.put("refresh_token", value=refresh_token)
        cls._emit_event(event_type=EVENT_LOGIN)

    @classmethod
    def destroy(cls):
        cls._email = None
        cls._access_token = None
        cls._store.delete("email")
        cls._store.delete("access_token")
        cls._store.delete("refresh_token")
        cls._emit_event(event_type=EVENT_LOGOUT)

    @classmethod
    def refresh(cls, access_token):
        cls._access_token = access_token
        cls._store.put("access_token", value=access_token)
        cls._emit_event(event_type=EVENT_ON_SESSION_REFRESH)

    @classproperty
    def email(cls):
        if cls._email is not None:
            return cls._email
        try:
            return cls._store.get("email")["value"]
        except KeyError:
            return None

    @classproperty
    def access_token(cls):
        if cls._access_token is not None:
            return cls._access_token
        try:
            return cls._store.get("access_token")["value"]
        except KeyError:
            return None

    @classproperty
    def refresh_token(cls):
        if cls._refresh_token is not None:
            return cls._refresh_token
        try:
            return cls._store.get("refresh_token")["value"]
        except KeyError:
            return None

    @classproperty
    def _store(cls):
        return JsonStore(filename=CONFIG_FILENAME)
