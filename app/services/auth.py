import constants

from events.dispatcher import EventDispatcher
from services.api import ApiService
from services.session import SessionService


class AuthService(ApiService):
	"""Authentication Service for handling registration, login etc."""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.dispatcher = EventDispatcher()

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
		self.dispatcher.dispatch('on_login', email)
		return json, error

	def logout(self):
		SessionService.destroy()
		return True
