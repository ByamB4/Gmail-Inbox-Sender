from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib, sys


class Ui_ComposeWindow(object):
    def __init__(self, cred):
        self.username, self.password = cred[0], cred[1]

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName()[0]

    def sendMail(self):
        print('[+] Trying to send mail')
        self.msg = MIMEMultipart()
        self.msg['From'] = self.username
        self.msg['Subject'] = self.inp2Subject.text()
        self.body = self.inp3Body.toPlainText()
        self.msg.attach(MIMEText(self.body, 'plain'))
        try:
            if self.filename != '':
                self.attachment = open(self.filename, 'rb')
                self.part = MIMEBase('application','octet-stream')
                self.part.set_payload((self.attachment).read())
                encoders.encode_base64(self.part)
                self.part.add_header('Content-Disposition',"attachment; filename= " + self.filename)
                self.msg.attach(self.part)
        except:
            print('[-] No file selected')
        self.text = self.msg.as_string()
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        # Trying to login
        try:
            # self.server.login(self.username, self.password)
            self.server.login(self.username, self.password)
            self.email_send = self.inp1Receiver.text()
            print(self.email_send)
            self.server.sendmail(self.username, self.email_send, self.text)
        except Exception as e:
            print(f'[-] Error on login: {e}')
            sys.exit(0)
        print('[+] Successfully sent')

    def setupUi(self, ComposeWindow):
        ComposeWindow.setObjectName("ComposeWindow")
        ComposeWindow.resize(391, 330)
        ComposeWindow.setMinimumSize(QtCore.QSize(391, 330))
        ComposeWindow.setMaximumSize(QtCore.QSize(391, 330))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ComposeWindow.setWindowIcon(icon)
        ComposeWindow.setStyleSheet("* {\n"
"    background-color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ComposeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl1Receiver = QtWidgets.QLabel(self.centralwidget)
        self.lbl1Receiver.setGeometry(QtCore.QRect(20, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.lbl1Receiver.setFont(font)
        self.lbl1Receiver.setObjectName("lbl1Receiver")
        self.lbl2Subject = QtWidgets.QLabel(self.centralwidget)
        self.lbl2Subject.setGeometry(QtCore.QRect(20, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.lbl2Subject.setFont(font)
        self.lbl2Subject.setObjectName("lbl2Subject")
        self.lbl3Body = QtWidgets.QLabel(self.centralwidget)
        self.lbl3Body.setGeometry(QtCore.QRect(20, 100, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.lbl3Body.setFont(font)
        self.lbl3Body.setObjectName("lbl3Body")
        self.inp1Receiver = QtWidgets.QLineEdit(self.centralwidget)
        self.inp1Receiver.setGeometry(QtCore.QRect(150, 20, 221, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inp1Receiver.setFont(font)
        self.inp1Receiver.setStyleSheet("padding-left:7px;")
        self.inp1Receiver.setObjectName("inp1Receiver")
        self.inp2Subject = QtWidgets.QLineEdit(self.centralwidget)
        self.inp2Subject.setGeometry(QtCore.QRect(150, 60, 221, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inp2Subject.setFont(font)
        self.inp2Subject.setStyleSheet("padding-left:7px;")
        self.inp2Subject.setObjectName("inp2Subject")
        self.inp3Body = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inp3Body.setGeometry(QtCore.QRect(150, 100, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inp3Body.setFont(font)
        self.inp3Body.setStyleSheet("padding-left:7px;")
        self.inp3Body.setObjectName("inp3Body")
        self.btn1File = QtWidgets.QPushButton(self.centralwidget)
        self.btn1File.setGeometry(QtCore.QRect(270, 270, 21, 28))
        self.btn1File.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1File.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/attach_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn1File.setIcon(icon1)
        self.btn1File.setIconSize(QtCore.QSize(32, 32))
        self.btn1File.setFlat(True)
        self.btn1File.setObjectName("btn1File")
        self.btn1File.clicked.connect(self.openFile)
        self.btn2Sent = QtWidgets.QPushButton(self.centralwidget)
        self.btn2Sent.setGeometry(QtCore.QRect(300, 270, 61, 31))
        self.btn2Sent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/sent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn2Sent.setIcon(icon2)
        self.btn2Sent.setIconSize(QtCore.QSize(20, 20))
        self.btn2Sent.setFlat(True)
        self.btn2Sent.setObjectName("btn2Sent")
        self.btn2Sent.clicked.connect(self.sendMail)
        ComposeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ComposeWindow)
        self.statusbar.setObjectName("statusbar")
        ComposeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ComposeWindow)
        QtCore.QMetaObject.connectSlotsByName(ComposeWindow)

    def retranslateUi(self, ComposeWindow):
        _translate = QtCore.QCoreApplication.translate
        ComposeWindow.setWindowTitle(_translate("ComposeWindow", "Мэйл илгээх"))
        self.lbl1Receiver.setText(_translate("ComposeWindow", "Хүлээн авагч"))
        self.lbl2Subject.setText(_translate("ComposeWindow", "Сэдэв"))
        self.lbl3Body.setText(_translate("ComposeWindow", "Мэндчилгээ"))
        self.inp1Receiver.setPlaceholderText(_translate("ComposeWindow", "Емэйл оруулна уу"))
        self.inp2Subject.setPlaceholderText(_translate("ComposeWindow", "Сэдвээ оруулна уу"))
        self.inp3Body.setPlaceholderText(_translate("ComposeWindow", "Агуулгаа оруулна уу"))
        self.btn1File.setToolTip(_translate("ComposeWindow", "Файл сонгох"))
        self.btn2Sent.setToolTip(_translate("ComposeWindow", "Илгээх"))
        self.btn2Sent.setText(_translate("ComposeWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ComposeWindow = QtWidgets.QMainWindow()
    ui = Ui_ComposeWindow()
    ui.setupUi(ComposeWindow)
    ComposeWindow.show()
    sys.exit(app.exec_())
