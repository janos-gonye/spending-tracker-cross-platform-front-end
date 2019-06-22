CONFIG_FILENAME = 'config.json'
API_PROTOCOL = 'http' # !Use Https in Production
API_HOST = 'localhost'
API_PORT = 5000
API_PATH = '/api'
API_DEFAULT_KEY = 'message'

# API Endpoints
API_AUTH_LOGIN = API_PATH + '/auth/login'
API_AUTH_REGISTRATION = API_PATH + '/auth/registration'
API_CATEGORIES = API_PATH + '/categories'
API_TRANACTIONS = API_PATH + '/categories/{cat_id}/transactions'
