from inspect import isclass
from aiogram.types import KeyboardButton, Message
from aiogram.fsm.context import FSMContext
from bot.control import menus
from utils.text_container import *
from base_types.button import Button
from utils import sender
from utils import funct

class CancelButton(Button):
    button_text = "Назад"
    button = KeyboardButton(text=button_text)
    async def trigger(message: Message, data):
        data_ = await data["state"].get_data()
        existing_menus = data["existing_menus"]
        await sender.Menu_Sender.send_menu(message, existing_menus[data_["current_menu"]].prev_menu, data)

class MyPlanButton(Button):
    button_text = "Мои Тарифы"
    button = KeyboardButton(text=button_text)
    async def trigger(message: Message, data: dict):
        pass

class PlansButton(Button):
    button_text = "Мои Тарифы"
    button = KeyboardButton(text=button_text)
    async def trigger(message: Message, data: dict):
        pass



def get_existing_buttons():
    res: dict = {}
    g = globals()
    for item in g:
        if not isclass(g[item]):
            continue
        if not issubclass(g[item], Button) or item == "Button":
            continue
        res[g[item].button_text] = g[item]

    return res