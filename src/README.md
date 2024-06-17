<h1 align="center">
  <b>Save restricted content Bot</b>
</h1> 

Contact: [Telegram](https://t.me/MaheshChauhan)

A stable telegram bot to get restricted messages with custom thumbnail support , made by Mahesh Chauhan. 

- works for both public and private chats
- Custom thumbnail support for Pvt medias
- supports text and webpage media messages
- Faster speed
- Forcesubscribe available
- To save from bots send link in this format : `t.me/b/bot_username/message_id` (use plus messenger for message_id)
- `/batch` - (For owner only) Use this command to save upto 100 files from a pvt or public restricted channel at once.
- `/cancel` -  Use this to stop batch
- Time delay is added to avoid FloodWait and keep user account safe. 
  
# Variables

- `API_ID`
- `API_HASH`
- `SESSION`
- `BOT_TOKEN` 
- `AUTH` - Owner user id
- `FORCESUB` - Public channel username without '@'. Don't forget to add bot in channel as administrator. 

# Get API & PYROGRAM string session from:
 
[Telegram.org](https://my.telegram.org/auth)

PYROGRAM SESSION: [SessionGen Bot](https://t.me/SessionStringGeneratorRobot) or [![Run on Repl.it](https://replit.com/badge/github/vasusen-code/saverestrictedcontentbot)](https://replit.com/@levinalab/Session-Generator#main.py)
after link generation do not the new device from your devices in settings.

BOT TOKEN: @Botfather on telegram

# Deploy
```
sudo apt update
sudo apt install ffmpeg git python3-pip
git clone your_repo_link
cd saverestrictedcontentbot 
pip3 install -r requirements.txt
edit config.py
python3 -m main
```

# Notes
when changing bots delete bot.session 
when changing session key delete saverestricted.session
when hosted make sure to check the downloads folder created and remove if some files does not get removed
by any chance to avoid full storage.

- if you want bot to be running in background then enter `screen -S srcb` before `python3 -m main` 
- after `python3 -m main`, click ctrl+A, ctrl+D
- if you want to stop bot, then enter `screen -r srcb` and to kill screen enter `screen -S srcb -X quit`.

Deploy your bot on `Render`

Tutorial - [Click here](https://telegra.ph/SRCB-on-Render-05-17)
