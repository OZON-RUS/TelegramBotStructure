from inspect import isclass
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from base_types.menu import Menu
from bot import states

class MainMenu(Menu):
    text = "Главное Меню"
    state = states.main_menu
    buttons = ["Мои Тарифы", "Тарифы"]
    reply_markup = Menu.init_markup([["Мои Тарифы","Тарифы"]])
    


def get_existing_menus():
    res: dict = {}
    g = globals()
    for item in g:
        if not isclass(g[item]):
            continue
        if not issubclass(g[item], Menu) or item == "Menu":
            continue
        res[g[item].state.state] = g[item]

    return res