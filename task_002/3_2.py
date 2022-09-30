# Задайте список, состоящий из произвольных слов, количество задает пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в список либо сообщит, 
# что ее нет.

# in 6 
# out ['xyz', 'yxz', 'xxz', 'xzy', 'yzz', 'xzy']
# in xzy
# out 3

# in 6
# out ['xyz', 'yxz', 'xxz', 'xzy', 'yzz', 'xzy']
# in yxz
# out -1

from random import choices

def create_list(num, str):
    strings = []
    for item in range(num):
        list = choices(str, k = 3)
        strings.append("".join(list))
    return strings

strings = create_list(40, 'xyz')    
print(strings)

def find_index(list, str):
    if str in list and list.count(str) > 1:
        index = list.index(str)
        print(list.index(str, index +1))
    else: print(-1)

find_index(strings, input("Введите три символа: "))

