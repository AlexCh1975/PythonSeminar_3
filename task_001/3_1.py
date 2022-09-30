# Задайте список, состоящий из произвольных чисел, количество задает пользователь.
# Напишите программу, определяющую присутствует ли в заданном списке число,
# полученное от пользователя.

# in 10
#     13
# out [13, 11, 21, 7, 14, 5, 1, 16, 14, 15]
# "The number - 13 is present in the list."

from random import sample

def find_number(q, num = 0):
    q = q if q > 0 else -q
    arr = sample(range(1, q * 2), q) 
    print(arr)
    if num in arr:
        return True
    return 'The number - {} is present in the list.'.format(num)
    

print(find_number(-10, 5))



