# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/HADIRAYANEH/PASSWORD_GENERATOR/UI/welcome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_welcome(object):
    def setupUi(self, welcome):
        welcome.setObjectName("welcome")
        welcome.resize(1107, 861)
        welcome.setMinimumSize(QtCore.QSize(18, 18))
        welcome.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(welcome)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1101, 831))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.signup = QtWidgets.QPushButton(self.frame)
        self.signup.setGeometry(QtCore.QRect(390, 690, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(12)
        self.signup.setFont(font)
        self.signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border-radius:15px;")
        self.signup.setObjectName("signup")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 30, 491, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:888888 ;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(270, 120, 551, 481))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Pictures/Binary code-amico.svg"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setGeometry(QtCore.QRect(1060, 10, 31, 28))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:8px;")
        self.close.setText("")
        self.close.setObjectName("close")
        self.minimize = QtWidgets.QPushButton(self.frame)
        self.minimize.setGeometry(QtCore.QRect(1020, 10, 31, 28))
        self.minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"border-radius:8px;")
        self.minimize.setText("")
        self.minimize.setObjectName("minimize")
        self.signin = QtWidgets.QPushButton(self.frame)
        self.signin.setGeometry(QtCore.QRect(570, 690, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(12)
        self.signin.setFont(font)
        self.signin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signin.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border-radius:15px;")
        self.signin.setObjectName("signin")
        welcome.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(welcome)
        self.statusbar.setObjectName("statusbar")
        welcome.setStatusBar(self.statusbar)

        self.retranslateUi(welcome)
        self.close.clicked.connect(welcome.close)
        self.minimize.clicked.connect(welcome.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        _translate = QtCore.QCoreApplication.translate
        welcome.setWindowTitle(_translate("welcome", "MainWindow"))
        self.signup.setText(_translate("welcome", "SIGN UP"))
        self.label.setText(_translate("welcome", "welcome to alan"))
        self.close.setToolTip(_translate("welcome", "close"))
        self.minimize.setToolTip(_translate("welcome", "minimize"))
        self.signin.setText(_translate("welcome", "SIGN IN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome = QtWidgets.QMainWindow()
    ui = Ui_welcome()
    ui.setupUi(welcome)
    welcome.show()
    sys.exit(app.exec_())

