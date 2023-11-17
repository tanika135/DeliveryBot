import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
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
    calculate_cost = State()


@calculator_router.message(Command("calculator"))
async def bot_calculator(message: Message, state: FSMContext) -> None:
    """/calculator — расчет стоимости доставки"""
    await state.set_state(Form.from_city)
    await message.answer(
        f"Пожалуйста, введите город, из которого вы хотите отправить посыпку.",
        reply_markup=ReplyKeyboardRemove(),
    )


@calculator_router.message(Command("cancel"))
@calculator_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )


@calculator_router.message(Form.from_city)
async def process_from_city(message: Message, state: FSMContext) -> None:
    await state.update_data(from_city=message.text)
    await state.set_state(Form.to_city)
    await message.answer(
        f"Пожалуйста, введите город, в который вы хотите отправить посыпку.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@calculator_router.message(Form.to_city)
async def process_to_city(message: Message, state: FSMContext) -> None:
    await state.update_data(to_city=message.text)
    await state.set_state(Form.places_height)
    await message.answer(
        f"Какова высота посылки?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="cancel"),
                ]
            ],
            resize_keyboard=True,
        ),
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
        reply_markup=ReplyKeyboardRemove(),
    )


@calculator_router.message(Form.places_weight)
async def process_places_weight(message: Message, state: FSMContext) -> None:
    await state.update_data(places_weight=message.text)
    await state.set_state(Form.calculate_cost)
    data = await state.get_data()
    await state.clear()

    await message.answer(
        f"Общая информация\n\n"
        f"Город отправления: {data['from_city']}\n"
        f"Город назначения: {data['to_city']}\n"
        f"Высота посылки: {data['places_height']}\n"
        f"Длина посылки: {data['places_length']}\n"
        f"Ширина посылки: {data['places_width']}\n"
        f"Вес посылки: {data['places_weight']}\n\n"
        f"Рассчитать стоимость?\n",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Да"),
                    KeyboardButton(text="Нет"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


# @calculator_router.message(Form.calculate_cost, F.text.casefold() == "да")
# async def process_calculate_cost(message: Message, state: FSMContext) -> None:
#     # await state.set_state(Form.language)
#
#     await message.reply(
#         "Cool! I'm too!\nWhat programming language did you use for it?",
#         reply_markup=ReplyKeyboardRemove(),
#     )



