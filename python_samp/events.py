from threading import Thread


class Events:
    def _handle(self, function: object, wrapper: object) -> None:
        data = function()
        while True:
            _data = function()
            if data != _data:
                wrapper(_data)
                data = _data

    def listen(self, *args: object) -> object:
        def wrap(wrapper):
            thread = Thread(target=self._handle, args=(args[0], wrapper))
            thread.start()

        return wrap
