from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot
from utils.api_ship import api_request

# async def start_bot(dp):
#     await bot.send_message(chat_id=admin_id, text='бот запущен')

help_router = Router()


@help_router.message(Command("help"))
async def bot_help(message: Message):
    """/help — помощь по командам бота"""

    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    await bot.send_message(chat_id=message.from_user.id,
                           text="\n".join(text))
    # text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]DEFAULT_COMMANDS
    # bot.reply_to(message, "\n".join(text))

