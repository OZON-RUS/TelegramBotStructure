from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from base_types.menu import Menu
from utils.text_container import *
from utils import funct

class Menu_Sender:
    async def send_menu(message: Message, menu: Menu, data, user_id=None, text=None):
        if not text:
            text = menu.text

        if user_id == None:
            state: FSMContext = data["state"]
            await message.answer(text, reply_markup=menu.reply_markup)
        else:
            state: FSMContext = FSMContext(funct.get_user_storage(user_id, data), funct.get_user_storage_key(user_id, data))
            await message.bot.send_message(user_id, text, reply_markup=menu.reply_markup)

        await state.update_data({"current_menu": menu.state.state})
        await state.set_state(menu.state)