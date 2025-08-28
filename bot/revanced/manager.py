import os
import shutil

from aiohttp import ClientSession, ClientTimeout

from bot import Config, LOGGER
from ..helpers.utils import download_file
from .utils import get_asset_url



class RevancedManager:
    session: ClientSession

    def __init__(self):
        pass

    async def fetch_files(self):
        self.session = ClientSession(timeout=ClientTimeout(total=30))

        LOGGER.debug('Fetching latest Revanced CLI')
        cli_url = await get_asset_url(self.session, Config.REVANCED_CLI_RELEASES)
        await download_file(self.session, cli_url, Config.REVANCED_CLI_PATH)

        LOGGER.debug('Fetching Revanced Patches')
        patches_url = await get_asset_url(self.session, Config.REVANCED_PATCH_RELEASES)
        await download_file(self.session, patches_url, Config.REVANCED_PATCH_FILE)


    async def cleanup(self):
        if os.path.isdir(Config.TEMP_DIR):
            shutil.rmtree(Config.TEMP_DIR)

        if self.session:
            await self.session.close()


revanced_manager = RevancedManager()