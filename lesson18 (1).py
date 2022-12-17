# Написать программу, которая решает математический пример из файла, а так же записывает результат обратно в файл.
# Пример:
# Строка в файле
# 34 + 22 - 11 * 10
# После работы вашей программы
# 34 + 22 - 11 * 10 = -54
# то есть в файл дозаписался ответ после вычисления!
# Файл с заданием в приложении к дз.
# ПРОВЕРКА НА 0))))))))))))))) (Рекомендую создать функцию для єтого!!!)
# Советую загуглить метод для этих целей))

# eval()
# from os import path

# file_name = 'file_name.txt'
# file_path=r'F:\DotPack Projects\HILLEL\2827CoffeeChamplsElecton\lesson18'
# file_path = path.join( file_path, file_name)
# print(file_path)
    
# all_lines = []

# with open(file_path, 'r') as f:
#     all_lines = f.readlines()
# # print(all_lines)

# for i in range(0, len(all_lines) - 1):
#     try:
#         otvet = str(eval(all_lines[i]))
#     except ZeroDivisionError:
#         otvet = 'OoPPS! ZERO'
#     all_lines[i] =  all_lines[i].strip() + ' = ' + otvet + '\n'

# # print(all_lines)

# with open(file_path, 'w') as f:
#     f.writelines(all_lines)
    
    
    
# Прочитать строку з файла, в которой буква "h" встречается как минимум два раза. Выведите последовательность символов, заключенную между первым и последним появлением буквы "h", в противоположном порядке



# (строка 1, больше нет)
# (название файла file.txt)
# (сделать для названия переменную для удобной смени)
# (Использовать Функции)
# ( (ВОЗМОЖНОСТЬ) Букву "h" поменять на любой другой символ например, компания поменяла кодировку и теперь знак "!")    
    
# asdasdasdasdasd@Hello@fgkljsdfsdfsdljkfh
# all_text = ''
# symbol = '!'

# with open( file_path, 'r') as f:
#     all_text = f.read()

# left = all_text.index(symbol)
# right = all_text.rindex(symbol)
# print(all_text[right-1:left:-1])



# Написать программу, которая генерит случайное количество файлов от 2 до 10 
# (создайте отдельную папку, и в неё записываете фалы, создать кодом :) ),
# заполняет эти файлы случайными числами (Количество случайных чисел от 1 до 10000)
# и диапазон случайных чисел от 1 до 1000.
# Найти одинаковые элементы, которые содержаться во всех
# файлах и записать их в файл под названием result.txt

# не забудьте добавить возможность смени названия папки, 
# где будут все ваши сгенерированные файли
# result.txt тоже в ту папку положить

# def sdasdasd(a):
#     return a > 10
    
# print(list(map(sdasdasd,[3,5,10,19,2,6,11,66,2,4,6,10])))




import os
from os import path
import shutil
import random

file_name = 'file_name_'
folder_name = 'Kalina'

_path=r'F:\DotPack Projects\HILLEL\2827CoffeeChamplsElecton\lesson18'
file_path = path.join( _path, file_name)
folder_name = path.join( _path, folder_name)
# print(file_path)


if path.isdir(folder_name):
    shutil.rmtree(folder_name)

os.mkdir(folder_name)


for i in range(random.randint(2,10)):
    with open(path.join( folder_name, f'{file_name}{i}.txt'),'w') as f:
        f.write(' '.join(map(str,[random.randint(1,5) for _ in range(random.randint(1,100))])))

# [folder_name for el in range(len(os.listdir(folder_name)))]
# os.listdir(folder_name)

# print([folder_name for el in range(len(os.listdir(folder_name)))])
# print(os.listdir(folder_name))

all_my_files = map(path.join,[folder_name for el in range(len(os.listdir(folder_name)))],os.listdir(folder_name))

all_data_files = []

for ff_name in all_my_files:
    with open( ff_name, 'r' ) as f:
        all_data_files.append(set(f.read().split()))


#print(all_data_files)
unique_data = all_data_files[0]
for el in all_data_files:
    unique_data = unique_data.intersection(el)
    
print(unique_data)

with open( path.join(folder_name,'result.txt'), 'w' ) as f:
    f.write(' '.join(unique_data))