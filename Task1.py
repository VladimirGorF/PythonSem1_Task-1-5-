# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет
# - 
try:
    a = int(input('Please input a day '))
    if a > 0 and a < 6:
        print('This is a working day')
    elif a > 5 and a < 8:
        print('This is a holiday')
    else:
        print('Please input an integer from 1 to 7')
except:
    print('Please input an integer from 1 to 7')

    