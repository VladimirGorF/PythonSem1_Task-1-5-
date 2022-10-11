# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева
# направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

try:
    from random import randint
    n = int(input('Please input a qwantity of rows '))
    m = int(input('Please input a qwantity of columns '))
    print()
    matrix = [[randint(1, 9) for j in range(m)] for i in range(n)]
    MatrLine = []

    def printMatrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(f'{matrix[i][j]} ', end="")
            print()
        print()

    def onelineMatrix(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])): # как понять len(matrix[i]) ???  это длина элемента matrix[i] ???
                MatrLine.append(matrix[i][j])

    def sort_onelineMatrix(MatrLine):
        for i in range(len(MatrLine) - 1): # в обоих циклах этой функции использую один и тот же инедкс (i) и только так работает
            for i in range(len(MatrLine) - i - 1): 
                if MatrLine[i] > MatrLine[i + 1]:
                    MatrLine[i], MatrLine[i + 1] = MatrLine[i + 1], MatrLine[i]

    def sortMatrix(MatrLine):
        k = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = MatrLine[k]
                k += 1

    printMatrix(matrix)
    onelineMatrix(matrix)
    sort_onelineMatrix(MatrLine)
    sortMatrix(MatrLine)
    printMatrix(matrix)
except:
    print('Please input an integer!')