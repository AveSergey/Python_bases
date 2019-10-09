revenue = float(input("Введите значение выручки - "))
costs = float(input("Введите значение издержки фирмы - "))

"""
в этом примере не стал проверять на условие .isdigit(), чтоб использовать числа с плавающей точкой.
проверку можно сделать с помощью конструкции Try-Except, но для первого урока рано)))
"""

if revenue < costs:
    print("Фирма работает с убытком")
elif revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue
    print("Фирма работает с прибылью.\nРентабельность составляет -", '{0:.2f}'.format(profitability))

    num = int(input("Введите численность сотрудников фирмы - "))
    emp_profit = profit / num
    print("Прибыль фирмы в расчете на одного сотрудника составляет -", '{0:.2f}'.format(emp_profit))