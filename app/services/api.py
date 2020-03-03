import json
from functools import wraps
from json.decoder import JSONDecodeError

from requests import Session

import constants
from services.config import ConfigService
from services.http import HttpService
from services.mixins import EventEmitterMixin
from services.session import SessionService
from utils.url import (create_url, get_path_from_url,
                       get_query_params_from_url, succ_status)


def _attach_token(f):
    """
    Attach access token if exists
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        if SessionService.access_token:
            token = 'Bearer {token}'.format(token=SessionService.access_token)
            if kwargs.get('headers'):
                kwargs['headers']['Authorization'] = token
            else:
                kwargs['headers'] = {'Authorization': token}
        return f(*args, **kwargs)
    return decorated


class ApiService(EventEmitterMixin, HttpService):

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

    @_attach_token
    def resend_request(self, r, *args, **kwargs):
        path = get_path_from_url(r.url)
        params = get_query_params_from_url(r.url)
        method = getattr(self, r.method.lower())
        body = getattr(r, 'body', None)
        if body:
            kwargs['json'] = json.loads(body)
        return method(path=path, params=params, *args, **kwargs)

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
            if json and json.get('expired'):
                if r.url == self._get_api_url(constants.API_AUTH_REFRESH):
                    self.__class__._emit_event(constants.EVENT_SESSION_EXPIRE)
                    return None, json[constants.API_DEFAULT_KEY]
                else:
                    if self.refresh_session():
                        return self.resend_request(r.request)
                    else:
                        return None, json[constants.API_DEFAULT_KEY]
            return None, json[constants.API_DEFAULT_KEY]
        except JSONDecodeError:
            return None, error
        return None, error

    def refresh_session(self):
        refresh_token = SessionService.refresh_token
        if refresh_token:
            json = {'refresh_token': refresh_token}
            json, error = self.post(path=constants.API_AUTH_REFRESH, json=json)
            if not error:
                SessionService.refresh(access_token=json['access_token'])
                return True
            else:
                return False
        else:
            return False
