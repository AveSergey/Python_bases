"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""

def user_data_func(name, surname, birth_year, residence_city, e_mail, tel_number):
    """
    Функция принимает именованные аргументы и выводит данные о пользователе одной строкой

    :param name: Имя
    :param surname: Фамилия
    :param birth_year: год рождения
    :param residence_city: город проживания
    :param e_mail: эл. почта
    :param tel_number: номер телефона
    :return: данные о пользователе одной строкой
    """
    return print(f"Имя: {name}, Фамилия: {surname}, год рождения: {birth_year}, город проживания: {residence_city}, "
                 f"e-mail: {e_mail}, телефон: {tel_number}")


user_data_func(name = "Вася", surname = "Пупкин", birth_year = 1927, residence_city = "Нью-Васюки",
               e_mail = "pupkin@ya.ru", tel_number = "+7(499)123-45-67")