import constants

from services.http import HttpService
from utils import create_url, succ_status


class ApiService(HttpService):

	def __init__(self, *args, **kwargs):
		"""
		Extend the Functionality of <HttpService> by Handling Unsuccessful Requests
		
		Return <json>, <message>
			If successful message is None
			If not successful json is None
		"""
		super().__init__(*args, **kwargs)

	# Override
	def get(self, path, params={}):
		url = self._get_api_url(path=path)
		r = super().get(url=url, params=params)
		return self._handle_unsuccessful_requests(r)

	# Override
	def post(self, path, params={}, json=None):
		url = self._get_api_url(path=path)
		r = super().post(url=url, params=params, json=json)
		return self._handle_unsuccessful_requests(r)

	# Override
	def put(self, path, params={}, json=None):
		url = self._get_api_url(path=path)
		r = super().put(url=url, params=params, json=json)
		return self._handle_unsuccessful_requests(r)

	# Override
	def patch(self, path, params={}, json=None):
		url = self._get_api_url(path=path)
		r = super().patch(url=url, params=params, json=json)
		return self._handle_unsuccessful_requests(r)

	# Override
	def delete(self, path, params={}):
		url = self._get_api_url(path=path)
		r = super().delete(url=url, params=params)
		return self._handle_unsuccessful_requests(r)

	# Private Methods
	def _get_api_url(self, path):
		return create_url(
			protocol=constants.API_PROTOCOL,
			host=constants.API_HOST,
			port=constants.API_PORT,
			path=path)

	def _handle_unsuccessful_requests(self, r):
		if r:
			if succ_status(r.status_code):
				return r.json(), None
			json = r.json()
			if json:
				return None, json[constants.API_DEFAULT_KEY]
			return None, 'Error Occured When Connecting to Server'
		return None, 'Error Occured When Connecting to Server'
