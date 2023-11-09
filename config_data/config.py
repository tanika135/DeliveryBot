import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
admin_id = os.getenv("admin_id")


DEFAULT_COMMANDS = (
    ("start", "начало работы с ботом"),
    ("help", "помощь по командам бота"),
    ("calculator", "расчет стоимости доставки"),
    ("history", "вывод истории поиска стоимости")
)
