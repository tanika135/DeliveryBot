import datetime

from peewee import *
from database.storage_postgresql import db


class BaseModel(Model):
    class Meta:
        database = db


class History(BaseModel):
    id = PrimaryKeyField(null=False)
    chat_id = IntegerField(null=False)
    from_city = CharField(null=False)
    to_city = CharField(null=False)
    places_weight = FloatField(null=False)
    date = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = "Search history"
        order_by = ("id",)


class Shipping_costs(BaseModel):
    id = PrimaryKeyField(null=False)
    id_history = IntegerField(null=False)  # Общее поле для таблицы History и Shipping_costs
    provider_key = CharField(null=False)  # Название службы доставки
    tariff_name = CharField(null=False)
    delivery_cost = FloatField(null=False)

    class Meta:
        db_table = "Shipping costs"
        order_by = ("id",)
