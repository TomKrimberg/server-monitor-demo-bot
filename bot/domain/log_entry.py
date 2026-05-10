from bot.exceptions import DemoDataError


class LogEntry:
    def __init__(self, timestamp: str, level: str, message: str):
        if not timestamp:
            raise DemoDataError("Log timestamp cannot be empty")

        if not level:
            raise DemoDataError("Log level cannot be empty")

        if not message:
            raise DemoDataError("Log message cannot be empty")

        self._timestamp = timestamp
        self._level = level
        self._message = message

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def level(self):
        return self._level

    @property
    def message(self):
        return self._message

    def as_dict(self):
        return {
            "timestamp": self._timestamp,
            "level": self._level,
            "message": self._message
        }

    def to_display_line(self):
        return f"[{self._timestamp}] {self._level} - {self._message}"