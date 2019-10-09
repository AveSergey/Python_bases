n = input("Введите целое положительное число - ")
if n.isdigit():
    max = 0
    n = int(n)
    while n > 0:
        d = n % 10
        n //= 10
        if d > max:
            max = d
    print(max)
else:
    print("Введено некорректное значение, повторите ещё раз!")