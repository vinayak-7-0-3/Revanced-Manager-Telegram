from pyrogram import Client, filters
from pyrogram.types import Message

from ..revanced.patcher import patch_apk
from ..helpers.utils import cleanup_after_patching

from bot import Config, LOGGER, CMD

@Client.on_message(filters.command(CMD.PATCH))
async def process_apk(c:Client, msg:Message):
    filename = msg.reply_to_message.document.file_name

    LOGGER.debug(f'Bot: Starting to download {filename}')
    status_msg = await msg.reply_text('Downloading APK......')
    apk = await msg.reply_to_message.download(Config.TEMP_DIR + filename)
    LOGGER.debug(f'Bot: Finished downloading {filename}')

    LOGGER.debug(f'Bot: Giving {filename} for patching')
    status_msg.edit_text('Patching the APK......')
    new_apk = await patch_apk(apk)

    await status_msg.edit_text('Uploading the APK......')
    if new_apk:
        await c.send_document(
            msg.chat.id,
            new_apk,
            caption=f"Patched APK Ready"
        )
    
    cleanup_after_patching(apk, new_apk)
