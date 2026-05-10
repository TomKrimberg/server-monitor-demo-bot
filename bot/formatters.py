from bot.domain.memory_info import MemoryInfo
from bot.domain.disk_info import DiskInfo
from bot.domain.cpu_info import CpuInfo
from bot.domain.log_entry import LogEntry


def format_status_message(status) -> str:
    status_icon = "🟢" if status.is_healthy() else "🔴"
    status_text = "Online" if status.is_healthy() else "Offline"

    return (
        f"🖥 *Server Status*\n"
        f"━━━━━━━━━━━━━━\n"
        f"📍 *Name:* {status.server_name}\n"
        f"🌍 *Environment:* {status.environment.upper()}\n"
        f"⏱ *Time:* {status.current_time}\n"
        f"{status_icon} *Status:* {status_text}\n"
        f"💬 *Message:* {status.message}"
    )


def format_uptime_message(uptime_str: str) -> str:
    return (
        f"⏱️ *Server Uptime*\n"
        f"━━━━━━━━━━━━━━\n"
        f"The server has been running for:\n"
        f"`{uptime_str}`"
    )


def format_memory_message(memory: MemoryInfo) -> str:
    warning = ""
    if memory.is_high_usage():
        warning = "\n⚠️ *Warning: High memory usage detected!*"

    return (
        f"🧠 *Memory Usage*\n"
        f"━━━━━━━━━━━━━━\n"
        f"📊 *Usage:* {memory.usage_percent}%\n"
        f"✅ *Free:* {memory.free_gb} GB\n"
        f"📦 *Used:* {memory.used_gb} GB\n"
        f"🛠 *Total:* {memory.total_gb} GB"
        f"{warning}"
    )


def format_disk_message(disks: list[DiskInfo]) -> str:
    lines = [
        "💾 *Disk Usage*",
        "━━━━━━━━━━━━━━"
    ]

    for disk in disks:
        warning = " ⚠️ *CRITICAL: Almost full!*" if disk.is_almost_full() else ""

        disk_text = (
            f"📁 *Mount:* `{disk.mount_point}`{warning}\n"
            f"📊 *Usage:* {disk.usage_percent}%\n"
            f"🔹 *Free:* {disk.free_gb} GB / {disk.total_gb} GB"
        )

        lines.append(disk_text)

    return "\n\n".join(lines)


def format_cpu_message(cpu: CpuInfo) -> str:
    warning = "⚠️ *High CPU load!*" if cpu.is_high_usage() else "✅ *Normal Load*"

    return (
        f"⚡ *CPU Metrics*\n"
        f"━━━━━━━━━━━━━━\n"
        f"📊 *Usage:* {cpu.usage_percent}%\n"
        f"🧠 *Cores:* {cpu.core_count}\n"
        f"📈 *Load Average:*\n"
        f"  └ 1m: `{cpu.load_average_1m}`\n"
        f"  └ 5m: `{cpu.load_average_5m}`\n"
        f"  └ 15m: `{cpu.load_average_15m}`\n\n"
        f"Status: {warning}"
    )


def format_logs_message(logs: list[LogEntry]) -> str:
    log_lines = "\n".join([f"`{log.to_display_line()}`" for log in logs])

    return (
        f"📄 *Recent Logs*\n"
        f"━━━━━━━━━━━━━━\n"
        f"{log_lines}"
    )


def format_help_message() -> str:
    return (
        f"❓ *Available Commands*\n"
        f"━━━━━━━━━━━━━━\n"
        f"/status - General server status\n"
        f"/uptime - Server running time\n"
        f"/memory - RAM usage stats\n"
        f"/disk - Disk space information\n"
        f"/cpu - Processor load metrics\n"
        f"/logs - View recent system logs\n"
        f"/help - Show this menu"
    )


def format_start_message(bot_name: str) -> str:
    return (
        f"🤖 *Welcome to {bot_name}!*\n\n"
        f"I am a demo system for server monitoring.\n"
        f"I can help you visualize server data in a clean way.\n\n"
        f"Press /help to see what I can do!"
    )


def format_error_message(error_msg: str) -> str:
    return f"❌ *Error:* {error_msg}\n\nPlease try again later."