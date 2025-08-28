from pyrogram import Client

from bot import LOGGER, Config

plugins = dict(
    root="bot/plugins"
)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Revanced-Manager",
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.TG_BOT_TOKEN,
            plugins=plugins,
            workdir=Config.BASE_DIR,
            workers=100
        )

    async def start(self):
        await super().start()
        LOGGER.info("BOT : Started Successfully")

    async def stop(self, *args):
        await super().stop()
        LOGGER.info('BOT : Exited Successfully ! Bye..........')

revanced_bot = Bot()