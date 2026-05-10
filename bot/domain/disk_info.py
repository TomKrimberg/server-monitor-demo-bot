from bot.exceptions import DemoDataError


class DiskInfo:
    def __init__(self, mount_point, total_gb, used_gb, free_gb, usage_percent):
        if not mount_point:
            raise DemoDataError("Mount point cannot be empty")

        if total_gb <= 0:
            raise DemoDataError("Total disk size must be positive")

        if used_gb < 0 or free_gb < 0:
            raise DemoDataError("Disk values cannot be negative")

        if not (0 <= usage_percent <= 100):
            raise DemoDataError(f"Invalid disk usage percent: {usage_percent}%")

        self._mount_point = mount_point
        self._total_gb = total_gb
        self._used_gb = used_gb
        self._free_gb = free_gb
        self._usage_percent = usage_percent

    @property
    def mount_point(self):
        return self._mount_point

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
            "mount_point": self._mount_point,
            "total_gb": self._total_gb,
            "used_gb": self._used_gb,
            "free_gb": self._free_gb,
            "usage_percent": self._usage_percent
        }

    def is_almost_full(self):
        return self._usage_percent >= 85