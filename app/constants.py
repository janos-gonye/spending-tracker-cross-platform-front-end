CONFIG_FILENAME = 'config.json'
API_PATH = '/api'
API_DEFAULT_KEY = 'message'

# API Endpoints
API_AUTH_LOGIN = API_PATH + '/auth/login'
API_AUTH_VERIFY_TOKEN = API_PATH + '/auth/verify-token'
API_AUTH_REGISTRATION = API_PATH + '/auth/registration'
API_AUTH_CHANGE_PASSWORD = API_PATH + '/auth/change-password'
API_AUTH_FORGOT_PASSWORD = API_PATH + '/auth/forgot-password'
API_AUTH_REFRESH = API_PATH + '/auth/refresh-token'
API_CATEGORIES = API_PATH + '/categories'
API_MERGE_CATEGORIES = API_PATH + '/merge-categories'
API_TRANACTIONS = API_PATH + '/categories/{cat_id}/transactions'
API_STATISTICS = API_PATH + '/statistics'
API_STATISTICS_EXPORT = API_PATH + '/statistics/export'

# Event types
EVENT_LOGIN = 'on_login'
EVENT_LOGOUT = 'on_logout'
EVENT_SETTINGS_CHANGE = 'on_settings_change'
EVENT_SESSION_EXPIRE = 'on_session_expire'
