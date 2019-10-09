sec = input("Введите время в секундах - ")
if sec.isdigit():
    sec = int(sec)
    h = ((sec//3600))%24
    m = (sec//60)%60
    s = sec%60
    print( '{0:=02}:{1:=02}:{2:=02}'.format(h, m, s) )
else:
    print("Введено некорректное значение, повторите ещё раз!")