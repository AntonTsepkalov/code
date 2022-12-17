# +++++++++++++++++++++++++++++++++++++++ LESSON 17  +++++++++++++++++++++++++++++++
# Создать алгоритм игры "Города". То есть правила такие :
# Есть словарь со столицами стран. (10ть столиц стран на твой выбор)
# Пользователь "бесконечно" вводит название городов и программа на основе
# словаря выдает ответ да это столица такой то страны или нет увы это не
# столица если такой столицы у 10и стран из словаря нет. или введите слово 
# стоп, которое закончит цикл.


# sity_dict = {
#     'kyiv':'Ukraine',
#     'minsk':'Belarus',
#     'warsaw':'Poland',
#     'brasilia':'Brazil',
#     'athens':'Greece',
#     'berne':'Switzerland',
#     'bucharest':'Romania',
#     'buenos aires':'Argentina',
#     'vilnius':'Lithuania','zagreb':'Croatia','cairo':'Egypt','kishinev':'Moldova','oslo':'Norway','ottawa':'Canada','rome':'Italy','tokyo':'Japan'
# }
# while True:
#     city_input = input("Input City: ").lower()
#     if city_input == 'stop':
#         break
#     elif city_input in sity_dict.keys():
#         print(f"Sity: {city_input.capitalize()}, country: {sity_dict.get(city_input).capitalize()}")
#     else:
#         print(f"Try again")

# +++++++++++++++++++++++++++++++++++++++ LESSON 17 end +++++++++++++++++++++++++++++++


# +++++++++++++++++++++++++++++++++++++++ LESSON 18  +++++++++++++++++++++++++++++++
# Створіть функцію, яка приймає список, індекс початку сортування 
# та індекс кінця сортування, і повертає список, у якому відсортовано 
# лише ті елементи, які укладені між індексом початку
# сортування та індексом кінця сортування.

# У відповідь вернуть початковий список, але з відсортованою частиною!

# Зробити змінні для зручного виставлення індексів
# програма повинна тільки надрукувати список
# підпишіть коментарями як працює ваша функція
# довжина списку не більше 1000

# def sort_by_part(some_list:list, start:int, end:int) -> list:
#     if start < 0 or end > len(some_list):
#         raise
#     done_list = some_list[:start] + sorted(some_list[start:end]) + some_list[end:] 
#     return done_list
    
# my_list = [3,3,3,7,7,7,6,6,6,65,5,4,3,2,3,3,3,3,3,3,3,6,6,6,6,7,8,8,88]
# print(my_list)
# print(sort_by_part(my_list,3,8))
# +++++++++++++++++++++++++++++++++++++++ LESSON 18 end +++++++++++++++++++++++++++++++


# +++++++++++++++++++++++++++++++++++++++ LESSON 19  +++++++++++++++++++++++++++++++

# Створіть словник із кількістю елементів щонайменше 
# п'ять за допомогою рандома. Поміняйте місцями перший
# та останній елемент об'єкта. Видаліть другий елемент. 
# Додайте до кінця ключ «new_key» зі значенням «new_value».
# Виведіть на друк підсумковий словник.
# Коментарі для кожної із задач

# from random import randint as rd
# rnd_dict = {}
# while len(rnd_dict.keys()) < 5 :
#     key = "key_" + str(rd(1,10000))
#     value = "value_" + str(rd(0,10000))
#     rnd_dict[key] = value
# print(rnd_dict)
    

# keyss = list(rnd_dict.keys())
# values = list(rnd_dict.values())
# keyss[0], keyss[-1] = keyss[-1], keyss[0]
# values[0], values[-1] = values[-1], values[0]


# # my_dict = dict(zip(keyss, values))
# my_dict = {}
# for i in range(len(keyss)):
#     my_dict[keyss[i]] = values[i]

# print(my_dict)
# my_dict.pop(list(rnd_dict.keys())[1])
# print(my_dict)

# +++++++++++++++++++++++++++++++++++++++ LESSON 19 end +++++++++++++++++++++++++++++++







# +++++++++++++++++++++++++++++++++++++++ LESSON 20  +++++++++++++++++++++++++++++++
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


# from aiogram import Bot, Dispatcher, executor, types



# path = "F:/DotPack Projects/HILLEL/2827CoffeeChamplsElecton/lesson23/some_answers/"

# my_answers = {}
# with open(path + 'main.json', 'r',encoding='utf-8') as f:
#     my_answers = json.load(f)
# print(my_answers)


# def get_answer_from_file(filename,path):
#     with open(path +filename, 'r', encoding='utf-8') as f:
#         return random.choice(f.readlines())
    


# API_TOKEN = '5737819587:AAEDiguDeYdWON94k6MusxfHuHUUfncTtaY'

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Привіт, я можу відповідати на запитання:\n" + "\n".join(my_answers.keys()))



# @dp.message_handler()
# async def echo(message: types.Message):
#     input_text = message.text.strip().capitalize()
#     if input_text in my_answers.keys():
#         answer = get_answer_from_file(my_answers[input_text],path)
#         await message.answer(answer)
#     else:
#         await message.answer("Напиши мені привіт))\n Або спрбуй команду /help")


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)




# +++++++++++++++++++++++++++++++++++++++ LESSON 20 end +++++++++++++++++++++++++++++++




# OFFF TOPP


# Создать математическую игру в которую можно играть через телеграм.

# Бот генерирует пример (пример на основные 4е действия +-*/) и пользователь вводит ответ, если ответ правильный то +1 к 

# количеству правильных ответов, если ответ не правильный то -1.

# Останавливать игру по вводу системной команды /stop_game и возвращать в сообщении количество примеров за игру 

# и количество правильных и неправильных ответов.



# Так же возвращать Веселый стикер если кол-во правильных ответов больше чем неправильных иначе возвращать грустный стикер(
    
# znak = random.choice('+-*/')
# print(znak)
# q = f'{random.randint(1,100)} {znak} {random.randint(1,100)}'
# print(f'Спробуй відповісти:\n{q}')

# answer = int(input())
# q_answer = round(eval(q))

# if answer == q_answer:
#     print('Answer TRUE', q_answer)
# else:
#     print('Answer FALSE', q_answer)



