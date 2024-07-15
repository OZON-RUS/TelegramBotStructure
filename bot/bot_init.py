from aiogram import Bot
from utils.config_reader import config_reader
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


config = config_reader.get_config()

bot = Bot(config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))