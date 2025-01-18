import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7383786168:AAFweJcL-csENpXnvb3z5HZrfgNT4hJ-LMU")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20445873"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "057fd0be9d7c38526b143c582bceb24b")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6975428639, 5543390445, 7607741983, 5164955785"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://renamebot:amrenamebot@cluster0.5ornz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
