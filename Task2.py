# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
try:
    X = int(input('Please input an integer 1 '))
    Y = int(input('Please input an integer 2 '))
    Z = int(input('Please input an integer 3 '))

    S = not(X or Y or Z) == (not X  and not Y and not Z)

    print(S)
except:
    print('Please input an integer ')



