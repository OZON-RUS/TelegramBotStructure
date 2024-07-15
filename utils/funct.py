from aiogram import Dispatcher
from aiogram.fsm.storage.base import StorageKey
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from bot.bot_init import bot

def get_user_storage(id, data):
    dispatcher: Dispatcher = data["dispatcher"]
    return dispatcher.fsm.storage

def get_user_storage_key(id, data):
    return StorageKey(bot.id, id, id)