import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QLabel
import socket
import mysocket
import threading

HOST = "127.0.0.1"
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

class SignUp(QWidget):
    def signUpUi(self):
        self.setGeometry(300, 100, 350, 550)
        self.setWindowTitle('Sign Up')

        self.inputNm = QLineEdit(self)
        self.inputNm.move(20, 220)
        self.inputNm.resize(200, 20)

        self.inputID = QLineEdit(self)
        self.inputID.move(20, 250)
        self.inputID.resize(200, 20)

        btn = QPushButton('ID 중복확인', self)

        btn.resize(btn.sizeHint())
        btn.resize(100, 20)
        btn.move(235, 250)

        self.inputPW = QLineEdit(self)
        self.inputPW.move(20, 280)
        self.inputPW.resize(200, 20)

        self.inputPW2 = QLineEdit(self)
        self.inputPW2.move(20, 310)
        self.inputPW2.resize(200, 20)

        btn = QPushButton('회원가입', self)

        btn.resize(btn.sizeHint())
        btn.resize(54, 54)
        btn.move(140, 460)

        self.show()

    def joinUp_click(btn):
        pass

class Chattin(QWidget):
    pass

class Login(QWidget):
    def __init__(self):
        super().__init__()

    def loginUi(self):

        self.IDlabel = QLabel("ID", self)
        self.IDlabel.move(20, 230)

        self.inputID = QLineEdit(self)
        self.inputID.move(20, 250)
        self.inputID.resize(200, 20)

        self.PWlabel = QLabel("PW", self)
        self.PWlabel.move(20, 280)

        self.inputPW = QLineEdit(self)
        self.inputPW.move(20, 300)
        self.inputPW.resize(200, 20)

        btn = QPushButton('sign in', self)

        btn.resize(btn.sizeHint())
        btn.resize(52, 52)
        btn.move(250, 250)

        singup_btn = QPushButton('sign up', self)

        singup_btn.resize(singup_btn.sizeHint())
        singup_btn.move(20, 330)
        singup_btn.resize(70, 20)

        self.setGeometry(300, 100, 350, 550)
        self.setWindowTitle('Log in')

        btn.clicked.connect(self.login_click)

        singup_btn.clicked.connect(self.signup_click)
        self.show()

    def login_click(btn):
        string = ''
        ID = btn.inputID.text()
        passwd = btn.inputPW.text()

        if ID == '' or passwd == '':
            QMessageBox.warning(btn, 'Awwww!', '아이디 혹은 비밀번호가 비어 있습니다.')

        else:
            mysocket.sendMsg(s, '0', 0)
            mysocket.sendMsg(s, ID, 0)
            mysocket.sendMsg(s, passwd, 0)

            string = mysocket.getMsg(s, 0)

            if string == 'success':
                QMessageBox.warning(btn, 'Awwww!', string)
            else:
                QMessageBox.warning(btn, 'Awwww!', string)

        btn.inputID.setText("")
        btn.inputPW.setText("")

    def signup_click(self):
        self.tmp = SignUp()
        self.hide()
        self.tmp.signUpUi()

    def command(action):
        pass

    def run(self):
        self.loginUi()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.run()
    sys.exit(app.exec_())