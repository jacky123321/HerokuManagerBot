import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","2078246533:AAH75DmLh9UVSVvGkYZ38MBGBV0kFlahV64")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY","cf588226-9ad9-450e-a4f2-d80965171111")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split("1378212735")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME","")
