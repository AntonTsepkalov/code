# Hi

# How_are_you

# What_is_the_weather_outside_the_window

# What_is_your_name

# How_many_days_are_you

# What_time_is_it_now


import os
import json
import random
import logging


from aiogram import Bot, Dispatcher, executor, types



path = "D:\code\some_answers/"

my_answers = {}
with open(path + 'main.json', 'r',encoding='utf-8') as f:
    my_answers = json.load(f)
print(my_answers)


def get_answer_from_file(filename,path):
    with open(path +filename, 'r', encoding='utf-8') as f:
        return random.choice(f.readlines())
    


API_TOKEN = '5987878976:AAHiieP2m7mzt3dFCuUUJBKV3AQTFpRykr4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привіт, я можу відповідати на запитання:\n" + "\n".join(my_answers.keys()))



@dp.message_handler()
async def echo(message: types.Message):
    input_text = message.text.strip().capitalize()
    if input_text in my_answers.keys():
        answer = get_answer_from_file(my_answers[input_text],path)
        await message.answer(answer)
    else:
        await message.answer("Напиши мені привіт))\n Або спрбуй команду /help")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)