# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:
    x = int(input('Please input coordinate x '))
    y = int(input('Please input coordinate y '))

    if x > 0 and y > 0:
        print('The point lies in first quarter')
    elif x < 0 and y > 0:
        print('The point lies in second quarter')
    elif x < 0 and y < 0:
        print('The point lies in third quarter')
    elif x > 0 and y < 0:
        print('The point lies in fourth quarter')

    elif x == 0 and y == 0:
        print('The point lies on the center of coordinates')
    elif x == 0:
        print('The point lies on axis Y')
    elif y == 0:
        print('The point lies on axis X')
except:
    print('Please input an integer')
       
