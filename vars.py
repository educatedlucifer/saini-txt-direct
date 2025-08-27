#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27834178"))
API_HASH = environ.get("API_HASH", "ce3fa1d03f49420c1727f5b3f80dd890")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "7589886020"))
CREDIT = environ.get("CREDIT", "ᵉᵈᵘᶜᵃᵗᵉᵈˡᵘᶜⁱᶠᵉʳ")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7589886020').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7589886020').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

