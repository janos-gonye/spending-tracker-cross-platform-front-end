class EventDispatcher:
    handlers = []

    def __init__(self):
        pass

    def dispatch(self, event_type, *args):
        for handler in EventDispatcher.handlers:
            if handler.event_type == event_type:
                handler.callback(*args)
