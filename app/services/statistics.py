import constants

from models.category import Category
from services.api import ApiService
from services.exceptions import ConnectionError_


class StatisticsService(ApiService):

    def get_statistics(self, from_, to):
        params = {'from': from_, 'to': to}
        payload, error = super().get(path=constants.API_STATISTICS,
                                     params=params)
        if payload is None:
            raise ConnectionError_(error)
        return payload['statistics']

    def export_statistics(self, from_, to):
        params = {'from': from_, 'to': to}
        payload, error = super().get(path=constants.API_STATISTICS_EXPORT,
                                     params=params)
        if payload is None:
            raise ConnectionError_(error)
        return payload[constants.API_DEFAULT_KEY]
