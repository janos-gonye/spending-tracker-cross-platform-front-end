from functools import wraps
from json.decoder import JSONDecodeError

import constants

from services.config import ConfigService
from services.http import HttpService
from services.session import SessionService
from utils import create_url, succ_status


def _attach_token(f):
	"""
	Attach token if exists
	"""
	@wraps(f)
	def decorated(*args, **kwargs):
		if SessionService.token:
			token = 'Bearer {token}'.format(token=SessionService.token)
			if kwargs.get('headers'):
				kwargs['headers']['Authorization'] = token
			else:
				kwargs['headers'] = {'Authorization': token}
		return f(*args, **kwargs)
	return decorated


class ApiService(HttpService):

	def __init__(self, *args, **kwargs):
		"""
		Extend the Functionality of <HttpService> by Handling Unsuccessful Requests
		
		Return <json>, <message>
			If successful message is None
			If not successful json is None
		"""
		super().__init__(*args, **kwargs)

	@_attach_token
	def get(self, path, params={}, **kwargs):
		url = self._get_api_url(path=path)
		r = super().get(url=url, params=params, **kwargs)
		return self._handle_request(r)

	@_attach_token
	def post(self, path, params={}, json=None, **kwargs):
		url = self._get_api_url(path=path)
		r = super().post(url=url, params=params, json=json, **kwargs)
		return self._handle_request(r)

	@_attach_token
	def put(self, path, params={}, json=None, **kwargs):
		url = self._get_api_url(path=path)
		r = super().put(url=url, params=params, json=json, **kwargs)
		return self._handle_request(r)

	@_attach_token
	def patch(self, path, params={}, json=None, **kwargs):
		url = self._get_api_url(path=path)
		r = super().patch(url=url, params=params, json=json, **kwargs)
		return self._handle_request(r)

	@_attach_token
	def delete(self, path, params={}, **kwargs):
		url = self._get_api_url(path=path)
		r = super().delete(url=url, params=params, **kwargs)
		return self._handle_request(r)

	# Private Methods
	def _get_api_url(self, path):
		return create_url(
			protocol=ConfigService.get_protocol(),
			host=ConfigService.get_host(),
			port=ConfigService.get_port(),
			path=path)

	def _handle_request(self, r):
		error = 'Error Occured When Connecting to Server'
		if r is None:
			return None, error
		try:
			if succ_status(r.status_code):
				return r.json(), None
			json = r.json()
			if json:
				return None, json[constants.API_DEFAULT_KEY]
		except JSONDecodeError:
			return None, error
		return None, error
