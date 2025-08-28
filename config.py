import os
from os import getenv
from dotenv import load_dotenv

if not os.environ.get("ENV"):
    load_dotenv('.env', override=True)

class Config(object):
    try:
        TG_BOT_TOKEN = getenv("TG_BOT_TOKEN")
        APP_ID = int(getenv("APP_ID"))
        API_HASH = getenv("API_HASH")

        #DATABASE_URL = getenv("DATABASE_URL")
        #DATABASE_NAME = getenv("DATABASE_NAME")

        BOT_USERNAME = getenv("BOT_USERNAME")
        ADMINS = set(int(x) for x in getenv("ADMINS").split())

    except:
        print("Telegram Bot: Essential Configs are missing")
        exit(1)

    BASE_DIR = "./bot/"
    WORKING_DIR = BASE_DIR + "STORAGE/"
    TEMP_DIR = WORKING_DIR + "temp/"
    
    # User defined patch file save directory
    CUSTOM_PATCH_FILE = WORKING_DIR + "custom.rvp"

    # Latest CLI from github release
    REVANCED_CLI_PATH = getenv("REVANCED_CLI_PATH", WORKING_DIR + "cli.jar")
    # Default patch file fetched from github release
    REVANCED_PATCH_FILE = getenv("REVANCED_PATCH_FILE", WORKING_DIR + "patches/default.rvp")

    REVANCED_CLI_RELEASES = getenv("REVANCED_CLI_RELEASES", "https://api.github.com/repos/ReVanced/revanced-cli/releases")
    REVANCED_PATCH_RELEASES = getenv("REVANCED_PATCH_RELEASES", "https://api.github.com/repos/ReVanced/revanced-patches/releases")
    REVANCED_API_URL = getenv("REVANCED_API_URL", "https://api.revanced.app/v4")