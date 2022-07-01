import logging
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5463304740:AAHkiVoBoOteppv5qoUN8JWj_bPJzg1ziFk")

# API ID my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16202200"))

# API Hash my.telegram.org
API_HASH = os.environ.get("API_HASH", "84399d304c1a903c09e873d013f4f1a7")

# Channel Database ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001783585328"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "784850011"))

# OWNER ID
#OWNER = os.environ.get("OWNER", "-")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://kay:Botkzkay@kz/kay")

# Force sub channel id, if you want enable force sub, leave 0 for none
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001650013655"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001150482751"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001524885114"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>I can store private files in Specified Channel and other users can access it from special link.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "784850011 5058392474").split())]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers..")

# Force sub message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nYou need to join in my Channels & Group to use me\n\nPlease join the Channel first!</b>",
)

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
#PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.extend((OWNER_ID, 784850011, 1250450587, 5058392474))

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, 
        maxBytes=50000000, 
        backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
