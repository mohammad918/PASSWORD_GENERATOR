# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/HADIRAYANEH/PASSWORD_GENERATOR/UI/account.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(1121, 865)
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 1121, 831))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 1141, 81))
        self.frame_2.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.close = QtWidgets.QPushButton(self.frame_2)
        self.close.setGeometry(QtCore.QRect(1080, 10, 31, 28))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:8px;")
        self.close.setText("")
        self.close.setObjectName("close")
        self.min = QtWidgets.QPushButton(self.frame_2)
        self.min.setGeometry(QtCore.QRect(1040, 10, 31, 28))
        self.min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"border-radius:8px;")
        self.min.setText("")
        self.min.setObjectName("min")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../Pictures/icons8-home-500.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(70, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(-1, 70, 181, 771))
        self.frame_3.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.generation = QtWidgets.QPushButton(self.frame_3)
        self.generation.setGeometry(QtCore.QRect(0, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.generation.setFont(font)
        self.generation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generation.setToolTip("")
        self.generation.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0;")
        self.generation.setIconSize(QtCore.QSize(50, 50))
        self.generation.setObjectName("generation")
        self.aboutus = QtWidgets.QPushButton(self.frame_3)
        self.aboutus.setEnabled(True)
        self.aboutus.setGeometry(QtCore.QRect(0, 190, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.aboutus.setFont(font)
        self.aboutus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutus.setMouseTracking(False)
        self.aboutus.setTabletTracking(False)
        self.aboutus.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.aboutus.setAcceptDrops(False)
        self.aboutus.setToolTip("")
        self.aboutus.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/icons8-contact-us-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutus.setIcon(icon)
        self.aboutus.setIconSize(QtCore.QSize(50, 50))
        self.aboutus.setObjectName("aboutus")
        self.setting = QtWidgets.QPushButton(self.frame_3)
        self.setting.setGeometry(QtCore.QRect(0, 100, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.setting.setFont(font)
        self.setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setting.setToolTip("")
        self.setting.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Downloads/icons8-setting-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon1)
        self.setting.setIconSize(QtCore.QSize(50, 50))
        self.setting.setObjectName("setting")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(0, 670, 51, 20))
        self.label_3.setStyleSheet("background-color: rgb(112, 112, 167)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(0, 700, 101, 20))
        self.label_4.setStyleSheet("background-color: rgb(112, 112, 167)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(0, 730, 131, 20))
        self.label_5.setStyleSheet("background-color: rgb(112, 112, 167)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 90, 881, 581))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Pictures/Two factor authentication-bro.svg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(230, 680, 821, 101))
        font = QtGui.QFont()
        font.setFamily("Raleway Medium")
        font.setPointSize(35)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        home.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(home)
        self.statusbar.setObjectName("statusbar")
        home.setStatusBar(self.statusbar)

        self.retranslateUi(home)
        self.close.clicked.connect(home.close)
        self.min.clicked.connect(home.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "MainWindow"))
        self.close.setToolTip(_translate("home", "close"))
        self.min.setToolTip(_translate("home", "minimize"))
        self.label_7.setText(_translate("home", "Home"))
        self.generation.setText(_translate("home", "Generator"))
        self.aboutus.setText(_translate("home", "About Alan"))
        self.setting.setText(_translate("home", "Setting"))
        self.label_2.setText(_translate("home", "welcome to your account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())

