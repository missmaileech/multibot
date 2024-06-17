from pyrogram import Client

from telethon.sync import TelegramClient

import logging, time, sys

from config2 import API_HASH, API_ID, SESSION, TG_BOT_WORKERS, TG_BOT_TOKEN, FORCESUB, OWNER_ID

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = TG_BOT_TOKEN
SESSION = SESSION
FORCESUB = FORCESUB
AUTH = OWNER_ID

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=TG_BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=TG_BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH,
    workers=TG_BOT_WORKERS,
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
