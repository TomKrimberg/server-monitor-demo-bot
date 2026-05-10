import random
from datetime import datetime
from bot.domain.server_status import ServerStatus
from bot.domain.memory_info import MemoryInfo
from bot.domain.cpu_info import CpuInfo
from bot.domain.disk_info import DiskInfo
from bot.domain.log_entry import LogEntry

class DemoServerService:
    def __init__(self,server_name="demo-server-01",environment="demo"):
        self._server_name = server_name
        self._environment = environment

    def get_status(self):
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return ServerStatus(
            server_name=self._server_name,
            environment=self._environment,
            is_online=True,
            current_time=now_str,
            message="Server is running smoothly"
        )

    def get_uptime(self):
        days = random.randint(1, 365)
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        return f"{days} days, {hours} hours, {minutes} minutes"

    def get_memory_info(self):
        total = random.randint(1, 20)
        used = round(random.uniform(1.0, total-1), 2)
        free = round(total - used, 2)
        usage_pct = round((used / total) * 100, 2)
        return MemoryInfo(
            total_gb=total,
            used_gb=used,
            free_gb=free,
            usage_percent=usage_pct
        )

    def _build_single_disk(self, mount_point, total_gb):
        used = round(random.uniform(10, total_gb - 5), 2)
        free = round(total_gb - used, 2)
        usage_pct = round((used / total_gb) * 100, 2)
        return DiskInfo(
            mount_point=mount_point,
            total_gb=total_gb,
            used_gb=used,
            free_gb=free,
            usage_percent=usage_pct
        )

    def get_disk_info(self):
        return [
            self._build_single_disk("C:", 256),
            self._build_single_disk("D:", 1024)
        ]

    def get_cpu_info(self):
        usage_pct = random.randint(1, 100)
        load_1m = round(random.uniform(0.1, 1.5), 2)
        load_5m = round(random.uniform(0.1, 1.2), 2)
        load_15m = round(random.uniform(0.1, 1.0), 2)
        core_cnt= random.randrange(8, 16, 4)
        return CpuInfo(
            usage_percent=usage_pct,
            load_average_1m=load_1m,
            load_average_5m=load_5m,
            load_average_15m=load_15m,
            core_count=core_cnt
        )

    def get_recent_logs(self, count=5):
        possible_messages = [
            "Nginx service started",
            "Database backup completed",
            "User 'Tom' connected via SSH",
            "System update available",
            "High memory usage detected",
            "Inbound connection from 192.168.1.45"
        ]
        logs = []
        for i in range(count):
            entry = LogEntry(
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                level="INFO",
                message=random.choice(possible_messages)
            )
            logs.append(entry)
        return logs

    def get_health_summary(self):
        status = self.get_status()
        memory = self.get_memory_info()
        cpu = self.get_cpu_info()
        return {
            "server_name": status.server_name,
            "is_online": status.is_online,
            "cpu_usage": cpu.usage_percent,
            "memory_usage": memory.usage_percent,
            "timestamp": status.current_time
        }
    