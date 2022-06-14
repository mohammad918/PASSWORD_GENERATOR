from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from welcome import Ui_welcome
from signup import Ui_signup
from signin import Ui_signin
from account import Ui_home
from setting import Ui_setting
from aboutalan import Ui_aboutalan
from GEN import Ui_generator
from PyQt5 import QtCore
import sqlite3
import random
import pyperclip as pc
import re
from plyer import notification
from webbrowser import open
connection = sqlite3.connect('../password_generator.db')
C = connection.cursor()
C.execute('''CREATE TABLE IF NOT EXISTS logsign(username TEXT NOT NULL UNIQUE,
             email TEXT NOT NULL UNIQUE,
             password TEXT NOT NULL)''')
connection.commit()



Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', '?', '*']
ambiguous=['{', '}', '[', ']', '(',  ')', '/', '\', ',';', ':', '.', '<', '>']
output=[]
dic={"username":"NULL", "email":"NULL", "password":"NULL"}
class forGen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.GEN=Ui_generator()
        self.GEN.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.GEN.pushButton.clicked.connect(self.final)
        self.GEN.pushButton_4.clicked.connect(self.home)
        self.GEN.pushButton_3.clicked.connect(self.setting)
        self.GEN.pushButton_2.clicked.connect(self.about)
        self.GEN.copy.clicked.connect(self.copy)
        self.GEN.checkBox_3.stateChanged.connect(self.num)
        self.GEN.checkBox_4.stateChanged.connect(self.symbol)
        self.GEN.checkBox.stateChanged.connect(self.upper)
        self.GEN.checkBox_2.stateChanged.connect(self.lower)
        self.GEN.checkBox_5.stateChanged.connect(self.ambig)
        self.show()

    def copy(self):
        text=self.GEN.label_6.text()
        pc.copy(text)
        text2=pc.paste()

    def setting(self):
        self.setting=forsetting()
        self.setting.show()
        self.close()

    def about(self):
        self.about=forabout()
        self.about.show()
        self.close()

    def home(self):
        self.home=forhome()
        self.home.show()
        self.close()

    def mousePressEvent(self, evt):
        self.oldPos=evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta=QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos=evt.globalPos()

    def num(self, state):
        if state == QtCore.Qt.Checked :
            output.extend(Numbers)

    def symbol(self, state):
        if state == QtCore.Qt.Checked:
            output.extend(SYMBOLS)

    def upper(self, state):
        if state == QtCore.Qt.Checked:
            output.extend(UPCASE_CHARACTERS)

    def lower(self, state):
        if state == QtCore.Qt.Checked:
            output.extend(LOCASE_CHARACTERS)

    def ambig(self, state):
        if state == QtCore.Qt.Checked:
            output.extend(ambiguous)

    def final(self):
        ultimate=''.join(random.sample(output, int(self.GEN.spinBox.text())))
        self.GEN.label_6.setText('                                                                     ')
        self.GEN.label_6.setText(ultimate)

