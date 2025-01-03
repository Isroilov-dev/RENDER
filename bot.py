import os
from dotenv import load_dotenv
import asyncio
from aiogram import Dispatcher as dp  # Replace with your Dispatcher instance
from aiogram import Bot

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    await dp.start_polling(Bot(token=BOT_TOKEN))

if __name__ == "__main__":
    asyncio.run(main())
