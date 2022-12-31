import os
import re

id_pattern = re.compile(r'^.\d+$')
# get a token from @BotFather
TOKEN = os.environ.get("TOKEN", "5747703213:AAH29TN_h_Dnt8gCAlhZSVe8lQx1QMKHfq0")
# The Telegram API things
APP_ID = int(os.environ.get("APP_ID", "10303160"))
API_HASH = os.environ.get("API_HASH", "a479b881a19ec6ddb64ed90f834488e8")
#Array to store users who are authorized to use the bot
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1484847208').split()]
#Your Mongo DB Database Name
DB_NAME = os.environ.get("DB_NAME", "Prv")
#Your Mongo DB URL Obtained From mongodb.com
DB_URL = os.environ.get("DB_URL", "mongodb+srv://YO:YO@cluster0.4j0kwrm.mongodb.net/?retryWrites=true&w=majority")

START_PIC = (os.environ.get("START_PIC", "https://telegra.ph/file/43a52a0192ec02e2fe0e1.jpg")).split()

PORT = os.environ.get("PORT", "8080")

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001554691233")

FLOOD = int(os.environ.get("FLOOD", "5"))
