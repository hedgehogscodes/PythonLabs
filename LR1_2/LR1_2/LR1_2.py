a=[]
b=[]
c=[]
n = 0 
res = 0
st = ""
exit = False
countnum = 0
negativecount = 0
bib = dict()
while exit != True:
    print("\n-----------------Меню-----------------")
    print("1 - Показать значения списка")
    print("2 - Добавить в указанную позицию списка")
    print("3 - Удаленить последнего элемента списка")
    print("4 - Сформировать кортеж") 
    print("5 - Найти сумму всех целочисленных отрицательных элементов")
    print("6 - Сформировать строку и посчитать количество букв в строке")
    print("7 - Разница множеств M2 и M1")
    print("8 - Получить из списка словарь")
    print("9 - Выход")
    print("----------------------------------------")

    n = int(input("Выбирите пункт: "))
    if n==1:
        print('\n')
        print('Список:')
        print(a)
    elif n==2:
        print('\n')
        print('Выбирите позицию от 0 до', len(a))
        i = int(input())
        print('Введите значение элемента')
        str1 = input()
        a.insert(i,str1)
        for j, value in enumerate(a):
            try:
                 a[j] = int(a[j])
            except ValueError:
                 pass  
    elif n==3:
        a.pop()
    elif n==4:
        for j in range(0, len(a)):
            proverka=a[j].isdigit()
            if proverka == False:
                b.append(a[j])
        print('\n')
        print('Кортеж:')
        print(tuple(b))
        b.clear()
    elif n==5:
        for j in range(0, len(a)):
            if (type(a[j]) == int):
                if (a[j]<0):
                       res=res+a[j]
        print('\n')
        print('Результат:', res)
        res = 0
    elif n==6:
        for j in range(0, len(a)):
            if type(a[j])==int:
                countnum=countnum+1
                if a[j]<0:
                     negativecount=negativecount+1
            st=st+str(a[j])+" "
        print(st)
        print('Количество букв в строке:', len(st.replace(" ", ""))-countnum-negativecount)
        countnum = 0
        st=""
    elif n==7:
        m1 = set(a)
        m2 = set(c)
        seting = True
        while seting == True:
            vvod=input("Введите значение: ")
            try:
                 vvod = int(vvod)
            except ValueError:
                 pass 
            m2.add(vvod)
            setstop=int(input("Для прододжения заполнения введите 1: "))
            if setstop == 1:
                seting = True
            else:
                seting = False
                print('Множество M1: ', m1)
                print('Множество M2: ', m2)
                print('Разница: ', m2-m1)
    elif n==8:
        for j in range(0, len(a)):
                bib[j] = a[j]
        print('Словарь: ', bib)
        print('Элементы словаря с нечетными значениями ключа: ')
        if len(a)>2:
               for j in range(0, len(a)-2):
                     print(2*j+1,':',bib[2*j+1])  
        elif len(a)==2:
             print(bib[1])
    elif n==9:
        exit = True
    else:
        print("\nНеверный пункт........!\n")



