import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
from tkinter import filedialog
from BD import Database


labels = [ 'Код Животного', 'Кличка', 'Код Хозяина', 'ФИО хозяина', 'Телефон']

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.db = Database()
        self.db.connect()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 867)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showall = QtWidgets.QPushButton(self.centralwidget)
        self.showall.setGeometry(QtCore.QRect(740, 10, 281, 61))
        self.showall.setObjectName("showall")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 151, 16))
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 130, 161, 16))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 100, 141, 16))
        self.label_6.setObjectName("label_6")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(200, 170, 93, 28))
        self.add.setObjectName("add")
        self.klichka = QtWidgets.QLineEdit(self.centralwidget)
        self.klichka.setGeometry(QtCore.QRect(200, 70, 91, 22))
        self.klichka.setObjectName("klichka")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 181, 16))
        self.label_3.setObjectName("label_3")
        self.code = QtWidgets.QLineEdit(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(180, 40, 111, 22))
        self.code.setObjectName("code")
        self.telxoz = QtWidgets.QLineEdit(self.centralwidget)
        self.telxoz.setGeometry(QtCore.QRect(190, 130, 101, 22))
        self.telxoz.setObjectName("telxoz")
        self.fioxoz = QtWidgets.QLineEdit(self.centralwidget)
        self.fioxoz.setGeometry(QtCore.QRect(170, 100, 121, 22))
        self.fioxoz.setObjectName("fioxoz")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(400, 10, 221, 16))
        self.label_8.setObjectName("label_8")
        self.delcod = QtWidgets.QLineEdit(self.centralwidget)
        self.delcod.setGeometry(QtCore.QRect(400, 30, 111, 22))
        self.delcod.setObjectName("delcod")
        self.dell = QtWidgets.QPushButton(self.centralwidget)
        self.dell.setGeometry(QtCore.QRect(400, 60, 93, 28))
        self.dell.setObjectName("del")
        self.table_search = QtWidgets.QTableWidget(self.centralwidget)
        self.table_search.setGeometry(QtCore.QRect(10, 220, 1061, 591))
        self.table_search.setObjectName("table_search")
        self.table_search.setColumnCount(0)
        self.table_search.setRowCount(0)
        self.Xozcode = QtWidgets.QLineEdit(self.centralwidget)
        self.Xozcode.setGeometry(QtCore.QRect(180, 10, 111, 22))
        self.Xozcode.setObjectName("Xozcode")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 151, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.table_search.clear()



        self.table_search.setColumnCount(len(labels))
        self.table_search.setColumnWidth(0, 210) 
        self.table_search.setColumnWidth(1, 210) 
        self.table_search.setColumnWidth(2, 210) 
        self.table_search.setColumnWidth(3, 210) 
        self.table_search.setColumnWidth(4, 217) 
        self.table_search.setHorizontalHeaderLabels(labels)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.add.clicked.connect(lambda: self.add_animal())
        self.dell.clicked.connect(lambda: self.dell_animal())
        self.showall.clicked.connect(lambda: self.show_all())





    def show_all(self):
        self.table_search.clear()
        self.table_search.setHorizontalHeaderLabels(labels)
        self.table_search.setRowCount(0) 

        for rowsanimalxoz in self.db.get_animalxoz():
            row = self.table_search.rowCount()
            self.table_search.insertRow(row) 
            self.table_search.setItem(row,0,QtWidgets.QTableWidgetItem(rowsanimalxoz[0]))
            self.table_search.setItem(row,1,QtWidgets.QTableWidgetItem(rowsanimalxoz[1]))
            self.table_search.setItem(row,2,QtWidgets.QTableWidgetItem(rowsanimalxoz[2]))
            self.table_search.setItem(row,3,QtWidgets.QTableWidgetItem(rowsanimalxoz[3]))
            self.table_search.setItem(row,4,QtWidgets.QTableWidgetItem(rowsanimalxoz[4]))



    def dell_animal(self):
        animalkeys = []
        delcod = self.delcod.text()

        if len(delcod) == 0: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Вы не заполнили все поля")
            msg.setWindowTitle("Пустые поля")
            msg.exec_()
            return

        for row in self.db.get_animals():
                animalkeys.append(row[0])

        if(delcod in animalkeys): 
            self.db.delete_animal(delcod)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Успешно удалено!")
            msg.setWindowTitle("Информация")
            msg.exec_()
        else: 
            self.db.delete_animal(delcod)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Животного с таким кодом не существует")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return

        self.table_search.clear()
        self.table_search.setHorizontalHeaderLabels(labels)
        self.table_search.setRowCount(0) 

        for rowsanimalxoz in self.db.get_animalxoz():
            row = self.table_search.rowCount()
            self.table_search.insertRow(row) 
            self.table_search.setItem(row,0,QtWidgets.QTableWidgetItem(rowsanimalxoz[0]))
            self.table_search.setItem(row,1,QtWidgets.QTableWidgetItem(rowsanimalxoz[1]))
            self.table_search.setItem(row,2,QtWidgets.QTableWidgetItem(rowsanimalxoz[2]))
            self.table_search.setItem(row,3,QtWidgets.QTableWidgetItem(rowsanimalxoz[3]))
            self.table_search.setItem(row,4,QtWidgets.QTableWidgetItem(rowsanimalxoz[4])) 


    def add_animal(self):
            animalkeys = []
            xozkeys = []
            xoz_code = self.Xozcode.text()
            animal_code = self.code.text()
            klichka = self.klichka.text()
            FIO = self.fioxoz.text()
            telefon = self.telxoz.text()

            if len(xoz_code) == 0 or len(animal_code) == 0 or len(klichka) == 0 or len(FIO) == 0 or len(telefon) == 0: 
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Вы не заполнили все поля")
                    msg.setWindowTitle("Пустые поля")
                    msg.exec_()
                    return

            for row in self.db.get_xoz():
                xozkeys.append(row[0]) 

            for row in self.db.get_animals():
                animalkeys.append(row[0])  

            if(animal_code in animalkeys):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Такой код с животным уже существует")
                    msg.setWindowTitle("Ошибка")
                    msg.exec_()
                    return
            if(xoz_code in xozkeys): 
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Такой Хозяин уже существует.К животному добавлен существуюший хозяин")
                    msg.setWindowTitle("Информация")
                    msg.exec_()
                    self.db.insert_animal(animal_code, klichka, xoz_code)
                    return
            else: 
                self.db.insert_xoz(xoz_code, FIO, telefon)
            self.db.insert_animal(animal_code, klichka, xoz_code)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showall.setText(_translate("MainWindow", "Отобразить всё"))
        self.label.setText(_translate("MainWindow", "Введите код животного:"))
        self.label_7.setText(_translate("MainWindow", "Введите телефон хозяина:"))
        self.label_6.setText(_translate("MainWindow", "Введите ФИО хозяина:"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.label_3.setText(_translate("MainWindow", "Введите кличку животного:"))
        self.label_8.setText(_translate("MainWindow", "Введите код удаляемого животного:"))
        self.dell.setText(_translate("MainWindow", "Удалить")) 
        self.label_2.setText(_translate("MainWindow", "Введите код хозяина:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())