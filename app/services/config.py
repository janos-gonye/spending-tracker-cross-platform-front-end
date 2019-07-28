from kivy.storage.jsonstore import JsonStore

from constants import CONFIG_FILENAME
from events.dispatcher import EventDispatcher
from utils.lang import classproperty


# TODO: Find out how to fix setter here:
# https://stackoverflow.com/questions/5189699/how-to-make-a-class-property
class ConfigService:
    _protocol = None
    _host = None
    _port = None
    _dispatcher = EventDispatcher()

    @classmethod
    def get_protocol(cls):
        if cls._protocol is not None:
            return cls._protocol
        try:
            return cls._store.get('protocol')['value']
        except KeyError:
            return ''

    @classmethod
    def set_protocol(cls, value):
        value = value.lower()
        if value not in ['http', 'https']:
            raise ValueError
        cls._protocol = value
        cls._store.put("protocol", value=value)
        cls._settings_changed()

    @classmethod
    def get_host(cls):
        if cls._host is not None:
            return cls._host
        try:
            return cls._store.get('host')['value']
        except KeyError:
            return ''

    @classmethod
    def set_host(cls, value):
        if value == '': raise ValueError
        cls._host = value
        cls._store.put("host", value=value)
        cls._settings_changed()

    @classmethod
    def get_port(cls):
        if cls._port is not None:
            return cls._port
        try:
            return cls._store.get('port')['value']
        except KeyError:
            return ''

    @classmethod
    def set_port(cls, value):
        # raise ValueError if not an integer taken
        value = int(value)
        if not (0 < value <= 65535):
            raise ValueError
        cls._port = value
        cls._store.put("port", value=value)
        cls._settings_changed()

    @classproperty
    def _store(cls):
        return JsonStore(filename=CONFIG_FILENAME)

    @classmethod
    def _settings_changed(cls):
        cls._dispatcher.dispatch(event_type='on_settings_change')
