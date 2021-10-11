
class Animal(object):

    animal_code = None
    animal_vid = None
    klichka = None
    okras = None
    data_birthday = None
    FIO = None
    telefon = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def print(self):
        print('Код:', self.animal_code)
        print('Вид:', self.animal_vid)
        print('Кличка: ', self.klichka)
        print('Окрас:', self.okras)
        print('Дата рождения:', self.data_birthday)
        print('ФИО:', self.FIO)
        print('Телефон:', self.telefon)
        print('\n')

    def search_FIO(self, st_FIO):
        if self.FIO==st_FIO:
            self.print()


menu = '''
    1) Добавить животного;
    2) Удалить животного (по коду);
    3) Вывести всех животных;
    4) Вывести животных указанного хозяина;
    0) Выход.
'''

animals = []

while True:
    print(menu)
    try:
        command = int(input('Введите команду: '))
    except:
        command = None
        
    if command == 1:
        animal_code = input('Введите код животного: ')
        animal_vid = input('Введите вид животного: ')
        klichka = input('Введите кличку животного: ')
        okras = input('Введите окрас животного: ')
        data_birthday = input('Введите дату рождения: ')
        FIO = input('Введите ФИО хозяина: ')
        telefon = input('Введите телефон хозяина: ')
        animals.append(Animal(
            animal_code = animal_code,
            animal_vid = animal_vid,
            klichka = klichka,
            okras = okras,
            data_birthday = data_birthday,
            FIO = FIO,
            telefon = telefon)
        )

    elif command == 2:
        animal_code = input('Введите код удаляемого животного: ')
        animals = [item for item in animals if item.animal_code != animal_code]

    elif command == 3:
        for item in animals:
            item.print()

    elif command == 4:
        FIO = input('Введите ФИО хозяина: ')
        for item in animals:
            item.search_FIO(FIO)

    elif command == 0:
        exit(0)

    else:
        print('Неверная команда!')
