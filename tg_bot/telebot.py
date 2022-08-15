from aiogram import types, Bot, Dispatcher, executor
import config
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
     "Hi! {0}. It is auto registration-authorization bot.".format(message.from_user.first_name))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
