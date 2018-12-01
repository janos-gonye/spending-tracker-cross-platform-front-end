import constants

from services.api import ApiService


class AuthService(ApiService):
	"""Authentication Service for handling registration, login etc."""

	def __init__(self):
		pass

	def registrate(self, email, password):
		pass

	def delete_registration(self):
		pass

	def login(self, email, password):
		json = {
			'email': email,
			'password': password, 
		}
		json, error = super().post(path=constants.API_AUTH_LOGIN, json=json)
		if not json:
			return False
		token = json['token']
		print(token)
		return True

	def logout(self):
		pass
