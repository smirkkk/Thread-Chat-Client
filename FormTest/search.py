import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QApplication, QMessageBox
import socket
import mysocket

HOST = "192.168.137.191"
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
key = 23
username = ''
account = ''
friend = ['a', 'b', 'c']

class searchID(QWidget):
    def __init__(self):
        super().__init__()

    def searchIDForm(self):
        self.name_label = QLabel("아이디로 친구를 검색합니다.", self)
        self.name_label.move(20, 20)

        self.result_label = QLabel("검색 결과", self)
        self.result_label.move(20, 100)

        self.input_search_ID = QLineEdit(self)
        self.input_search_ID.move(20, 50)
        self.input_search_ID.resize(200, 20)

        self.nickname = QLabel(self)
        self.nickname.move(20, 130)
        self.nickname.resize(200, 20)

        search_btn = QPushButton('검색', self)

        search_btn.resize(search_btn.sizeHint())
        search_btn.resize(100, 22)
        search_btn.move(235, 50)

        search_btn.clicked.connect(self.search_click)

        self.add_btn = QPushButton('find', self)

        self.add_btn.resize(self.add_btn.sizeHint())
        self.add_btn.resize(100, 22)
        self.add_btn.move(235, 130)
        self.add_btn.setVisible(False)


        self.setGeometry(300, 100, 350, 180)
        self.setWindowTitle('친구 찾기')
        self.show()


    def search_click(self):
        ID = self.input_search_ID.text()


        mysocket.sendMsg(s, '3', key)
        mysocket.sendMsg(s, ID, key)
        string = mysocket.getMsg(s, key)

        self.add_btn.setVisible(False)

        self.nickname.setText(string)

        if string == 'not Find!' or string == 'not Find! ':
            QMessageBox.warning(self, '', '존재하지 않는 ID 입니다.')
            self.nickname.setText('존재하지 않는 ID 입니다.')

        elif friend.__contains__(ID) == False:
            self.add_btn.setVisible(True)
            #string2 = mysocket.getMsg(s, key)
            #print(string2)

        else:
            QMessageBox.warning(self, '', '이미 추가되어 있는 사용자 입니다.')
            self.nickname.setText(self.input_search_ID.text()+' 님은 이미 추가된 사용자 입니다.')


    def add_click(self):
        mysocket.sendMsg(s, '4', key)
        mysocket.sendMsg(s, self.input_search_ID.text(), key)
        #친구추가 성공했는지 실패했는지 확인필요



    def run(self):
        self.searchIDForm()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = searchID()
    ex.run()
    sys.exit(app.exec_())