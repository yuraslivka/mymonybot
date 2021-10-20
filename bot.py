import config
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
   This handler will be called when user sends `/start` or `/help` command
   """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    b = int(message.text)

    if message.text.lower() == '5':
        await message.answer('Fuck you.')
    else:
        if message.text.lower() == '6':
            await message.answer('Yurii.')
        else:
            await message.answer(b*6)


# запускаем лонг поллинг
if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
