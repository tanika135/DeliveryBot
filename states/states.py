from aiogram.fsm.state import State, StatesGroup


class FSMShip(StatesGroup):
    to_city = State()
    from_city = State()
    places_height = State()
    places_length = State()
    places_width = State()
    places_weight = State()
    assessed_cost = State()


