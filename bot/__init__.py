from config import Config
from .logger import LOGGER

bot = Config.BOT_USERNAME

class CMD(object):
    PATCH = ["patch", f"patch@{bot}"]