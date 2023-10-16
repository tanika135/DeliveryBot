import logging
import sys
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config_data import config
from handlers.help import help_router
from handlers.start import start_router

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

else:
    loop = asyncio.get_event_loop()


async def on_startup(_):
    print('running')


async def main() -> None:
    dp = Dispatcher(loop=loop, storage=MemoryStorage())
    dp.include_routers(
        help_router,
        start_router,
    )

    bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

