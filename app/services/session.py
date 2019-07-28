from kivy.storage.jsonstore import JsonStore

from constants import CONFIG_FILENAME
from events.dispatcher import EventDispatcher
from utils.lang import classproperty


class SessionService:
	_email = None
	_token = None
	_dispatcher = EventDispatcher()

	@classmethod
	def create(cls, email, token):
		cls._email = email
		cls._token = token
		cls._store.put("email", value=email)
		cls._store.put("token", value=token)
		cls._session_changed()

	@classmethod
	def destroy(cls):
		cls._email = None
		cls._token = None
		cls._store.delete("email")
		cls._store.delete("token")
		cls._session_changed()

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

	@classmethod
	def _session_changed(cls):
		cls._dispatcher.dispatch(event_type='on_session_change')
