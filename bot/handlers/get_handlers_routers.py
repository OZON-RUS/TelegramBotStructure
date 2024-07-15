from bot.handlers.command_handler import router as commands_router
from bot.handlers.button_handler import router as button_router

def get_handlers_routers():
    return [commands_router, button_router]