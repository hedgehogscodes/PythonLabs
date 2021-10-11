import math
n = ''
r=0
a=0
b=0
P=0
rm=0
Quit = False
while Quit != True:
    print("\n-----------------Меню-----------------")
    print("«С» площадь круга")
    print("«E» площадь эллипса")
    print("«M» площадь многоугольника")
    print("«Q» выход из программы")
    print("----------------------------------------")

    n = input("Выбирите пункт: ")
    if n=='C':
         try:
                 r=int(input('Введите значение радиуса: '))
         except ValueError:
                 pass  
         while r<=0:
                print("\nНеверное значение радиуса")
                try:
                     r=int(input('Введите значение радиуса: '))
                except ValueError:
                     pass
         print('Площадь круга:', math.pi*r**2)
    elif n=='E':
         try:
                a=int(input('Введите значение большой полуоси: '))
         except ValueError:
                 pass  
         while a<=0:
                print("\nНеверное значение большой полуоси")
                try:
                    a=int(input('Введите значение большой полуоси: '))
                except ValueError:
                     pass
         try:
                b=int(input('Введите значение малой полуоси: '))
         except ValueError:
                 pass  
         while b<=0:
                print("\nНеверное значение малой полуоси")
                try:
                     b=int(input('Введите значение малой полуоси: '))
                except ValueError:
                     pass
         print('Площадь Эллипса:', math.pi*a*b)
    elif n=='M':
         try:
                P=int(input('Введите значение периметра: '))
         except ValueError:
                 pass  
         while P<=0:
                print("\nНеверное значение периметра")
                try:
                    P=int(input('Введите значение периметра: '))
                except ValueError:
                     pass

         try:
                rm=int(input('Введите значение радиуса: '))
         except ValueError:
                 pass  
         while rm<=0:
                print("\nНеверное значение радиуса")
                try:
                    rm=int(input('Введите значение радиуса: '))
                except ValueError:
                     pass
         print('Площадь Многоугольника:', (1/2)*P*rm)
    elif n=='Q':
        Quit = True
    else:
        print("\nНеверный пункт........!\n")