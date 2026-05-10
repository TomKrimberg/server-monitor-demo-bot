from telegram import Update
from telegram.ext import ContextTypes

from bot.formatters import (
    format_start_message,
    format_help_message,
    format_status_message,
    format_uptime_message,
    format_memory_message,
    format_disk_message,
    format_cpu_message,
    format_logs_message,
    format_error_message
)


class BotHandlers:
    def __init__(self, demo_service, logger, bot_name):
        self._demo_service = demo_service
        self._logger = logger
        self._bot_name = bot_name

    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._logger.info(f"User {update.effective_user.id} triggered /start")
        try:
            message = format_start_message(self._bot_name)
            await update.message.reply_text(message, parse_mode="Markdown")
        except Exception as e:
            await self._handle_error(update, e)

    async def handle_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._logger.info(f"User {update.effective_user.id} triggered /help")
        try:
            message = format_help_message()
            await update.message.reply_text(message, parse_mode="Markdown")
        except Exception as e:
            await self._handle_error(update, e)

    async def handle_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._logger.info("Command /status received")
        try:
            status_data = self._demo_service.get_status()
            message = format_status_message(status_data)
            await update.message.reply_text(message, parse_mode="Markdown")
        except Exception as e:
            await self._handle_error(update, e)

    async def handle_uptime(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._logger.info("Command /uptime received")
        try:
            uptime_data = self._demo_service.get_uptime()
            message = format_uptime_message(uptime_data)
            await update.message.reply_text(message, parse_mode="Markdown")
        except Exception as e:
            await self._handle_error(update, e)

    async def handle_memory(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._logger.info("Command /memory received")
        try:
            memory_data = self._demo_service.get_memory_info()
            message = format_memory_message(memory_data)
            await update.message.reply_text(message, parse_mode="Markdown")
        except Exception as e:
            await self._handle_error(update, e)

    async def handle_disk(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._logger.info("Command /disk received")
        try:
            disk_data = self._demo_service.get_disk_info()
            message = format_disk_message(disk_data)
            await update.message.reply_text(message, parse_mode="Markdown")
        except Exception as e:
            await self._handle_error(update, e)

    async def handle_cpu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._logger.info("Command /cpu received")
        try:
            cpu_data = self._demo_service.get_cpu_info()
            message = format_cpu_message(cpu_data)
            await update.message.reply_text(message, parse_mode="Markdown")
        except Exception as e:
            await self._handle_error(update, e)

    async def handle_logs(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._logger.info("Command /logs received")
        try:
            logs_data = self._demo_service.get_recent_logs()
            message = format_logs_message(logs_data)
            await update.message.reply_text(message, parse_mode="Markdown")
        except Exception as e:
            await self._handle_error(update, e)

    async def _handle_error(self, update: Update, e: Exception):
        self._logger.error(f"Error handling command: {str(e)}")
        error_msg = format_error_message("Something went wrong while fetching data.")
        await update.message.reply_text(error_msg, parse_mode="Markdown")