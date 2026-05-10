from bot.services.demo_server_service import DemoServerService
from bot.domain.server_status import ServerStatus
from bot.domain.memory_info import MemoryInfo
from bot.domain.cpu_info import CpuInfo
from bot.domain.log_entry import LogEntry


def test_get_status_returns_server_status():
    service = DemoServerService()

    status = service.get_status()

    assert isinstance(status, ServerStatus)
    assert status.server_name != ""
    assert status.environment != ""
    assert status.is_healthy() is True


def test_get_uptime_returns_string():
    service = DemoServerService()

    uptime = service.get_uptime()

    assert isinstance(uptime, str)
    assert len(uptime) > 0


def test_get_memory_info_returns_valid_memory_info():
    service = DemoServerService()

    memory = service.get_memory_info()

    assert isinstance(memory, MemoryInfo)
    assert 0 <= memory.usage_percent <= 100
    assert memory.total_gb > 0
    assert memory.used_gb >= 0
    assert memory.free_gb >= 0


def test_get_disk_info_returns_list():
    service = DemoServerService()

    disks = service.get_disk_info()

    assert isinstance(disks, list)
    assert len(disks) > 0

    for disk in disks:
        assert disk.mount_point != ""
        assert 0 <= disk.usage_percent <= 100
        assert disk.total_gb > 0


def test_get_cpu_info_returns_valid_cpu_info():
    service = DemoServerService()

    cpu = service.get_cpu_info()

    assert isinstance(cpu, CpuInfo)
    assert 0 <= cpu.usage_percent <= 100
    assert cpu.core_count > 0


def test_get_recent_logs_returns_log_entries():
    service = DemoServerService()

    logs = service.get_recent_logs()

    assert isinstance(logs, list)
    assert len(logs) > 0

    for log in logs:
        assert isinstance(log, LogEntry)
        assert log.to_display_line() != ""