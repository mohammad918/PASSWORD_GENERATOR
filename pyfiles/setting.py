# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/HADIRAYANEH/PASSWORD_GENERATOR/UI/setting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setting(object):
    def setupUi(self, setting):
        setting.setObjectName("setting")
        setting.resize(1127, 865)
        self.centralwidget = QtWidgets.QWidget(setting)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 1121, 831))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.frame.setFont(font)
        self.frame.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(0, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(200, 110, 411, 661))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(100, 0, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Raleway SemiBold")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(120, 70, 171, 151))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton.setStyleSheet("border-radius:15px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/icons8-picture-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(200, 200))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 240, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setToolTip("")
        self.lineEdit.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 310, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: #c2c2c2;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 380, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(194, 194, 194);\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 530, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Raleway Black")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(630, 330, 471, 421))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../Pictures/Usability testing-bro.svg"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(-1, -1, 1131, 81))
        self.frame_3.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.min = QtWidgets.QPushButton(self.frame_3)
        self.min.setGeometry(QtCore.QRect(1040, 10, 31, 28))
        self.min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"border-radius:8px;")
        self.min.setText("")
        self.min.setObjectName("min")
        self.close = QtWidgets.QPushButton(self.frame_3)
        self.close.setGeometry(QtCore.QRect(1080, 10, 31, 28))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:8px;")
        self.close.setText("")
        self.close.setObjectName("close")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../Pictures/icons8-setting-64.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(70, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(0, 70, 181, 771))
        self.frame_4.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 100, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setToolTip("")
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0;")
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setToolTip("")
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0;")
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 190, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setToolTip("")
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0;")
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(0, 730, 131, 20))
        self.label_12.setStyleSheet("background-color: rgb(112, 112, 167)")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(0, 700, 101, 20))
        self.label_13.setStyleSheet("background-color: rgb(112, 112, 167)")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(0, 670, 51, 20))
        self.label_14.setStyleSheet("background-color: rgb(112, 112, 167)")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(590, 110, 521, 171))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(200, 10, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(210, 60, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setGeometry(QtCore.QRect(250, 110, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        setting.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(setting)
        self.statusbar.setObjectName("statusbar")
        setting.setStatusBar(self.statusbar)

        self.retranslateUi(setting)
        self.close.clicked.connect(setting.close)
        self.min.clicked.connect(setting.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "MainWindow"))
        self.label.setText(_translate("setting", "my profile"))
        self.lineEdit.setPlaceholderText(_translate("setting", "type your new Username"))
        self.lineEdit_2.setPlaceholderText(_translate("setting", "type new E-mail address"))
        self.lineEdit_3.setPlaceholderText(_translate("setting", "type your new Password"))
        self.pushButton_2.setText(_translate("setting", "Edit"))
        self.min.setToolTip(_translate("setting", "minimize"))
        self.close.setToolTip(_translate("setting", "close"))
        self.label_11.setText(_translate("setting", "Setting"))
        self.pushButton_4.setText(_translate("setting", "Generator"))
        self.pushButton_3.setText(_translate("setting", "Home"))
        self.pushButton_5.setText(_translate("setting", "About Alan"))
        self.label_3.setText(_translate("setting", "current Name:"))
        self.label_5.setText(_translate("setting", "current E-mail:"))
        self.label_6.setText(_translate("setting", "current Password:"))
        self.label_7.setText(_translate("setting", "srthryhtestynj"))
        self.label_8.setText(_translate("setting", "rbsrtshsrhtrhb"))
        self.label_9.setText(_translate("setting", "sdffverkengkn23442534"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setting = QtWidgets.QMainWindow()
    ui = Ui_setting()
    ui.setupUi(setting)
    setting.show()
    sys.exit(app.exec_())

