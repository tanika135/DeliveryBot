import peewee
from models import *


def add_history(
        chat_id: int,
        from_city: str,
        to_city: str,
        places_height: float,
        places_length: float,
        places_width: float,
        places_weight: float,
        date
):
    row = History(
        chat_id=chat_id,
        from_city=from_city,
        to_city=to_city,
        places_height=places_height,
        places_length=places_length,
        places_width=places_width,
        places_weight=places_weight,
        date=date
    )

    row.save()


if __name__ == '__main__':
    try:
        # db.connect()
        History.create_table()
        add_history(1, "Москва", "Санкт-Петербург", 18.3, 14.2, 16.2, 16.2, datetime.datetime.now())
        print('success')
    except peewee.InternalError as px:
        print(str(px))
    try:
        # db.connect()
        Shipping_costs.create_table()
    except peewee.InternalError as px:
        print(str(px))



