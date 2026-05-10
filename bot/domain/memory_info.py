from bot.exceptions import DemoDataError


class MemoryInfo:
    def __init__(self, total_gb, used_gb, free_gb, usage_percent):
        if total_gb <= 0:
            raise DemoDataError("Total memory must be positive")

        if not (0 <= usage_percent <= 100):
            raise DemoDataError(f"Invalid usage percent: {usage_percent}%")

        if used_gb < 0 or free_gb < 0:
            raise DemoDataError("Memory values cannot be negative")

        self._total_gb = total_gb
        self._used_gb = used_gb
        self._free_gb = free_gb
        self._usage_percent = usage_percent

    @property
    def total_gb(self):
        return self._total_gb

    @property
    def used_gb(self):
        return self._used_gb

    @property
    def free_gb(self):
        return self._free_gb

    @property
    def usage_percent(self):
        return self._usage_percent

    def as_dict(self):
        return {
            "total_gb": self._total_gb,
            "used_gb": self._used_gb,
            "free_gb": self._free_gb,
            "usage_percent": self._usage_percent
        }

    def is_high_usage(self):
        return self._usage_percent >= 80