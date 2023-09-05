# №2 Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

#num = int(input('Введите число: '))
#num2 = num
#res_num = ""
#res_str = ""
#while num > 0:
    #res_str = str(num % 16) + res_num
    #num //= 16
    ######return res_str(лишнее пыталась так сделать )
#print(f'Число {num2} в {16} системе счисления будет: 0x{res_str}')
#print(hex(num2))

#(Задание 1 провально не могу понять почему ? делала по семинару повторно пересматривала но все равно не получается совпадений в ответе)
#Nfr же наконспектировала и опробовала обратный перевод с конвертором тоже что то не получается


#№3.Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#Программа должна возвращать сумму и произведение* дробей.
#Для проверки своего кода используйте модуль fractions.

import fractions
# Преобразуем дроби из строк в числа
num1, denom1 = map(int, input("Введите первую дробь в формате a/b: ").split("/"))
num2, denom2 = map(int, input("Введите вторую дробь в формате c/d: ").split("/"))

# Вычисляем сумму дробей
sum_frac_num = num1 * denom2 + num2 * denom1
sum_frac_denom = denom1 * denom2
sum_frac = (sum_frac_num, sum_frac_denom)

print(f"Сумма дробей {sum_frac_num} и {sum_frac_denom} - {sum_frac[0]}/{sum_frac[1]}")
print(fractions.Fraction(num1, denom1)+fractions.Fraction(num2, denom2))

# Вычисляем произведение дробей
orig_frac_num = num1 * num2
orig_frac_denom = denom1 * denom2
orig_frac = (orig_frac_num, orig_frac_denom)

print(f"Произведение дробей {orig_frac_num} и {orig_frac_denom} - {orig_frac_num}/{orig_frac_denom}")
print("#сокращенная дробь",fractions.Fraction(num1, denom1) * fractions.Fraction(num2, denom2)) #сокращенная дробь


# Решено совместно с коллегами конечно небольшое растройство что сама недогнала это  тренероваться начала на степике чтобы нагнать после командировки
