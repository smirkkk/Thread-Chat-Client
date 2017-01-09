import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QAction, QTabWidget,QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit, QLabel
import myfile
import socket
import mysocket
import threading

HOST = "192.168.137.191"
PORT = 6974
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((HOST, PORT))
key = 23
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


class mainWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab4 = QWidget()

        self.tabs.addTab(self.tab1, "친구")
        self.tabs.addTab(self.tab2, "채팅")
        self.tabs.addTab(self.tab4, "설정")

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

        self.tab4.layout = QVBoxLayout(self)
        self.withdraw_btn = QPushButton('탈퇴')
        self.logout_btn = QPushButton('로그아웃')
        self.tab4.layout.addWidget(self.withdraw_btn)
        self.tab4.layout.addWidget(self.logout_btn)
        self.tab4.setLayout(self.tab4.layout)

        self.withdraw_btn.clicked.connect(self.withdraw_btn_click)
        self.logout_btn.clicked.connect(self.logout_btn_click)

    def withdraw_btn_click(self):
        self.tmp = withdrawID()
        self.tmp.withdrawUi()

    def btn_click(self):
        self.tmp = chatting()
        self.tmp.chatUi()

    def refresh_click(self):
        friend_list = []

        mysocket.sendMsg(s, '5', key)

        while True:
            string = mysocket.getMsg(s, key)
            if string == 'end' or string == 'end ':
                break
            else:
                friend_list.append(string)

        print(friend_list)

    def logout_btn_click(self):
        answer = QMessageBox.warning(self, '로그아웃', '로그아웃 하시겠습니까?', QMessageBox.Ok|QMessageBox.No)
        if (answer == QMessageBox.No):
            return
        else:
            QMessageBox.information(self, '로그아웃', '로그아웃')
            #mysocket.sendMsg(s, '8', key)
            #로그인 정보 비우고
            #로그인 폼으로 이동.




class withdrawID(QWidget):

    def __init__(self):
        super().__init__()

    def withdrawUi(self):
        self.setGeometry(300, 100, 240, 160)
        self.setWindowTitle('회원 탈퇴')

        self.name_label = QLabel("대화 내용, 친구 목록 등 모든 정보가\n즉시 삭제되며 복구가 불가능합니다.\n\n비밀번호를 입력해주세요 : ", self)
        self.name_label.move(20, 20)

        self.input_PW = QLineEdit(self)
        self.input_PW.move(20, 80)
        self.input_PW.resize(200, 20)

        self.with_btn = QPushButton('회원 탈퇴', self)
        self.with_btn.resize(200, 20)
        self.with_btn.move(20, 110)

        self.with_btn.clicked.connect(self.with_btn_click)

        self.show()

    def with_btn_click(self):
        if self.input_PW.text() == '':
            QMessageBox.warning(self, '회원 탈퇴', '비밀번호를 입력해 주세요')
            return

        answer = QMessageBox.warning(self, '회원 탈퇴', '정말로 탈퇴 하시겠습니까?\n삭제된 정보는 복구가 불가능합니다.', QMessageBox.Ok|QMessageBox.No)
        if (answer == QMessageBox.No):
            return
        else:
            QMessageBox.information(self, '와시발 ㅋㅋ', '엠창 탈퇴하네')
            """
            mysocket.sendMsg(s, '2', key)
            mysocket.sendMsg(s, self.input_PW.text(), key)
            result = mysocket.getMsg(s, key)
            if result == 'PW different' or result == 'PW different ':
                QMessageBox.warning(self, '회원 탈퇴', '회원 탈퇴 실패')
                return
            else:
                QMessageBox.information(self, '회원 탈퇴', '지금까지 감사헀습니다. 안녕~')
                로그인 폼으로.
            """




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainUi()
    sys.exit(app.exec_())