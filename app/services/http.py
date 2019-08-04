import requests


class HttpService:
    """
    Basic HTTP Service
    Base Class of Other HTTP Services used within the Application
    Responsible for Sending HTTP Requests, Receiving Responses and catching any <RequestException>

    Return <requests.Response> object if no <RequestException> occured
    Return <None> else
    """

    def __init__(self):
        pass

    def get(self, url, **kwargs):
        try:
            return requests.get(url, **kwargs)
        except requests.exceptions.RequestException:
            return None

    def post(self, url, **kwargs):
        try:
            return requests.post(url, **kwargs)
        except requests.exceptions.RequestException:
            return None

    def put(self, url, **kwargs):
        try:
            return requests.put(url, **kwargs)
        except requests.exceptions.RequestException:
            return None

    def patch(self, url, **kwargs):
        try:
            return requests.patch(url, **kwargs)
        except requests.exceptions.RequestException:
            return None

    def delete(self, url, **kwargs):
        try:
            return requests.delete(url, **kwargs)
        except requests.exceptions.RequestException:
            return None
