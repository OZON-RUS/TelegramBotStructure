from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import StatesGroup

class Menu(StatesGroup):
    text = None
    prev_menu = None
    state = None
    buttons: list[str] = None
    reply_markup: ReplyKeyboardMarkup = None
    commands: list[str] = []

    def get_keyboard(buttons_array):
        res = []
        for button in buttons_array:
            if type(button) == list:
                res.append(Menu.get_keyboard(button))
            elif type(button) == str:
                res.append(KeyboardButton(text=button))
        return res

    def init_markup(buttons_text):
        keyboard = Menu.get_keyboard(buttons_text)
        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    