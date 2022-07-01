# Fileshare-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
</p>

<p align="center">
  <a href="https://t.me/CodeXBotz">
    <img src="https://github.com/CodeXBotz/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a>
  <a href="https://t.me/mrizmanaziz">
    <img src="https://github.com/CodeXBotz/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a>
</p>


Telegram Bot to store Posts and Documents and it can Access by Special Links.

##
### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- More than one Posts in One Link.
- Can be deployed on heroku directly.

### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 

##
### Installation

#### Deploy on Heroku
**BEFORE YOU DEPLOY ON HEROKU, YOU SHOULD FORK THE REPO AND CHANGE ITS NAME TO ANYTHING ELSE**<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>
<a href="https://youtu.be/LCrkRTMkmzE">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>
**Check This Tutorial Video on YouTube for any Help**<br>
**Thanks to [Erich](https://t.me/ErichDaniken) and his [InFoTel](https://t.me/InFoTel_Group) for this Video**

#### Deploy in your VPS (ubuntu)
````bash
git clone https://github.com/krzky/fileshare
cd File-Sharing-Bot
pip3 install -r requirements.txt
sudo apt install postgresql postgresql-contrib 
# <Create config.py appropriately>
bash start
````
For more database setup at: <a href='https://www.tecmint.com/install-postgresql-and-pgadmin-in-ubuntu'>Link</a>

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users

/ping - check bot availibility

/uptime - check bot uptime
```

### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `API_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/krzky/fileshare/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `FORCE_SUB_CHANNEL2` Optional: ForceSub Channel2 ID, leave 0 if you want disable force sub
* `FORCE_SUB_GROUP` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption


## Support   
Join and support our Coders

[Telegram Group](https://www.telegram.dog/codexbotzsupport & https://t.me/SharingUserbot) For Support/Assistance 

And Our 

[Channel](https://www.telegram.dog/codexbotz & https://t.me/Lunatic0de) For Updates.   
   
Report Bugs, Give Feature Requests There..   

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Special thanks to @mrismanaziz [FILE-SHARING-MAN](https://github.com/mrismanaziz/File-Sharing-Man) & CodeXBotz [FILE-SHARING-BOT](https://github.com/CodeXBotz/File-Sharing-Bot/) who could make this happen

##

   **Star this Repo if you Liked it ⭐⭐⭐**

