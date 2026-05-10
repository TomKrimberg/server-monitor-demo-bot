class ServerStatus:
    def __init__(self, server_name, environment, is_online, current_time, message):
        self._server_name = server_name
        self._environment = environment
        self._is_online = is_online
        self._current_time = current_time
        self._message = message

    @property
    def server_name(self):
        return self._server_name

    @property
    def environment(self):
        return self._environment

    @property
    def is_online(self):
        return self._is_online

    @property
    def current_time(self):
        return self._current_time

    @property
    def message(self):
        return self._message

    def as_dict(self):
        return {
            "server_name": self._server_name,
            "environment": self._environment,
            "is_online": self._is_online,
            "current_time": self._current_time,
            "message": self._message
        }

    def is_healthy(self):
        return self._is_online