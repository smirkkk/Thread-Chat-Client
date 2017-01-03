import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
import socket

HOST = "10.156.145.99"
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.inputID = QLineEdit(self)
        self.inputID.move(20, 20)
        self.inputID.resize(150,20)

        self.inputPW = QLineEdit(self)
        self.inputPW.move(20, 50)
        self.inputPW.resize(150,20)

        btn = QPushButton('Login', self)
        btn.resize(btn.sizeHint())
        btn.move(200,20)
        btn.resize(55,55)

        self.setGeometry(300,100,300,500)
        self.show()

        btn.clicked.connect(self.login_click)
        self.show()

    def login_click(btn):
        value = btn.inputID.text()+chr(0)
        passwd = btn.inputPW.text()+chr(0)
        s.sendall(str.encode(value))
        s.sendall(str.encode(passwd))
        btn.inputID.setText("")
        btn.inputPW.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())