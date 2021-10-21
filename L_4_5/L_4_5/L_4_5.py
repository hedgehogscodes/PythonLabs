from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
from tkinter import filedialog

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

    def saved(self):
        s1 = '_'.join(self.animal_code.split())
        s2 = '_'.join(self.animal_vid.split())
        s3 = '_'.join(self.klichka.split())
        s4 = '_'.join(self.okras.split())
        s5 = '_'.join(self.data_birthday.split())
        s6 = '_'.join(self.FIO.split())
        s7 = '_'.join(self.telefon.split())
        return '{0} {1} {2} {3} {4} {5} {6}\n'.format(s1, s2, s3,  s4,
                                            s5, s6, s7)

animals = []
labels = ['Код', 'Вид', 'Кличка', 'Окрас', 'Дата рождения', 'ФИО хозяина', 'Телефон']

class Ui_MainWindow(object):
    file_name1 = ""
    file_name = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 944)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showall = QtWidgets.QPushButton(self.centralwidget)
        self.showall.setGeometry(QtCore.QRect(580, 180, 281, 61))
        self.showall.setObjectName("showall")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 151, 16))
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 200, 161, 16))
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 170, 141, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 110, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(190, 240, 93, 28))
        self.add_btn.setObjectName("add")
        self.klichka = QtWidgets.QLineEdit(self.centralwidget)
        self.klichka.setGeometry(QtCore.QRect(200, 80, 91, 22))
        self.klichka.setObjectName("klichka")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 171, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 181, 16))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 240, 121, 20))
        self.checkBox.setObjectName("checkBox")
        self.code = QtWidgets.QLineEdit(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(180, 20, 111, 22))
        self.code.setObjectName("code")
        self.telxoz = QtWidgets.QLineEdit(self.centralwidget)
        self.telxoz.setGeometry(QtCore.QRect(190, 200, 101, 22))
        self.telxoz.setObjectName("telxoz")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 151, 16))
        self.label_5.setObjectName("label_5")
        self.fioxoz = QtWidgets.QLineEdit(self.centralwidget)
        self.fioxoz.setGeometry(QtCore.QRect(170, 170, 121, 22))
        self.fioxoz.setObjectName("fioxoz")
        self.dateof = QtWidgets.QLineEdit(self.centralwidget)
        self.dateof.setGeometry(QtCore.QRect(180, 140, 111, 22))
        self.dateof.setObjectName("dateof")
        self.vid = QtWidgets.QLineEdit(self.centralwidget)
        self.vid.setGeometry(QtCore.QRect(180, 50, 111, 22))
        self.vid.setObjectName("vid")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(860, 70, 93, 28))
        self.search.setObjectName("search")
        self.searchfio = QtWidgets.QLineEdit(self.centralwidget)
        self.searchfio.setGeometry(QtCore.QRect(860, 40, 111, 22))
        self.searchfio.setObjectName("searchfio")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(860, 20, 221, 16))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(490, 20, 221, 16))
        self.label_8.setObjectName("label_8")
        self.delcod = QtWidgets.QLineEdit(self.centralwidget)
        self.delcod.setGeometry(QtCore.QRect(490, 40, 111, 22))
        self.delcod.setObjectName("delcod")
        self.dell = QtWidgets.QPushButton(self.centralwidget)
        self.dell.setGeometry(QtCore.QRect(490, 70, 93, 28))
        self.dell.setObjectName("del")
        self.table_search = QtWidgets.QTableWidget(self.centralwidget)
        self.table_search.setGeometry(QtCore.QRect(20, 300, 1061, 591))
        self.table_search.setObjectName("table_search")
        self.table_search.setColumnCount(0)
        self.table_search.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.newfile = QtWidgets.QAction(MainWindow)
        self.newfile.setObjectName("newfile")
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.saveas = QtWidgets.QAction(MainWindow)
        self.saveas.setObjectName("saveas")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.menu.addAction(self.newfile)
        self.menu.addAction(self.open)
        self.menu.addAction(self.save)
        self.menu.addAction(self.saveas)
        self.menu.addAction(self.exit)
        self.menu_2.addAction(self.about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.table_search.clear()



        self.table_search.setColumnCount(len(labels))
        self.table_search.setColumnWidth(0, 150) 
        self.table_search.setColumnWidth(1, 150) 
        self.table_search.setColumnWidth(2, 150) 
        self.table_search.setColumnWidth(3, 150) 
        self.table_search.setColumnWidth(4, 150) 
        self.table_search.setColumnWidth(5, 150) 
        self.table_search.setColumnWidth(6, 157) 
        self.table_search.setHorizontalHeaderLabels(labels)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.add_btn.clicked.connect(lambda: self.add_animal())
        self.dell.clicked.connect(lambda: self.dell_animal())
        self.showall.clicked.connect(lambda: self.show_all())
        self.search.clicked.connect(lambda: self.search_animal())
        self.saveas.triggered.connect(lambda: self.save_as_file())
        self.save.triggered.connect(lambda: self.save_file())
        self.open.triggered.connect(lambda: self.download_file())
        self.newfile.triggered.connect(lambda: self.new_file())
        self.exit.triggered.connect(lambda: self.exit_prog())
        self.about.triggered.connect(lambda: self.about_me())
     
    def about_me(self):
        msg2 = QMessageBox()
        msg2.setText("Погосян Жора, 92ПГ")
        msg2.setWindowTitle("О программе")
        msg2.exec_()


    def exit_prog(self):
        msg2 = QMessageBox()
        msg2.setText("Вы дейстельно хотите выйти?")
        msg2.setWindowTitle("Выход")
        DaBtn2 = msg2.addButton('Да', QMessageBox.ActionRole)
        NetBtn2 = msg2.addButton('Нет', QMessageBox.ActionRole)
        msg2.exec_()
        if msg2.clickedButton() == DaBtn2:
            msg = QMessageBox()
            msg.setText("Сохранить данные?")
            msg.setWindowTitle("Сохранение")
            DaBtn = msg.addButton('Да', QMessageBox.ActionRole)
            NetBtn = msg.addButton('Нет', QMessageBox.ActionRole)
            msg.exec_()
            if msg.clickedButton() == DaBtn:
                if len(self.file_name) > 0:
                    self.save_file()
                else:
                    self.save_as_file()
            MainWindow.close()

        
        



    def new_file(self):
        msg = QMessageBox()
        msg.setText("Сохранить изменения?")
        msg.setWindowTitle("Сохранение")
        DaBtn = msg.addButton('Да', QMessageBox.ActionRole)
        NetBtn = msg.addButton('Нет', QMessageBox.ActionRole)
        msg.exec_()
        if msg.clickedButton() == DaBtn:
            if len(self.file_name) > 0:
                self.save_file()
            else:
                self.save_as_file()

        self.file_name = ""
        animals.clear()
        self.table_search.clear()
        self.table_search.setHorizontalHeaderLabels(labels)
        self.table_search.setRowCount(0) 




    def download_file(self):
        msg = QMessageBox()
        msg.setText("Сохранить изменения?")
        msg.setWindowTitle("Сохранение")
        DaBtn = msg.addButton('Да', QMessageBox.ActionRole)
        NetBtn = msg.addButton('Нет', QMessageBox.ActionRole)
        msg.exec_()
        if msg.clickedButton() == DaBtn:
            if len(self.file_name) > 0:
                self.save_file()
            else:
                self.save_as_file()

        animals.clear()
        self.file_name = QFileDialog.getOpenFileName(None, "Сохранение картинки", None, "Text files (*.txt)")[0]
        self.file_name1 = self.file_name
        with open(self.file_name, "r", encoding='utf-8') as f:
            f.seek(0)
            for line in f:
                info = line.split()
                animals.append(Animal(
                    animal_code=info[0].replace("_", " "),
                    animal_vid=info[1].replace("_", " "),
                    klichka=info[2].replace("_", " "),
                    okras=info[3].replace("_", " "),
                    data_birthday=info[3].replace("_", " "),
                    FIO=info[5].replace("_", " "),
                    telefon=info[6].replace("_", " "))
                )
        self.table_search.clear()
        self.table_search.setHorizontalHeaderLabels(labels)
        self.table_search.setRowCount(0) 
        for j in range(0, len(animals)):     
            row = self.table_search.rowCount()
            self.table_search.insertRow(row) 
            self.table_search.setItem(row,0,QtWidgets.QTableWidgetItem(animals[j].animal_code))
            self.table_search.setItem(row,1,QtWidgets.QTableWidgetItem(animals[j].animal_vid))
            self.table_search.setItem(row,2,QtWidgets.QTableWidgetItem(animals[j].klichka))
            self.table_search.setItem(row,3,QtWidgets.QTableWidgetItem(animals[j].okras))
            self.table_search.setItem(row,4,QtWidgets.QTableWidgetItem(animals[j].data_birthday))
            self.table_search.setItem(row,5,QtWidgets.QTableWidgetItem(animals[j].FIO))
            self.table_search.setItem(row,6,QtWidgets.QTableWidgetItem(animals[j].telefon))
               
        

    def save_file(self):
        if self.file_name1 != "":
            with open(self.file_name, "w", encoding='utf-8') as f:
                f.seek(0)
                for item in animals:
                    f.write(item.saved())
        else:
            self.save_as_file()

        

    def save_as_file(self):
            self.file_name = QFileDialog.getSaveFileName(None, "Сохранение картинки", None, "Text files (*.txt)")[0]
            self.file_name1 = self.file_name
            if self.file_name:
                self.save_file()

    def search_animal(self):
        self.table_search.clear()
        self.table_search.setHorizontalHeaderLabels(labels)
        self.table_search.setRowCount(0) 
        searchfio = self.searchfio.text()
        for i in range(0, len(animals)):
            if animals[i].FIO == searchfio:
                row = self.table_search.rowCount()
                self.table_search.insertRow(row) 
                self.table_search.setItem(row,0,QtWidgets.QTableWidgetItem(animals[i].animal_code))
                self.table_search.setItem(row,1,QtWidgets.QTableWidgetItem(animals[i].animal_vid))
                self.table_search.setItem(row,2,QtWidgets.QTableWidgetItem(animals[i].klichka))
                self.table_search.setItem(row,3,QtWidgets.QTableWidgetItem(animals[i].okras))
                self.table_search.setItem(row,4,QtWidgets.QTableWidgetItem(animals[i].data_birthday))
                self.table_search.setItem(row,5,QtWidgets.QTableWidgetItem(animals[i].FIO))
                self.table_search.setItem(row,6,QtWidgets.QTableWidgetItem(animals[i].telefon))


    def show_all(self):
        self.table_search.clear()
        self.table_search.setHorizontalHeaderLabels(labels)
        self.table_search.setRowCount(0) 
        for j in range(0, len(animals)):     
            row = self.table_search.rowCount()
            self.table_search.insertRow(row) 
            self.table_search.setItem(row,0,QtWidgets.QTableWidgetItem(animals[j].animal_code))
            self.table_search.setItem(row,1,QtWidgets.QTableWidgetItem(animals[j].animal_vid))
            self.table_search.setItem(row,2,QtWidgets.QTableWidgetItem(animals[j].klichka))
            self.table_search.setItem(row,3,QtWidgets.QTableWidgetItem(animals[j].okras))
            self.table_search.setItem(row,4,QtWidgets.QTableWidgetItem(animals[j].data_birthday))
            self.table_search.setItem(row,5,QtWidgets.QTableWidgetItem(animals[j].FIO))
            self.table_search.setItem(row,6,QtWidgets.QTableWidgetItem(animals[j].telefon))


    def dell_animal(self):
        delcod = self.delcod.text()
        for i in range(0, len(animals)):
            if animals[i].animal_code == delcod:
                animals.pop(i)
                break
        self.table_search.clear()
        self.table_search.setHorizontalHeaderLabels(labels)
        self.table_search.setRowCount(0) 
        for j in range(0, len(animals)):     
            row = self.table_search.rowCount()
            self.table_search.insertRow(row) 
            self.table_search.setItem(row,0,QtWidgets.QTableWidgetItem(animals[j].animal_code))
            self.table_search.setItem(row,1,QtWidgets.QTableWidgetItem(animals[j].animal_vid))
            self.table_search.setItem(row,2,QtWidgets.QTableWidgetItem(animals[j].klichka))
            self.table_search.setItem(row,3,QtWidgets.QTableWidgetItem(animals[j].okras))
            self.table_search.setItem(row,4,QtWidgets.QTableWidgetItem(animals[j].data_birthday))
            self.table_search.setItem(row,5,QtWidgets.QTableWidgetItem(animals[j].FIO))
            self.table_search.setItem(row,6,QtWidgets.QTableWidgetItem(animals[j].telefon))


    def add_animal(self):
            if self.checkBox.isChecked()==True:
                 animal_code = self.code.text()
                 for j in range(0, len(animals)):
                     if animals[j].animal_code == animal_code:
                         msg = QMessageBox()
                         msg.setIcon(QMessageBox.Critical)
                         msg.setText("Животное с таким кодом уже существует")
                         msg.setWindowTitle("Пустые поля")
                         msg.exec_()
                         return
                 animal_vid = self.vid.text()
                 klichka = self.klichka.text()
                 okras = self.comboBox.currentText()
                 data_birthday = self.dateof.text()
                 FIO = self.fioxoz.text()
                 telefon = self.telxoz.text()
            else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Вы не подтвердили добавление")
                    msg.setWindowTitle("Ошибка")
                    msg.exec_()
                    return

            if len(animal_code) == 0 or len(animal_vid) == 0 or len(klichka) == 0 or len(okras) == 0 or len(data_birthday) == 0 or len(FIO) == 0 or len(telefon) == 0: 
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Вы не заполнили все поля")
                    msg.setWindowTitle("Пустые поля")
                    msg.exec_()
                    return

            animals.append(Animal(
                animal_code = animal_code,
                animal_vid = animal_vid,
                klichka = klichka,
                okras = okras,
                data_birthday = data_birthday,
                FIO = FIO,
                telefon = telefon)
             )
            self.table_search.clear()
            self.table_search.setHorizontalHeaderLabels(labels)
            self.table_search.setRowCount(0) 
            for j in range(0, len(animals)):  
                row = self.table_search.rowCount()
                self.table_search.insertRow(row) 
                self.table_search.setItem(row,0,QtWidgets.QTableWidgetItem(animals[j].animal_code))
                self.table_search.setItem(row,1,QtWidgets.QTableWidgetItem(animals[j].animal_vid))
                self.table_search.setItem(row,2,QtWidgets.QTableWidgetItem(animals[j].klichka))
                self.table_search.setItem(row,3,QtWidgets.QTableWidgetItem(animals[j].okras))
                self.table_search.setItem(row,4,QtWidgets.QTableWidgetItem(animals[j].data_birthday))
                self.table_search.setItem(row,5,QtWidgets.QTableWidgetItem(animals[j].FIO))
                self.table_search.setItem(row,6,QtWidgets.QTableWidgetItem(animals[j].telefon))

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showall.setText(_translate("MainWindow", "Отобразить всё"))
        self.label.setText(_translate("MainWindow", "Введите код животного:"))
        self.label_7.setText(_translate("MainWindow", "Введите телефон хозяина:"))
        self.label_2.setText(_translate("MainWindow", "Введите вид животного:"))
        self.label_6.setText(_translate("MainWindow", "Введите ФИО хозяина:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Бурый"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Светлый"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Черный"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Серый"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Рыжий"))
        self.add_btn.setText(_translate("MainWindow", "Добавить"))
        self.label_4.setText(_translate("MainWindow", "Выберите окрас животного:"))
        self.label_3.setText(_translate("MainWindow", "Введите кличку животного:"))
        self.checkBox.setText(_translate("MainWindow", "Подтверждение "))
        self.label_5.setText(_translate("MainWindow", "Введите дату рождения:"))
        self.search.setText(_translate("MainWindow", "Поиск"))
        self.label_9.setText(_translate("MainWindow", "Введите ФИО хозяина:"))
        self.label_8.setText(_translate("MainWindow", "Введите код удаляемого животного:"))
        self.dell.setText(_translate("MainWindow", "Удалить"))
        self.about.setText(_translate("MainWindow", "О программе"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.newfile.setText(_translate("MainWindow", "Создать"))
        self.open.setText(_translate("MainWindow", "Открыть"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.saveas.setText(_translate("MainWindow", "Сохранить как"))
        self.exit.setText(_translate("MainWindow", "Выход"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
