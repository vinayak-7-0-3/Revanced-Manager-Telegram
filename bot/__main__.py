import asyncio

from pyrogram import idle

from bot import Config, LOGGER

from .tg_client import revanced_bot
from .revanced.manager import revanced_manager


async def main():
    await revanced_manager.setup()

    await revanced_bot.start()
    await idle()
    await revanced_bot.stop()

    await revanced_manager.cleanup()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())