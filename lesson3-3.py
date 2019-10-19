"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""
import re

def sum_func(var_1, var_2, var_3):
    """
    Функция находит сумму наибольших двух аргументов.

    :param var_1: первое число
    :param var_2: второе число
    :param var_3: третье число
    :return: возвращает сумму двух наибольших аргументов
    """
    arg_sum = var_1 + var_2 + var_3 - min(var_1, var_2, var_3)     # нахождение суммы двух наибольших аргументов
    return arg_sum                                                 # из суммы трех аргументов отнимаем мин. аргумент

try:
    first_num = float(input("Введите первое число - "))
    second_num = float(input("Введите второе число - "))
    third_num = float(input("Введите третье число - "))

    summa = sum_func(first_num, second_num, third_num)
    print(f"Сумма наибольших двух значений равна - {summa}")
except ValueError:
    print("Введено неправильное значение. Введите число!")






