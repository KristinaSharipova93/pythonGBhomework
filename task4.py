# Напишите функцию транспонирования матрицы.

matrix = [ [7, 8, 9], [9, 7, 5] ] #coздаем матрицу
trans_matrix = [[matrix[i][j] for i in range (len(matrix))] for j in range(len(matrix[0]))]
#использую 2 вложенных цикла для генерации наших списков
print(matrix)
print(trans_matrix)
