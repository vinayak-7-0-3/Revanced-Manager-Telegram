# ReVanced Manager Telegram Bot

Trying to replicate the Revanced Manager features in a Telegram Bot.

![GitHub Repo stars](https://img.shields.io/github/stars/vinayak-7-0-3/Revanced-Manager-Telegram?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/vinayak-7-0-3/Revanced-Manager-Telegram?style=for-the-badge)
![Docker Pulls](https://img.shields.io/docker/pulls/weebzbots/revanced-manager-telegrama?style=for-the-badge)
[![Static Badge](https://img.shields.io/badge/support-pink?style=for-the-badge)](https://t.me/weebzgroup)


## FEATURES

**Project is in early development stage and all features from ReVanced Manager is not implemented**

**Implemented Features**
 - Patch given APK using default patch choices.

Feels free to check the repo and report bugs / features

## INSTALLATION


#### 1) LOCAL DEPLOYMENT

**Requirements**
- Python>=3.10 (3.12 recommended) 
- Git installed (optional)

**Steps**
- Install system dependencies
```
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y default-jre-headless

# macOS
brew install openjdk
```
- Git clone (or download) the repo
- Create virtual environment and run
```
virtualenv -p python3 VENV
. ./VENV/bin/activate
```
- Edit and fill out the essentials environment variables in `sample.env` (refer [here](#variables-info))
- Rename `sample.env` to `.env`
- Finally run
```
pip install -r requirements.txt
python -m bot
```

## VARIABLES INFO

#### ESSENTIAL VARIABLES
- `TG_BOT_TOKEN` - Telegeam bot token (get it from [BotFather](https://t.me/BotFather))
- `APP_ID` - Your Telegram APP ID (get it from my.telegram.org) `(int)`
- `API_HASH` - Your Telegram APP HASH (get it from my.telegram.org) `(str)`
- `BOT_USERNAME` - Your Telegram Bot username (with or without `@`) `(str)`
- `ADMINS` - List of Admin users for the Bot (seperated by space) `(str)`

#### OPTIONAL VARIABLES
- `REVANCED_CLI_RELEASES` - Github API URL for ReVanced CLI releases `(str)`
- `REVANCED_PATCH_RELEASES` - Github API URL for ReVanced Patches releases `(str)`
- `REVANCED_API_URL` - ReVanced API URL for fetching informations `(str)`
- `PATCH_TIMEOUT` - Timeout for cancelling the patching process `(int)`


## Usage

### Basic Commands

- `/patch` - Reply to APK file to start the patching process


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [ReVanced Team](https://github.com/ReVanced) for the amazing patching tools

---

Made with ❤️ for the ReVanced community