from events.dispatcher import EventDispatcher


class EventHandler:

    def __init__(self, event_type, callback):
        EventDispatcher.handlers.append(self)
        self.event_type = event_type
        self.callback = callback
