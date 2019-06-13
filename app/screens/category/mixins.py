from services.category import CategoryService
from services.exceptions import ConnectionError_


class FetchCategoriesMixin:

    def fetch_categories(self):
        service = CategoryService()
        try:
            self.categories = service.get_all()
            self.cat_conn_error = None
        except ConnectionError_ as err:
            self.cat_conn_error = err
            self.categories = []
