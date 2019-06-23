from constants import CONFIG_FILENAME

from kivy.storage.jsonstore import JsonStore

from utils.lang import classproperty


class SessionService:
	_store = JsonStore(filename=CONFIG_FILENAME)
	_email = None
	_token = None

	@staticmethod
	def create(email, token):
		SessionService._email = email
		SessionService._token = token
		SessionService._store.put("email", value=email)
		SessionService._store.put("token", value=token)

	@staticmethod
	def destroy():
		SessionService._email = None
		SessionService._token = None
		SessionService._store.delete("email")
		SessionService._store.delete("token")

	@classproperty
	def email(cls):
		if cls._email is not None:
			return cls._email
		try:
			return SessionService._store.get("email")["value"]
		except KeyError:
			return None

	@classproperty
	def token(cls):
		if cls._token is not None:
			return cls._token
		try:
			return SessionService._store.get("token")["value"]
		except KeyError:
			return None
