# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "25637343"))
API_HASH = getenv("API_HASH", "70fb79a89ec2d30cab05704e817e5be6")
BOT_TOKEN = getenv("BOT_TOKEN", "7799682099:AAGxNrldfl42hSGqclaOX2RctmgO6E-M9uw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5390137933").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ellie535091:A8sx0Q3dVNPPku18@cluster0.ry133.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002039915658")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002386527380"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