class forabout(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.about=Ui_aboutalan()
        self.about.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.about.setting.clicked.connect(self.setting)
        self.about.account.clicked.connect(self.home)
        self.about.generation.clicked.connect(self.generator)
        self.about.Github.clicked.connect(self.Github)
        self.about.Email.clicked.connect(self.Email)
        self.about.Social.clicked.connect(self.Social)
        self.show()

    def mousePressEvent(self, evt):
        self.oldPos=evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta=QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos=evt.globalPos()

    def setting(self):
        self.setting=forsetting()
        self.setting.show()
        self.close()

    def home(self):
        self.home=forhome()
        self.home.show()
        self.close()

    def generator(self):
        self.generator=forGen()
        self.generator.show()
        self.close()

    def Github(self):
        open("https://github.com/mohammad918")
    def Email(self):
        open("mailto:?to=matttavakoli@gmail.com&subject='Hi there'", new=1)
    def Social(self):
        open("https://zil.ink/MMTavakoli")
class forsetting(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setting=Ui_setting()
        self.setting.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setting.pushButton.clicked.connect(self.Picture)
        self.setting.pushButton_3.clicked.connect(self.home)
        self.setting.pushButton_4.clicked.connect(self.generator)
        self.setting.pushButton_5.clicked.connect(self.about)
        self.setting.pushButton_2.clicked.connect(self.edit)
        self.setting.label_7.setText(dic["username"])
        self.setting.label_8.setText(dic["email"])
        self.setting.label_9.setText(dic["password"])
        self.show()
        
    def mousePressEvent(self, evt):
        self.oldPos=evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta=QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos=evt.globalPos()

    def Picture(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
        if not filename:
            return
        self.setting.pushButton.setIcon(QIcon(filename))

    def home(self):
        self.home=forhome()
        self.home.show()
        self.close()

    def generator(self):
        self.generator=forGen()
        self.generator.show()
        self.close()

    def about(self):
        self.about=forabout()
        self.about.show()
        self.close()

    def edit(self):
        Username=self.setting.lineEdit.text()
        Email=self.setting.lineEdit_2.text()
        Password=self.setting.lineEdit_3.text()
        regex = r"""^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"""
        RESULT = re.search(regex, Email)

        if (len(Username) and len(Password) >= 5) and RESULT is not None:
            statement="UPDATE logsign SET username=?, email=?, password=? WHERE username= ?"
            data_tuple=(Username, Email, Password, dic["username"])
            C.execute(statement, data_tuple)
            connection.commit()
            dic["username"]=Username
            dic["email"]=Email
            dic["password"]=Password
            notification.notify(
                title='DONE',
                message="the information successfully restored",
                app_name="Password Generator",
                app_icon=None)

            self.setting.label_7.setText(dic["username"])
            self.setting.label_8.setText(dic["email"])
            self.setting.label_9.setText(dic["password"])

        else:
            notification.notify(
                title='Error',
                message="please fill out all fields correctly and make sure you haven't entered "
                        "your Email before.the maximum length of words is 5",
                app_name="Password Generator",
                app_icon=None)


class forhome(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.home=Ui_home()
        self.home.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.home.setting.clicked.connect(self.setting)
        self.home.aboutus.clicked.connect(self.about)
        self.home.generation.clicked.connect(self.generator)
        self.show()

    def mousePressEvent(self, evt):
        self.oldPos=evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta=QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos=evt.globalPos()

    def setting(self):
        self.setting=forsetting()
        self.setting.show()
        self.close()

    def about(self):
        self.about=forabout()
        self.about.show()
        self.close()

    def generator(self):
        self.generator=forGen()
        self.generator.show()
        self.close()

class forsignin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.signin=Ui_signin()
        self.signin.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.signin.back.clicked.connect(self.back)
        self.signin.signinbutton.clicked.connect(self.already)
        self.signin.newaccount.clicked.connect(self.signup)
        self.show()

    def mousePressEvent(self, evt):
        self.oldPos=evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta=QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos=evt.globalPos()

    def back(self):
        self.back=forwelcome()
        self.back.show()
        self.close()

    def signup(self):
        self.signup=forsignup()
        self.signup.show()
        self.close()

    def already(self):
        Username=str(self.signin.lineEdit.text())
        Password=str(self.signin.lineEdit_3.text())
        statement="SELECT username, email, password FROM logsign"
        C.execute(statement)

        for U, E, P in C.fetchall():
            if (Username==U or E) and (Password==P):
                self.home = forhome()
                self.home.show()
                self.close()
                dic["username"]=U
                dic["email"]=E
                dic["password"]=P

        if dic["username"] and dic["email"] and dic["password"] == "NULL":
            notification.notify(
            title='Error',
            message="please fill out all fields correctly",
            app_name="Password Generator",
            app_icon=None)


class forsignup(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.signup=Ui_signup()
        self.signup.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.signup.back.clicked.connect(self.back)
        self.signup.signin.clicked.connect(self.signin)
        self.signup.pushButton.clicked.connect(self.saver)
        self.show()

    def mousePressEvent(self, evt):
        self.oldPos=evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta=QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos=evt.globalPos()

    def back(self):
        self.back=forwelcome()
        self.back.show()
        self.close()

    def signin(self):
        self.signin=forsignin()
        self.signin.show()
        self.close()

    def saver(self):
        Username=str(self.signup.lineEdit_2.text())
        Email=str(self.signup.lineEdit_3.text())
        Password=str(self.signup.lineEdit.text())
        regex = r"""^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"""
        RESULT = re.search(regex, Email)

        if (len(Username) and len(Password) >= 5) and RESULT is not None:
            statement = """INSERT INTO logsign(username, email, password) VALUES(?, ?, ?)"""
            data_tuple = (Username, Email, Password)
            C.execute(statement, data_tuple)
            connection.commit()
            self.signin=forsignin()
            self.signin.show()
            self.close()
            notification.notify(
                title='Done!',
                message="congratulations your account has been created",
                app_name="Password Generator",
                app_icon=None)

        else:
            notification.notify(
                title='Error',
                message="please fill out all fields correctly and make sure you haven't entered "
                        "your Email before.the maximum length of words is 5",
                app_name="Password Generator",
                app_icon=None)


class forwelcome(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.welcome=Ui_welcome()
        self.welcome.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.welcome.signup.clicked.connect(self.signup)
        self.welcome.signin.clicked.connect(self.signin)
        self.show()

    def mousePressEvent(self, evt):
        self.oldPos=evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta=QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos=evt.globalPos()

    def signup(self):
        self.signup=forsignup()
        self.signup.show()
        self.close()

    def signin(self):
        self.signin=forsignin()
        self.signin.show()
        self.close()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    Root=forwelcome()
    sys.exit(app.exec_())

