from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from utils.config_reader import *
from bot.handlers.get_handlers_routers import get_handlers_routers
from bot.middlewares.outer import *
from bot.control import buttons
from bot.control import menus
from bot.control import commands
from bot import bot_init
from database import Base



async def on_startup(engine_: AsyncEngine):
    async with engine_.begin() as connector:
        await connector.run_sync(Base.metadata.create_all)

def main():
    config = config_reader.get_config()
    bot = bot_init.bot
    engine_ = create_async_engine(config.SQL_DB_URL)
    sessionmaker_ = async_sessionmaker(engine_, expire_on_commit=False)

    MIDDLEWARES = []
    OUTER_MIDDLEWARES = [data_(), DBSession(sessionmaker_)]
    ROUTERS = get_handlers_routers()
    
    dispatcher = Dispatcher(existing_buttons = buttons.get_existing_buttons(), existing_menus = menus.get_existing_menus(),
                            existing_commands = commands.get_existing_commands(),
                            storage=RedisStorage.from_url(config.REDIS_URL), engine_=engine_)


    for middleware in MIDDLEWARES:
        dispatcher.message.middleware.register(middleware)
    for middleware in OUTER_MIDDLEWARES:
        dispatcher.message.outer_middleware.register(middleware)
    dispatcher.startup.register(on_startup)
    dispatcher.include_routers(*ROUTERS)

    dispatcher.run_polling(bot)

if __name__ == "__main__":
    main()