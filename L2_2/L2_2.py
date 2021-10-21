import math

Krug = lambda a, h: a * h**2
ellips = lambda a, b: math.pi * a * b
mnogoug = lambda p, b: 0.5 * p * b
exit = lambda x, y: x * y * 0 == 0


while True:
    list_arg = []
    list_arg.append(list(input("Введите команды через пробел (C, E, M, Q): ").split()))
    try:
        list_arg.append([list(map(int,input("Введите {0} значения: ".format(2)).split())) for i in list_arg[0]])
        print(list_arg)
        answer = list(map(lambda x, y:
           (x=="C" and Krug(y[0], y[1])) or (x=="E" and ellips(y[0], y[1])) 
           or (x=="M" and mnogoug(y[0], y[1])) or (x=="Q" and exit(y[0], y[1])) or "", list_arg[0], list_arg[1]))
        print(answer)
        exi = lambda: ((True in answer) and exit(0)) or ""
        print(exit())
    except:
        print("Ошибка в данных")
