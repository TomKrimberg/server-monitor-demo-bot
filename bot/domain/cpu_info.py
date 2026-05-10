from bot.exceptions import DemoDataError


class CpuInfo:
    def __init__(self, usage_percent, load_average_1m, load_average_5m, load_average_15m, core_count):
        if not (0 <= usage_percent <= 100):
            raise DemoDataError(f"Invalid CPU usage percent: {usage_percent}%")

        if load_average_1m < 0 or load_average_5m < 0 or load_average_15m < 0:
            raise DemoDataError("Load average values cannot be negative")

        if core_count <= 0:
            raise DemoDataError("Core count must be positive")

        self._usage_percent = usage_percent
        self._load_average_1m = load_average_1m
        self._load_average_5m = load_average_5m
        self._load_average_15m = load_average_15m
        self._core_count = core_count

    @property
    def usage_percent(self):
        return self._usage_percent

    @property
    def load_average_1m(self):
        return self._load_average_1m

    @property
    def load_average_5m(self):
        return self._load_average_5m

    @property
    def load_average_15m(self):
        return self._load_average_15m

    @property
    def core_count(self):
        return self._core_count

    def as_dict(self):
        return {
            "usage_percent": self._usage_percent,
            "load_average_1m": self._load_average_1m,
            "load_average_5m": self._load_average_5m,
            "load_average_15m": self._load_average_15m,
            "core_count": self._core_count
        }

    def is_high_usage(self):
        return self._usage_percent >= 75