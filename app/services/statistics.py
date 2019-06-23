import constants

from models.category import Category
from services.api import ApiService
from services.exceptions import ConnectionError_


class StatisticsService(ApiService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_statistics(self):
        payload, error = super().get(path=constants.API_STATISTICS)
        if payload is None:
            raise ConnectionError_(error)
        return payload['statistics']

    def export_statistics(self):
        payload, error = super().get(path=constants.API_STATISTICS_EXPORT)
        if payload is None:
            raise ConnectionError_(error)
        return payload[constants.API_DEFAULT_KEY]
