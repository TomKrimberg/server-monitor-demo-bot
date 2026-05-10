from bot.domain.server_status import ServerStatus
from bot.domain.memory_info import MemoryInfo
from bot.domain.disk_info import DiskInfo
from bot.domain.cpu_info import CpuInfo
from bot.domain.log_entry import LogEntry

from bot.formatters import (
    format_status_message,
    format_uptime_message,
    format_memory_message,
    format_disk_message,
    format_cpu_message,
    format_logs_message,
    format_help_message,
    format_start_message,
    format_error_message,
)


def test_format_status_message_returns_string():
    status = ServerStatus(
        server_name="demo-server-01",
        environment="demo",
        is_online=True,
        current_time="2026-05-10 19:30:00",
        message="Server is online",
    )

    message = format_status_message(status)

    assert isinstance(message, str)
    assert "Server Status" in message
    assert "demo-server-01" in message


def test_format_uptime_message_returns_string():
    message = format_uptime_message("2 days, 14 hours")

    assert isinstance(message, str)
    assert "Server Uptime" in message
    assert "2 days" in message


def test_format_memory_message_returns_string():
    memory = MemoryInfo(
        total_gb=8,
        used_gb=3.1,
        free_gb=4.9,
        usage_percent=39,
    )

    message = format_memory_message(memory)

    assert isinstance(message, str)
    assert "Memory Usage" in message
    assert "39" in message


def test_format_disk_message_returns_string():
    disks = [
        DiskInfo(
            mount_point="/",
            total_gb=120,
            used_gb=52,
            free_gb=68,
            usage_percent=43,
        )
    ]

    message = format_disk_message(disks)

    assert isinstance(message, str)
    assert "Disk Usage" in message
    assert "/" in message


def test_format_cpu_message_returns_string():
    cpu = CpuInfo(
        usage_percent=27,
        load_average_1m=0.62,
        load_average_5m=0.71,
        load_average_15m=0.54,
        core_count=4,
    )

    message = format_cpu_message(cpu)

    assert isinstance(message, str)
    assert "CPU Metrics" in message
    assert "27" in message


def test_format_logs_message_returns_string():
    logs = [
        LogEntry(
            timestamp="2026-05-10 19:30:00",
            level="INFO",
            message="demo health check passed",
        )
    ]

    message = format_logs_message(logs)

    assert isinstance(message, str)
    assert "Recent Logs" in message
    assert "demo health check passed" in message


def test_format_help_message_returns_string():
    message = format_help_message()

    assert isinstance(message, str)
    assert "/status" in message
    assert "/help" in message


def test_format_start_message_returns_string():
    message = format_start_message("Server Monitor Demo Bot")

    assert isinstance(message, str)
    assert "Server Monitor Demo Bot" in message


def test_format_error_message_returns_string():
    message = format_error_message("Something went wrong")

    assert isinstance(message, str)
    assert "Error" in message
    assert "Something went wrong" in message