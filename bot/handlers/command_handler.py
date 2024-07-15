from aiogram import Router
from aiogram.types import Message
from bot.filters.command_filter import command_filter
from base_types.command import Command


router = Router()

@router.message(command_filter())
async def command_handler(message: Message, command: Command, data: dict):
    await command.execute(message, data)