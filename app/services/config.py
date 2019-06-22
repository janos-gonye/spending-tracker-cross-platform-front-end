from constants import CONFIG_FILENAME

from kivy.storage.jsonstore import JsonStore

from utils.lang import classproperty


class ConfigService:
    _store = JsonStore(filename=CONFIG_FILENAME)
    _protocol = None
    _host = None
    _port = None

    @classproperty
    def protocol(cls):
        if cls._protocol is not None:
            return cls._protocol
        try:
            return cls._store.get('protocol')['value']
        except KeyError:
            return ''

    @protocol.setter
    def protocol(cls, value):
        value = value.lower()
        if value not in ['http', 'https']:
            raise ValueError
        cls._protocol = value
        cls._store.put("protocol", value=value)

    @classproperty
    def host(cls):
        if cls._host is not None:
            return cls.host
        try:
            return cls._store.get('host')['value']
        except KeyError:
            return ''

    @host.setter
    def host(cls, value):
        if value == '': raise ValueError
        cls._host = value
        cls._store.put("host", value=value)

    @classproperty
    def port(cls):
        if cls._port is not None:
            return cls._port
        try:
            return cls._store.get('port')['value']
        except KeyError:
            return ''

    @port.setter
    def port(cls, value):
        value = int(value) # raise ValueError if not an integer taken
        cls._port = value
        cls._store.put("port", value=value)
