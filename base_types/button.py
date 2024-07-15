from aiogram.types import KeyboardButton, Message

class Button:
    button_text: str = None
    button: KeyboardButton = None

    async def trigger(message: Message, data: dict):
        raise NotImplemented
    


    
