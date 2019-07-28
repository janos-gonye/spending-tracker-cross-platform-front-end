from kivy.storage.jsonstore import JsonStore

from constants import CONFIG_FILENAME
from constants import EVENT_LOGIN
from constants import EVENT_LOGOUT
from services.mixins import EventEmitterMixin
from utils.lang import classproperty


class SessionService(EventEmitterMixin):
	_email = None
	_token = None

	@classmethod
	def create(cls, email, token):
		cls._email = email
		cls._token = token
		cls._store.put("email", value=email)
		cls._store.put("token", value=token)
		cls._emit_event(event_type=EVENT_LOGIN)

	@classmethod
	def destroy(cls):
		cls._email = None
		cls._token = None
		cls._store.delete("email")
		cls._store.delete("token")
		cls._emit_event(event_type=EVENT_LOGOUT)

	@classproperty
	def email(cls):
		if cls._email is not None:
			return cls._email
		try:
			return cls._store.get("email")["value"]
		except KeyError:
			return None

	@classproperty
	def token(cls):
		if cls._token is not None:
			return cls._token
		try:
			return cls._store.get("token")["value"]
		except KeyError:
			return None

	@classproperty
	def _store(cls):
		return JsonStore(filename=CONFIG_FILENAME)
