"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv    # Импорт списка аргументов командной строки

def wages_func(user_production, user_rate, user_prize):
    """
    Функция получает параметры и расчитывает заработную плату

    :param user_production: Выработка в часах
    :param user_rate: Ставка в час
    :param user_prize: Премия
    :return: возвращается расчитанная заработная плата
    """

    print("Выработка в часах: ", user_production)
    print("Ставка в час: ", user_rate)
    print("Премия: ", user_prize)
    try:
        user_wages = float(user_production) * float(user_rate) + float(user_prize)  #Перевод параметров в числа и вычесление з/п

        return print(f"Зароботная плата сотрудника составляет - {user_wages}")  # Вывод значения з/п
    except ValueError:                                                              # Обработка ошибки, если параметр не число
        print('Введено неправильное значение. Параметры должны быть числами!' )

try:
    script_name, user_production, user_rate, user_prize = argv     # распаковка содержимого списка argv в переменные
    wages_func(user_production, user_rate, user_prize)             # вызов функции для расчета з/п
except ValueError:                                                 # обработка ошибки, если введены не все парамметры
    print('Необходимо ввести все три параметра')

#assert wages_func(190, 400, 1000) == 77000, 'wages_func(190, 400, 1000)'
"""
тут возникает ошибка которую не могу понять:
при запуске в командной строке - AssertionError: wages_func(190, 400, 1000). 
При запуске в PyCharm - 
Traceback (most recent call last):
  File "D:/Обучение - GeekBrains/Python_bases/Lesson-4/lesson4-1.py", line 28, in <module>
    script_name, user_production, user_rate, user_prize = argv
ValueError: not enough values to unpack (expected 4, got 1)

Но без assert скрипт работает
"""