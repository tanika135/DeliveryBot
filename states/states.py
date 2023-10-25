from aiogram.fsm.state import State, StatesGroup


class FSMShip(StatesGroup):
    from_city = State()
    to_city = State()
    places_weight = State()
    places_height = State()
    places_length = State()
    places_width = State()
    assessed_cost = State()


