"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

# Сразу устанавливаем проверку на ошибки при роботе с файлами
try:
    with open("text5-2.txt", 'r') as f_obj:   # Используя менеджер контекста открываем файл на чтение
        str_count = 0                         # счетчик строк

        for line in f_obj:                    # Итерация по строкам
            str_count += 1                    # Счетчик строк увеличиваем на 1

            word_count = 0                                # Счетчик слов
            indif = False                                 # Идентификатор, сигнализирующий нахождение за пределами слова
            for word in line:                             # Итерация по символам
                if word != ' ' and indif == False:     # Если символ не"пробел" и идентификатор "вне слова", то начинается новое слово
                    word_count += 1                       # Счетчик слов увеличивается на 1
                    indif = True                          # Идентификатор меняется на "в слове"
                elif word == ' ':                         # Если символ "пробел"
                    indif = False                         # Идентификатор меняется на "вне слове"

            print(f'В {str_count} строке {word_count} слов')   # печатаем количество слов в строке

        print(f'В файле {str_count} строк')                    # Печатаем количество строк в файле

except IOError:
    print('Ошибка ввода-вывода!')