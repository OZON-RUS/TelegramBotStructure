from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

class button_filter(Filter):
    async def __call__(self, message: Message, data: dict):
        existing_menus = data["existing_menus"]
        existing_buttons = data["existing_buttons"]
        state: FSMContext = data["state"]
        data_: dict = await state.get_data()
        if not "current_menu" in data_.keys():
            return False
        
        if message.text in existing_buttons.keys() and message.text in existing_menus[data_["current_menu"]].buttons:
            return {"button_pressed": existing_buttons[message.text]}