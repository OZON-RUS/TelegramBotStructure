from os import environ

class Config:
    BOT_TOKEN = None
    REDIS_PORT = None
    REDIS_URL = None
    SQL_DB_URL = None

    def __init__(self, BOT_TOKEN, REDIS_PORT="6382", SQL_DB_URL = "sqlite+aiosqlite:///../AnonChatDB.sqlite3", REDIS_URL = "redis://localhost:"):
        self.BOT_TOKEN = BOT_TOKEN
        self.REDIS_PORT = REDIS_PORT
        self.REDIS_URL = REDIS_URL + REDIS_PORT
        self.SQL_DB_URL = SQL_DB_URL

class config_reader:
    def get_config() -> Config:
        return Config(environ.get("BOT_TOKEN"), environ.get("REDIS_PORT", "6382"))