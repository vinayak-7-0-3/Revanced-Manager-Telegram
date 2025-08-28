from pyrogram import Client, filters
from pyrogram.types import Message

from bot import Config, LOGGER, CMD

@Client.on_message(filters.command(CMD.PATCH))
async def patch_apk(c:Client, msg:Message):
    filename = msg.reply_to_message.document.file_name

    LOGGER.debug(f'Telegram Bot: Starting to download {filename}')
    apk = await msg.reply_to_message.download(Config.TEMP_DIR + filename)
    LOGGER.debug(f'Telegram Bot: Finished downloading {filename}')
