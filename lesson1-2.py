n = input("Введите число n - ")
if n.isdigit():
    nn = n * 2
    nnn = n * 3
    sum = int(n) + int(nn) + int(nnn)
    print(sum)
else:
    print("Введено некорректное значение, повторите ещё раз!")