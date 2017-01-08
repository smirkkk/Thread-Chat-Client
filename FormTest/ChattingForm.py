import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QAction, QTabWidget,QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit
import myfile
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import socket
import mysocket
import threading

HOST = "127.0.0.1"
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
key = 0
friend_list = []


class MainUi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(300,100,300,500)
        self.table_widget = mainWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()

class chatting(QWidget):

    def __init__(self):
        super().__init__()

    def chatUi(self):
        string = '15 나성범 RF'
        self.setGeometry(124,200,300,500)
        self.setWindowTitle(string)

        self.chat = QLineEdit(self)
        self.chat.setReadOnly(True)
        self.chat.move(5, 5)
        self.chat.resize(290, 390)

        self.text = QLineEdit(self)
        self.text.move(5, 400)
        self.text.resize(233, 70)

        btn = QPushButton('전송', self)

        btn.resize(btn.sizeHint())
        btn.resize(52, 70)
        btn.move(243, 400)

        btn.clicked.connect(self.send_click)

        attach_btn = QPushButton('파일 첨부', self)

        attach_btn.resize(attach_btn.sizeHint())
        attach_btn.resize(60, 20)
        attach_btn.move(5, 475)

        attach_btn.clicked.connect(self.attach_btn_click)

        self.show()

    def send_click(self):
        mysocket.sendMsg(s, self.text.text(), key)
        a = self.chat.text() + '\n' + "me : "+self.text.text()
        self.chat.setText(a)
        self.text.setText("")

    def get_get_Msg(self):

        getString = mysocket.getMsg(s, key)
        print(getString)
        self.cat.setText("oppenent : "+getString)

    def attach_btn_click(self):
        nametest = 'test'
        file = myfile.openFileNameDialog(self)
        myfile.uploadFile(self, file_path=file, file_name=nametest, folder='')
        self.chat.setText('일단 업로드 성공~!@#45ㅁ6')

#    threading._start_new_thread(mysocket.sendMsg, (s, chatUi().text.text(), key))
#    threading._start_new_thread(get_get_Msg, ())


class mainWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1, "친구")
        self.tabs.addTab(self.tab2, "채팅")

        self.tab1.layout = QVBoxLayout(self)
        self.Refresh = QPushButton("친구목록 불러오기")
        self.pushButton2 = QPushButton("TQ")
        self.tab1.layout.addWidget(self.Refresh)
        self.tab1.layout.addWidget(self.pushButton2)
        self.tab1.setLayout(self.tab1.layout)

        self.Refresh.clicked.connect(self.refresh_click)

        self.tab2.layout = QVBoxLayout(self)
        self.pushButton3 = QPushButton("1")
        self.pushButton4 = QPushButton("2")
        self.tab2.layout.addWidget(self.pushButton3)
        self.tab2.layout.addWidget(self.pushButton4)
        self.tab2.setLayout(self.tab2.layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.pushButton4.clicked.connect(self.btn_click)

    def btn_click(self):
        self.tmp = chatting()
        self.tmp.chatUi()

    def refresh_click(self):
        friend_list = []

        #mysocket.sendMsg(s, '5', key)
        data = '5'
        s.sendall(str.encode(data))

        while True:
            #tmp = mysocket.getMsg(s, key)
            tmp = s.recv(1024)
            tmp = tmp.decode("utf-8")

            if tmp == 'end':
                break
            else:
                friend_list.append(tmp)

        print(friend_list)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainUi()
    sys.exit(app.exec_())