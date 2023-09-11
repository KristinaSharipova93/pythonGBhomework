# Напишите функцию транспонирования матрицы.

matrix = [ [7, 8, 9], [9, 7, 5] ] #coздаем матрицу
trans_matrix = [[matrix[i][j] for i in range (len(matrix))] for j in range(len(matrix[0]))]
#использую 2 вложенных цикла для генерации наших списков
print(matrix)
print(trans_matrix)

#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def hashable_dicts(**kwargs):
    new_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        ##else:
            new_dict[value] = key
    return new_dict


print(hashable_dicts(name=["Кристина", "Вика"], \
                     age=["30", "25"],\
                     work= ["Завод","Школа"]))
