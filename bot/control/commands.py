from inspect import isclass
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from bot.states import *
from bot.control import menus, buttons
from base_types.command import Command
from utils import funct
from utils import sender

class StartCommand(Command):
    command_text = "/start"
    async def execute(message: Message, data: dict):
        await sender.Menu_Sender.send_menu(message, menus.MainMenu, data)

def get_existing_commands():
    res: dict = {}
    g = globals()
    for item in g:
        if not isclass(g[item]):
            continue
        if not issubclass(g[item], Command) or item == "Command":
            continue
        res[g[item].command_text] = g[item]

    return res