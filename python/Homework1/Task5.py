""" 
5. Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 
"""


# print('Введите координаты точек A: ')
# xA = float(input('X: '))
# yA = float(input('Y: '))
# print('Введите координаты точек B: ')
# xB = float(input('X: '))
# yB = float(input('Y: '))

# print('Дистанция между А и В: ',(float((xB - xA)**2 + (yB - yA)**2)**(1/2))) # теорема Пифагора


# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

n = int(input('Введите число: '))

if (n%10 == 0 or n%15 == 0) and n%30 !=0:
    print('Выполняется')
else:
    print('Выполняется')