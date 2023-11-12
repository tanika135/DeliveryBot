from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from config_data.config import DEFAULT_COMMANDS
from loader import bot
from states.states import FSMShip
from utils.api_ship import api_request

calculator_router = Router()


class Form(StatesGroup):
    from_city = State()
    to_city = State()
    places_height = State()
    places_length = State()
    places_width = State()
    places_weight = State()


@calculator_router.message(Command("calculator"))
async def bot_calculator(message: Message, state: FSMContext) -> None:
    """/calculator — расчет стоимости доставки"""
    await state.set_state(Form.from_city)
    await message.answer(
        f"Пожалуйста, введите город, из которого вы хотите отправить посыпку.",
        reply_markup=ReplyKeyboardRemove(),
    )


@calculator_router.message(Form.from_city)
async def process_from_city(message: Message, state: FSMContext) -> None:
    await state.update_data(from_city=message.text)
    await state.set_state(Form.to_city)
    await message.answer(
        f"Пожалуйста, введите город, в который вы хотите отправить посыпку.",
        reply_markup=ReplyKeyboardRemove(),
    )


@calculator_router.message(Form.to_city)
async def process_to_city(message: Message, state: FSMContext) -> None:
    await state.update_data(to_city=message.text)
    await state.set_state(Form.places_height)
    await message.answer(
        f"Какова высота посылки?",
        reply_markup=ReplyKeyboardRemove(),
    )


@calculator_router.message(Form.places_height)
async def process_places_height(message: Message, state: FSMContext) -> None:
    await state.update_data(places_height=message.text)
    await state.set_state(Form.places_length)
    await message.answer(
        f"Какова длина посылки?",
        reply_markup=ReplyKeyboardRemove(),
    )


@calculator_router.message(Form.places_length)
async def process_places_length(message: Message, state: FSMContext) -> None:
    await state.update_data(places_length=message.text)
    await state.set_state(Form.places_width)
    await message.answer(
        f"Какова ширина посылки?",
        reply_markup=ReplyKeyboardRemove(),
    )


@calculator_router.message(Form.places_width)
async def process_places_width(message: Message, state: FSMContext) -> None:
    await state.update_data(places_width=message.text)
    await state.set_state(Form.places_weight)
    await message.answer(
        f"Каков вес посылки?",
    )



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

