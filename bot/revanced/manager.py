import os
import shutil

from aiohttp import ClientSession, ClientTimeout

from bot import Config, LOGGER
from ..helpers.utils import download_file
from .utils import get_asset_url



class RevancedManager:
    session: ClientSession

    def __init__(self):
        self.patches_list = []
        self.default_source = 'github'


    async def setup(self):
        await self.fetch_files()
        await self.fetch_all_patches()


    async def fetch_files(self):
        self.session = ClientSession(timeout=ClientTimeout(total=30))

        LOGGER.debug('Fetching latest Revanced CLI')
        cli_url = await get_asset_url(self.session, Config.REVANCED_CLI_RELEASES)
        await download_file(self.session, cli_url, Config.REVANCED_CLI_PATH)

        LOGGER.debug('Fetching Revanced Patches')
        patches_url = await get_asset_url(self.session, Config.REVANCED_PATCH_RELEASES)
        await download_file(self.session, patches_url, Config.REVANCED_PATCH_FILE)



    async def fetch_all_patches(self):
        """Saves all patches info from ReVanced API"""
        try:
            url = f"{Config.REVANCED_API_URL}/patches/list"
            async with self.session.get(url) as response:
                if response.status != 200:
                    return
                self.patches_list = await response.json() 
        except Exception as e:
            LOGGER.error(f"Revanced: Error getting all patches information from API - {e}")
            return



    def get_available_patches(self, package_name:str):
        """Get list of patches for the provided apk package"""
        package_patches = []
        for patch in self.patches_list:
            compatible_packages = patch.get('compatiblePackages')
            if compatible_packages:
                for pkg in compatible_packages:
                    if pkg == package_name:
                        package_patches.append({
                            'name': patch.get('name'),
                            'description': patch.get('description'),
                            'options': patch.get('options', []),
                            'use': patch.get('use', True)
                        })
                        break

        return package_patches



    async def cleanup(self):
        """Cleans up temp directory and close aiohttp session"""
        if os.path.isdir(Config.TEMP_DIR):
            shutil.rmtree(Config.TEMP_DIR)

        if self.session:
            await self.session.close()



revanced_manager = RevancedManager()