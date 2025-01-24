from multiprocessing.connection import answer_challenge

from config import TOKEN  # Убедитесь, что ваш токен хранится в config.py
import logging

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random
from gtts import gTTS
import os
import keyboards as kb


API_TOKEN = TOKEN


bot=Bot(token=TOKEN)
dp= Dispatcher()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Этот бот что-то там делает...{message.from_user.first_name}', reply_markup=await kb.test_keyboard())

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer(f'Приветствую Вас!  {message.from_user.first_name}', reply_markup=await kb.test_keyboard())


# Функция запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())