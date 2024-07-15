from typing import Any
from aiogram.filters import Filter
from aiogram.types import Message
from bot.control import commands

class command_filter(Filter):
    async def __call__(self, message: Message, data: dict):
        existing_commands = data["existing_commands"]
        if message.text in existing_commands.keys():
            return {"command": existing_commands[message.text]}
        else:
            return False