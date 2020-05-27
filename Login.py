from PyQt5 import QtCore, QtGui, QtWidgets
from Inbox import Ui_InboxWindow

# LOCAL CONFIG
DEBUG = True


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(475, 412)
        LoginWindow.setMinimumSize(QtCore.QSize(475, 412))
        LoginWindow.setMaximumSize(QtCore.QSize(475, 412))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("* {\n"
"    background-color: white;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imGoogle = QtWidgets.QLabel(self.centralwidget)
        self.imGoogle.setGeometry(QtCore.QRect(10, 10, 451, 101))
        self.imGoogle.setText("")
        self.imGoogle.setPixmap(QtGui.QPixmap("./img/shutis.png"))
        self.imGoogle.setObjectName("imGoogle")
        self.accountInput = QtWidgets.QLineEdit(self.centralwidget)
        self.accountInput.setGeometry(QtCore.QRect(40, 130, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto,RobotoDraft,Helvetica,Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.accountInput.setFont(font)
        self.accountInput.setStyleSheet("padding-left: 15px;\n"
"font:  400 16px Roboto,RobotoDraft,Helvetica,Arial,sans-serif")
        self.accountInput.setText("")
        self.accountInput.setObjectName("accountInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(60, 120, 41, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font-family: century gothic ;\n"
"color: #80868b;")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(40, 230, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto,RobotoDraft,Helvetica,Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(True)
        self.passwordInput.setFont(font)
        self.passwordInput.setStyleSheet("padding-left: 15px;\n"
"font:  400 16px Roboto,RobotoDraft,Helvetica,Arial,sans-serif")
        self.passwordInput.setObjectName("passwordInput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 61, 16))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-family: century gothic ;\n"
"color: #80868b;")
        self.label_2.setObjectName("label_2")
        self.btnLoginAccount = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoginAccount.setGeometry(QtCore.QRect(349, 330, 101, 28))
        self.btnLoginAccount.clicked.connect(self.loginAccount)

        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnLoginAccount.setFont(font)
        self.btnLoginAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLoginAccount.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 115, 232);")
        self.btnLoginAccount.setObjectName("btnLoginAccount")
        self.btnCreateAccount = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreateAccount.setGeometry(QtCore.QRect(40, 330, 90, 28))
        self.btnCreateAccount.clicked.connect(self.createAccount)

        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setItalic(False)
        self.btnCreateAccount.setFont(font)
        self.btnCreateAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCreateAccount.setStyleSheet("color: rgb(26, 115, 232);")
        self.btnCreateAccount.setFlat(True)
        self.btnCreateAccount.setObjectName("btnCreateAccount")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Мэйл нэвтрэх"))
        self.accountInput.setPlaceholderText(_translate("LoginWindow", "Хэрэглэгчийн нэрээ оруулна уу"))
        self.label.setText(_translate("LoginWindow", "Email"))
        self.passwordInput.setPlaceholderText(_translate("LoginWindow", "Нууц үгээ оруулна уу"))
        self.label_2.setText(_translate("LoginWindow", "Password"))
        self.btnLoginAccount.setToolTip(_translate("LoginWindow", "Үүнийг дарж нэвтэрнэ үү"))
        self.btnLoginAccount.setText(_translate("LoginWindow", "Нэвтрэх"))
        self.btnCreateAccount.setToolTip(_translate("LoginWindow", "Үүнийг дарж шинэ хаяг нээнэ үү"))
        self.btnCreateAccount.setText(_translate("LoginWindow", "Хаяг нээх"))
    def loginAccount(self):
        self.username, self.password = self.accountInput.text(), self.passwordInput.text()
        if DEBUG:
            print('[+] Trying to login')
            print(f'\tUsername: {self.username}')
            print(f'\tPassword: {self.password}')
        import smtplib
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        try:
            self.server.login(self.username, self.password)
        except Exception as e:
            print(f'[-] Can\'t login: {e}')
        else:
            if DEBUG: print('[+] Login successfully')
            self.openInboxWindow()
    def createAccount(self):
        import webbrowser
        if DEBUG: print('[+] Opening new browser')
        try: webbrowser.open('https://accounts.google.com/signup')
        except: print(f'[-] Error on creating browser: {e}')

    def openInboxWindow(self):
        if DEBUG: print('[+] Trying to open mail window')
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InboxWindow([self.username, self.password])
        self.ui.setupUi(self.window)
        LoginWindow.close()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
