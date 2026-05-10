from telegram.ext import ApplicationBuilder, CommandHandler

from bot.config import Config
from bot.logging_config import setup_logging
from bot.services.demo_server_service import DemoServerService
from bot.handlers import BotHandlers


def main():
    config = Config()
    config.validate()

    logger = setup_logging()
    logger.info("Starting Server Monitor Demo Bot...")

    demo_service = DemoServerService()

    handlers = BotHandlers(
        demo_service=demo_service,
        logger=logger,
        bot_name=config.bot_name
    )

    application = ApplicationBuilder().token(config.bot_token).build()

    application.add_handler(CommandHandler("start", handlers.handle_start))
    application.add_handler(CommandHandler("help", handlers.handle_help))
    application.add_handler(CommandHandler("status", handlers.handle_status))
    application.add_handler(CommandHandler("uptime", handlers.handle_uptime))
    application.add_handler(CommandHandler("memory", handlers.handle_memory))
    application.add_handler(CommandHandler("disk", handlers.handle_disk))
    application.add_handler(CommandHandler("cpu", handlers.handle_cpu))
    application.add_handler(CommandHandler("logs", handlers.handle_logs))

    logger.info("Bot is now running with polling.")
    application.run_polling()


if __name__ == "__main__":
    main()