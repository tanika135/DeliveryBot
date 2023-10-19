from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config_data.config import DEFAULT_COMMANDS
from loader import bot
from states.states import FSMShip
from utils.api_ship import api_request

calculator_router = Router()


@calculator_router.message(Command("calculator"))
async def bot_calculator(message: Message, state: FSMContext) -> None:
    """/calculator — расчет стоимости доставки"""
    await state.set_state(FSMShip.to_city)
    await message.answer(f"Пожалуйста, введите город, в который вы хотите отправить посыпку.")

    # print(api_request('calculator', {
    #     "to": {
    #         "city": "г Санкт-Петербург",
    #     },
    #     "from": {
    #         "city": "г Москва",
    #     },
    #     "places": [{
    #         "height": 45,
    #         "length": 30,
    #         "width": 20,
    #         "weight": 20
    #     }],
    #     "assessedCost": 100,
    # }, 'POST'))

