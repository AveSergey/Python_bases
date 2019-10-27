"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
"""

import json                               # Импорт модуля JSON

try:
    with open("text5-6.txt") as my_file:      # Открытие файла для чтения
        j_str = json.loads(my_file.read())    # Сериализация файла, для преобразования в словарь
        print(j_str)

    main_dict = {}                            # Создаем новый словарь для хранения названия предмета и общего количества занятий
    for key, value in j_str.items():          # С помощью итерации создаём словарь из значений исходного словаря
        my_dict = value
        class_num = 0                         # Счетчик общего количества занятий
        for k, v in my_dict.items():
            class_num += v                    # Определяем общее количество занятий
        new_dict ={key: class_num}            # Новые словари из названия предмета и общего количества занятий
        main_dict.update(new_dict)            # Полученные словари объединяем в один словарь
    print(main_dict)                          # Выводим словарь на экран

except IOError:
    print('Ошибка ввода-вывода!')