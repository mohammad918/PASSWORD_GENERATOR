# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/HADIRAYANEH/PASSWORD_GENERATOR/UI/aboutalan.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutalan(object):
    def setupUi(self, aboutalan):
        aboutalan.setObjectName("aboutalan")
        aboutalan.resize(1123, 863)
        self.centralwidget = QtWidgets.QWidget(aboutalan)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 1121, 841))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(610, 340, 501, 411))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Pictures/GDPR-pana.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(250, 110, 771, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(85, 0, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 370, 55, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../Downloads/icons8-instagram-48.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1131, 81))
        self.frame_2.setStyleSheet("\n"
"background-color: rgb(0, 85, 127);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.minimize = QtWidgets.QPushButton(self.frame_2)
        self.minimize.setGeometry(QtCore.QRect(1040, 10, 31, 28))
        self.minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"border-radius:8px;")
        self.minimize.setText("")
        self.minimize.setObjectName("minimize")
        self.close = QtWidgets.QPushButton(self.frame_2)
        self.close.setGeometry(QtCore.QRect(1080, 10, 31, 28))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:8px;")
        self.close.setText("")
        self.close.setObjectName("close")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../Pictures/icons8-about-480.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(70, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(-1, 70, 181, 781))
        self.frame_3.setStyleSheet("\n"
"background-color: rgb(0, 85, 127);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.account = QtWidgets.QPushButton(self.frame_3)
        self.account.setGeometry(QtCore.QRect(0, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.account.setFont(font)
        self.account.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.account.setToolTip("")
        self.account.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/icons8-account-48 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account.setIcon(icon)
        self.account.setIconSize(QtCore.QSize(50, 50))
        self.account.setObjectName("account")
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
"border-radius:0px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Downloads/icons8-setting-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon1)
        self.setting.setIconSize(QtCore.QSize(50, 50))
        self.setting.setObjectName("setting")
        self.generation = QtWidgets.QPushButton(self.frame_3)
        self.generation.setGeometry(QtCore.QRect(0, 190, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(17)
        self.generation.setFont(font)
        self.generation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generation.setToolTip("")
        self.generation.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0px;")
        self.generation.setIconSize(QtCore.QSize(50, 50))
        self.generation.setObjectName("generation")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(0, 740, 131, 20))
        self.label_6.setStyleSheet("background-color: rgb(112, 112, 167)")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(0, 710, 101, 20))
        self.label_7.setStyleSheet("background-color: rgb(112, 112, 167)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(0, 680, 51, 20))
        self.label_8.setStyleSheet("background-color: rgb(112, 112, 167)")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(200, 270, 411, 521))
        self.frame_4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 440, 411, 81))
        self.frame_5.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.Email = QtWidgets.QPushButton(self.frame_5)
        self.Email.setGeometry(QtCore.QRect(150, 10, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(13)
        self.Email.setFont(font)
        self.Email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Email.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.Email.setObjectName("Email")
        self.Social = QtWidgets.QPushButton(self.frame_5)
        self.Social.setGeometry(QtCore.QRect(290, 10, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.Social.setFont(font)
        self.Social.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Social.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 255);\n"
"")
        self.Social.setObjectName("Social")
        self.Github = QtWidgets.QPushButton(self.frame_5)
        self.Github.setGeometry(QtCore.QRect(10, 10, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(13)
        self.Github.setFont(font)
        self.Github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Github.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.Github.setObjectName("Github")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_4)
        self.textBrowser.setGeometry(QtCore.QRect(10, 0, 371, 441))
        self.textBrowser.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 251, 181))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Pictures/icons8-show-password-90.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        aboutalan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(aboutalan)
        self.statusbar.setObjectName("statusbar")
        aboutalan.setStatusBar(self.statusbar)

        self.retranslateUi(aboutalan)
        self.close.clicked.connect(aboutalan.close)
        self.minimize.clicked.connect(aboutalan.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(aboutalan)

    def retranslateUi(self, aboutalan):
        _translate = QtCore.QCoreApplication.translate
        aboutalan.setWindowTitle(_translate("aboutalan", "MainWindow"))
        self.label_2.setText(_translate("aboutalan", "alan is a high-level password generator system"))
        self.minimize.setToolTip(_translate("aboutalan", "minimize"))
        self.close.setToolTip(_translate("aboutalan", "close"))
        self.label_10.setText(_translate("aboutalan", "About Alan"))
        self.account.setText(_translate("aboutalan", "Home"))
        self.setting.setText(_translate("aboutalan", "Setting"))
        self.generation.setText(_translate("aboutalan", "Generator"))
        self.Email.setText(_translate("aboutalan", "Email Me"))
        self.Social.setText(_translate("aboutalan", "Social Media"))
        self.Github.setText(_translate("aboutalan", "Github"))
        self.textBrowser.setHtml(_translate("aboutalan", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">we created alan for you and using alan you can immediately generate Random and Strong Passwords.                   </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">also you can give feedbacks</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">and suggestions via:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutalan = QtWidgets.QMainWindow()
    ui = Ui_aboutalan()
    ui.setupUi(aboutalan)
    aboutalan.show()
    sys.exit(app.exec_())

