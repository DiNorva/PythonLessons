""" 
1. Напишите программу, которая принимает на вход вещественное число 
и показывает сумму его цифр.
НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку
Пример:
6782 -> 23
0,56 -> 11 
"""


num = input('Введите дробное число через точку: ')
sum = 0

for i in num:
    if float(num) < 0:
        num = float(num) * (-1)
    elif i != '.':
        sum += int(i)

print('Сумма чисел = ', sum)

