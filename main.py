from configparser import ConfigParser
import logging
import asyncio
# from time import gmtime, strftime, localtime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


config = ConfigParser()
config.read("config.ini")


TOKEN = config['token']['TOKEN']


logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()

bot = Bot(token=TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage, loop=loop)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение"""
    # await do_remember_user_start(message)
    hello_message = "Здарова ты лох"
    await message.answer(hello_message)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def text_question_handler(message: types.Message):
    """Обрабатывает прочие сообщения"""
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


