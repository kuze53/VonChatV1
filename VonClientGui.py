# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\slhkl\desktop\VonChat\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from VonSock import VonClient
import socket
import time
import threading
from datetime import datetime


class Ui_Form(QtWidgets.QMainWindow):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(411, 479)
        Form.setMinimumSize(QtCore.QSize(411, 480))
        Form.setMaximumSize(QtCore.QSize(411, 480))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(90, 90, 90);")
        Form.setWindowIcon(QtGui.QIcon("./main.ico"))
        Form.closeEvent = self.closeEvent
        self.Server_address_label = QtWidgets.QLabel(Form)
        self.Server_address_label.setGeometry(QtCore.QRect(10, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Server_address_label.setFont(font)
        self.Server_address_label.setStyleSheet("color: rgb(255, 255, 127);")
        self.Server_address_label.setObjectName("Server_address_label")
        self.Ip_Input = QtWidgets.QLineEdit(Form)
        self.Ip_Input.setGeometry(QtCore.QRect(120, 20, 161, 20))
        self.Ip_Input.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.Ip_Input.setObjectName("Ip_Input")
        self.chatText_textEdit = QtWidgets.QTextEdit(Form)
        self.chatText_textEdit.setGeometry(QtCore.QRect(10, 80, 271, 241))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.chatText_textEdit.setFont(font)
        self.chatText_textEdit.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.chatText_textEdit.setObjectName("chatText_textEdit")
        self.chatText_textEdit.setReadOnly(True)

        self.Online_user_list_label = QtWidgets.QLabel(Form)
        self.Online_user_list_label.setGeometry(QtCore.QRect(290, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Online_user_list_label.setFont(font)
        self.Online_user_list_label.setStyleSheet("color: rgb(255, 255, 127);")
        self.Online_user_list_label.setObjectName("Online_user_list_label")
        self.userList_textEdit = QtWidgets.QPlainTextEdit(Form)
        self.userList_textEdit.setGeometry(QtCore.QRect(290, 50, 111, 271))
        self.userList_textEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.userList_textEdit.setFont(font)
        self.userList_textEdit.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.userList_textEdit.setObjectName("userList_textEdit")
        self.message_textEdit = QtWidgets.QTextEdit(Form)
        self.message_textEdit.setGeometry(QtCore.QRect(10, 330, 391, 111))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(True)
        font.setWeight(75)
        self.message_textEdit.setFont(font)
        self.message_textEdit.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.message_textEdit.setObjectName("message_textEdit")
        self.message_textEdit.installEventFilter(self)

        self.Connect_button = QtWidgets.QPushButton(Form)
        self.Connect_button.setGeometry(QtCore.QRect(10, 50, 131, 23))
        self.Connect_button.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.Connect_button.setObjectName("Connect_button")
        self.Connect_button.clicked.connect(self.ConnectButton)

        self.Disconnect_button = QtWidgets.QPushButton(Form)
        self.Disconnect_button.setGeometry(QtCore.QRect(150, 50, 131, 23))
        self.Disconnect_button.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.Disconnect_button.setObjectName("Disconnect_button")
        self.Disconnect_button.clicked.connect(self.DisconnectButton)
        self.Disconnect_button.setEnabled(False)

        self.Info_label = QtWidgets.QLabel(Form)
        self.Info_label.setGeometry(QtCore.QRect(100, 450, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Info_label.setFont(font)
        self.Info_label.setStyleSheet("color: rgb(255, 255, 127);")
        self.Info_label.setText("")
        self.Info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Info_label.setObjectName("Info_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "VonChat V1"))
        self.Server_address_label.setText(_translate("Form", "SERVER ADDRESS"))
        self.Online_user_list_label.setText(_translate("Form", "ONLINE USER LIST"))
        self.Connect_button.setText(_translate("Form", "CONNECT TO SERVER"))
        self.Disconnect_button.setText(_translate("Form", "DISCONNECT"))

    # function
    def ListenServer(self):
        while True:
            data = self.MySock.ListenServer(self.MainConnection)

            try:

                if "#331" in data:
                    newData = data.replace("#331", "")
                    newData = newData.replace("[", "")
                    newData = newData.replace("]", "")
                    newData = newData.replace('"', "")
                    newData = newData.replace(',', "")

                    self.userList_textEdit.setPlainText(newData)
                else:
                    self.chatText_textEdit.append(data)
            except:
                break
                self.sock.close()



    def ConnectButton(self):
        self.MySock = VonClient()
        self.sock = self.MySock.CreateSocket(socket.AF_INET, socket.SOCK_STREAM)
        print("sock created")
        try:
            self.MainConnection = self.MySock.ConnectServer(self.sock, self.Ip_Input.text(), 1080)
            threading._start_new_thread(self.ListenServer, ())
            self.Connect_button.setEnabled(False)
            self.Disconnect_button.setEnabled(True)
        except:
            self.Info_label.setText("Connection Failed")

        print("Connection Succesfull")
    def DisconnectButton(self):

        self.sock.close()
        self.Connect_button.setEnabled(True)
        self.Disconnect_button.setEnabled(False)
        self.userList_textEdit.clear()
        self.chatText_textEdit.clear()

    def closeEvent(self, event):
        try:
            self.sock.close()
        except:
            pass


    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Return:
                text2 = datetime.now().strftime('%H:%M:%S')
                text2 += " | " + self.message_textEdit.toPlainText()

                if len(text2) > 120:
                    self.Info_label.setText("Maximum Character Length 120")
                else:
                    try:
                        self.MySock.SendMessage(self.sock, text2)
                        time.sleep(0.1)
                    except:
                        self.chatText_textEdit.clear()
                        self.userList_textEdit.clear()
                        self.sock.close()
                        self.Info_label.setText("Sending failed sv may be off")
                        self.Connect_button.setEnabled(True)
                        self.Disconnect_button.setEnabled(False)
        if event.type() == QtCore.QEvent.KeyRelease:
            if event.key() == QtCore.Qt.Key_Return:
                self.message_textEdit.clear()

        return False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
