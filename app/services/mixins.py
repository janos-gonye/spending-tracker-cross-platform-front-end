from events.dispatcher import EventDispatcher


class EventEmitterMixin:

    @classmethod
    def _emit_event(cls, event_type, *args):
        EventDispatcher().dispatch(event_type=event_type, *args)
