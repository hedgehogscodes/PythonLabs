import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 10, 511, 121))
        self.text.setObjectName("text")
        self.countstr = QtWidgets.QTextEdit(self.centralwidget)
        self.countstr.setGeometry(QtCore.QRect(10, 190, 511, 341))
        self.countstr.setObjectName("countstr")
        self.countstr.setReadOnly(True)
        self.startbtn = QtWidgets.QPushButton(self.centralwidget)
        self.startbtn.setGeometry(QtCore.QRect(190, 150, 93, 28))
        self.startbtn.setObjectName("startbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.startbtn.clicked.connect(lambda: self.get_str())

    def get_str(self):
        self.countstr.clear()
        str = self.text.toPlainText()
        hello = proxy.strcount(str)
        self.countstr.setPlainText(hello)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startbtn.setText(_translate("MainWindow", "Посчитать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
