import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


if __name__ == "__main__":
    from aiogram import Dispatcher as dp  # Replace with your Dispatcher instance
    from aiogram import Bot
    dp.start_polling(Bot(token=BOT_TOKEN))