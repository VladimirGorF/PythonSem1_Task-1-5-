# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию,
#  после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.
# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!
try:
    a = float(input('Please input first digit '))
    b = float(input('Please input second digit '))
    operation = input('Please input operation ')

    if operation == '*':
        print(a * b)
    elif operation == '/' and b == 0:
        print("You can't divid by Zero")
    elif operation == '/':
        print(a / b)
    elif  operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == 'mod':
        print(a % b)
    elif operation == 'pow':
        print(a ** b)
    elif operation == 'div' and b == 0:
        print("You can't divid by Zero")
    elif operation == 'div':
        print(a // b)
except:
    print('Please be clever!!!!!!')

