import datetime
import os
from peewee import *
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

user = os.getenv("user")
password = os.getenv("password")
db_name = "postgresql_database"

db = PostgresqlDatabase(
    db_name, user=user,
    password=password,
    host="localhost"
)


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
        db_table = "search_history"
        order_by = ("id",)


class Shipping_costs(BaseModel):
    id = PrimaryKeyField(null=False)
    id_history = IntegerField(null=False)  # Общее поле для таблиц History и Shipping_costs
    provider_key = CharField(null=False)  # Название службы доставки
    tariff_name = CharField(null=False)
    delivery_cost = FloatField(null=False)

    class Meta:
        db_table = "shipping_costs"
        order_by = ("id",)
