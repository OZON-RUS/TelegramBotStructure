from aiogram import Router
from aiogram.types import Message
from bot.filters import button_filter
from base_types.button import Button

router = Router()

@router.message(button_filter())
async def button_handler(message: Message, button_pressed: Button, data: dict):
    await button_pressed.trigger(message, data)