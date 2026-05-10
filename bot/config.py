import os
from dotenv import load_dotenv

from bot.exceptions import ConfigurationError


class Config:
    def __init__(self):
        load_dotenv()
        self._bot_token = os.getenv("BOT_TOKEN")
        self._bot_name = os.getenv("BOT_NAME")

    @property
    def bot_token(self):
        return self._bot_token

    @property
    def bot_name(self):
        return self._bot_name

    def validate(self):
        if not self._bot_token:
            raise ConfigurationError("BOT_TOKEN is missing in .env file")

        if not self._bot_name:
            raise ConfigurationError("BOT_NAME is missing in .env file")