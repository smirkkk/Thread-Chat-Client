import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QApplication
import socket
import mysocket

HOST = "127.0.0.1"
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
key = 23
username = ''
account = ''
friend = ['a', 'b', 'c']

class findID(QWidget):
    def __init__(self):
        super().__init__()

    def findIDForm(self):
        self.name_label = QLabel("친구 찾기", self)
        self.name_label.move(5, 5)

        self.input_search_ID = QLineEdit(self)
        self.input_search_ID.move(20, 50)
        self.input_search_ID.resize(200, 20)

        self.nickname = QLabel(self)
        self.nickname.move(20, 130)
        self.nickname.resize(200, 20)

        search_btn = QPushButton('find', self)

        search_btn.resize(search_btn.sizeHint())
        search_btn.resize(100, 22)
        search_btn.move(235, 50)

        search_btn.setVisible(True)

        search_btn.clicked.connect(self.search_click)

        self.add_btn = QPushButton('find', self)

        self.add_btn.resize(self.add_btn.sizeHint())
        self.add_btn.resize(52, 52)
        self.add_btn.move(235, 150)
        self.add_btn.setVisible(False)

        self.yet = QLabel(self)
        self.yet.move(235, 150)
        self.yet.resize(200, 20)

        self.setGeometry(300, 100, 350, 180)
        self.setWindowTitle('친구 찾기')
        self.show()

        self.setGeometry(300, 100, 350, 180)
        self.setWindowTitle('친구 찾기')
        self.show()

    def search_click(self):
        ID = self.input_search_ID.text()
        mysocket.sendMsg(s, '3', key)
        mysocket.sendMsg(s, ID, key)

        string = mysocket.getMsg(s, key)

        self.add_btn.setVisible(False)
        self.yet.setText("")

        self.nickname.setText(string)

        if friend.__contains__(ID) == False:
            self.add_btn.setVisible(True)
        else:
            self.yet.setText("이미 추가되어 있는 사용자 입니다.")



    def run(self):
        self.findIDForm()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = findID()
    ex.run()
    sys.exit(app.exec_())