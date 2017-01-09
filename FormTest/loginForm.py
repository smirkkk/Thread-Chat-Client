import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QLabel, QVBoxLayout, QTabWidget, QMainWindow, QScrollArea
import socket
import myfile
import mysocket
import mysign
import threading

HOST = "192.168.137.191"
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
key = 23

user_info = {
    'username': '',
    'account': ''
}

friend_list = []

## close add need

class Login(QWidget):
    def __init__(self):
        
        super().__init__()

    def loginUi(self):

        self.IDlabel = QLabel("ID", self)
        self.IDlabel.move(20, 30)

        self.inputID = QLineEdit(self)
        self.inputID.move(20, 50)
        self.inputID.resize(200, 20)

        self.PWlabel = QLabel("PW", self)
        self.PWlabel.move(20, 80)

        self.inputPW = QLineEdit(self)
        self.inputPW.move(20, 100)
        self.inputPW.resize(200, 20)

        btn = QPushButton('sign in', self)

        btn.resize(btn.sizeHint())
        btn.resize(52, 52)
        btn.move(250, 50)

        singup_btn = QPushButton('sign up', self)


        singup_btn.resize(singup_btn.sizeHint())
        singup_btn.move(20, 150)
        singup_btn.resize(70, 20)

        self.setGeometry(300, 100, 350, 180)
        self.setWindowTitle('Log in')

        btn.clicked.connect(self.login_click)

        singup_btn.clicked.connect(self.signup_click)
        self.show()

    def login_click(self):
        string = ''
        ID = self.inputID.text()
        passwd = self.inputPW.text()

        result = mysign.login(ID, passwd, s, key)

        if result == 1:
            QMessageBox.warning(self, '로그인', '아이디 혹은 비밀번호가 비어 있습니다.')
        elif result == 3:
            QMessageBox.warning(self, '로그인', '아이디 혹은 비밀번호가 일치하지 않습니다')
        else:
            QMessageBox.information(self, '로그인', result + '님, 반갑습니다.')

            user_info['username'] = result
            user_info['account'] = ID

            self.tmp = MainForm()
            self.hide()
            self.tmp.draw()

        self.inputID.setText("")
        self.inputPW.setText("")

    def signup_click(self):
        self.tmp = SignUp()
        self.hide()
        self.tmp.signUpUi()

    def command(action):
        pass

    def run(self):
        self.loginUi()


class SignUp(QWidget):
    i = 0

    def signUpUi(self):
        self.setGeometry(300, 100, 350, 550)
        self.setWindowTitle('Sign Up')

        self.inputNm = QLineEdit(self)
        self.inputNm.move(20, 50)
        self.inputNm.resize(200, 20)

        self.Nmlabel = QLabel("이름", self)
        self.Nmlabel.move(20, 30)

        self.IDlabel = QLabel("ID", self)
        self.IDlabel.move(20, 80)

        self.inputID = QLineEdit(self)
        self.inputID.move(20, 100)
        self.inputID.resize(200, 20)

        check_btn = QPushButton('ID 중복확인', self)

        check_btn.resize(check_btn.sizeHint())
        check_btn.resize(100, 20)
        check_btn.move(235, 100)

        check_btn.clicked.connect(self.check_btn_click)

        self.PWlabel = QLabel("PW", self)
        self.PWlabel.move(20, 130)

        self.inputPW = QLineEdit(self)
        self.inputPW.move(20, 150)
        self.inputPW.resize(200, 20)

        self.PW2label = QLabel("PW 재입력", self)
        self.PW2label.move(20, 180)

        self.inputPW2 = QLineEdit(self)
        self.inputPW2.move(20, 200)
        self.inputPW2.resize(200, 20)

        btn = QPushButton('회원가입', self)

        btn.resize(btn.sizeHint())
        btn.resize(54, 54)
        btn.move(140, 460)

        btn.clicked.connect(self.signup_click)

        self.show()

    def check_btn_click(self):
        ID = self.inputID.text()

        if len(ID) < 5 or len(ID) > 20:
            QMessageBox.warning(self, '회원 가입', '아이디는 5글자에서 20글자 까지만 가능합니다.')
            self.inputID.setText("")
            return
        elif len(ID) > 5 or len(ID) < 20:

            string = mysign.overlap(ID, s, key)

            if string == 'success':
                QMessageBox.information(self, '회원 가입', '사용 가능한 아이디 입니다')
                self.i = 1

            else:
                QMessageBox.warning(self, '회원 가입', '이미 존재하는 아이디 입니다.')
                self.inputID.setText("")

    def move_to_login(self):
        self.tmp = Login()
        self.hide()
        self.tmp.loginUi()

    def signup_click(self):
        NAME = self.inputNm.text()
        ID = self.inputID.text()
        PW = self.inputPW.text()
        PW2 = self.inputPW2.text()

        if NAME == '':
            QMessageBox.warning(self, '회원 가입', '이름을 확인 해주세요')
            return
        else:
            if self.i == 0:
                QMessageBox.warning(self, '회원 가입', '아이디 중복 확인을 해주세요.')
                return
            elif self.i == 1:
                if len(PW) < 5 or len(PW) > 20:
                    QMessageBox.warning(self, '회원 가입', '비밀번호는 5글자에서 20글자 까지만 가능합니다.')
                    self.inputPW.setText("")
                    return
                elif len(PW) > 5 or len(PW) < 20:
                    if PW != PW2:
                        QMessageBox.warning(self, '회원 가입', '두 비밀번호 값이 일치하지 않습니다.')
                        self.inputPW2.setText("")
                        return
                    elif PW == PW2:
                        mysocket.sendMsg(s, '1', key)

                        mysocket.sendMsg(s, ID, key)
                        mysocket.sendMsg(s, PW, key)
                        mysocket.sendMsg(s, NAME, key)

                        string = mysocket.getMsg(s, key)


        if string == 'success':
            QMessageBox.information(self, '회원 가입', '회원가입 성공')
            self.tmp = Login()
            self.hide()
            self.tmp.loginUi()
        else:
            QMessageBox.warning(self, '회원 가입', '회원가입 실패')


class MainForm(QMainWindow):
    def draw(self):
        self.setGeometry(300, 100, 300, 500)
        self.table_widget = MainWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()


class Chatting(QWidget):
    def draw(self):
        string = '15 나성범 RF'
        self.setGeometry(124, 200, 300, 500)
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

    def attach_btn_click(self):
        nametest = 'test'
        file = myfile.openFileNameDialog(self)
        myfile.uploadFile(self, file_path=file, file_name=nametest, folder='')
        self.chat.setText('일단 업로드 성공~!@#45ㅁ6')


class MainWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.tabs.addTab(self.tab1, "친구")
        self.tabs.addTab(self.tab2, "채팅")
        self.tabs.addTab(self.tab3, "검색")
        self.tabs.addTab(self.tab4, "설정")

        self.tab1.layout = QVBoxLayout(self)
        self.refresh_btn = QPushButton("친구목록 새로고침")
        self.tab1.layout.addWidget(self.refresh_btn)
        self.tab1.setLayout(self.tab1.layout)
        self.refresh_btn.clicked.connect(self.refresh_click)

        self.tab2.layout = QVBoxLayout(self)
        self.pushButton3 = QPushButton("1")
        self.pushButton4 = QPushButton("2")
        self.tab2.layout.addWidget(self.pushButton3)
        self.tab2.layout.addWidget(self.pushButton4)
        self.tab2.setLayout(self.tab2.layout)

        self.tab3.layout = QVBoxLayout(self)

        self.search_label = QLabel('아이디를 통해 쉽게 친구를 추가하세요.')
        self.myID = QLineEdit('내 아이디 : '+user_info['account'])
        self.myID.setReadOnly(True)

        self.to_search = QPushButton("검색")

        self.tab3.layout.addWidget(self.search_label)
        self.tab3.layout.addWidget(self.myID)
        self.tab3.layout.addWidget(self.to_search)


        self.tab3.setLayout(self.tab3.layout)

        self.to_search.clicked.connect(self.move_to_search)


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

    def btn_click(self):
        self.tmp = Chatting()
        self.tmp.draw()

    def refresh_click(self):
        friend_list = []

        mysocket.sendMsg(s, '5', key)

        while True:
            string = mysocket.getMsg(s, key)
            if string == 'end' or string == 'end ':
                break
            else:
                friend_list.append(string)

        print(user_info['username'])
        print(user_info['account'])
        print(friend_list)

    def move_to_search(self):
        self.tmp = searchID()
        self.tmp.searchIDForm()

    def withdraw_btn_click(self):
        self.tmp = withdrawID()
        self.tmp.withdrawUi()

    def logout_btn_click(self):
        answer = QMessageBox.warning(self, '로그아웃', '로그아웃 하시겠습니까?', QMessageBox.Ok|QMessageBox.No)
        if (answer == QMessageBox.No):
            return
        else:
            QMessageBox.information(self, '로그아웃', '로그아웃')
            #mysocket.sendMsg(s, '8', key)
            #로그인 정보 비우고
            #로그인 폼으로 이동.

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
        self.nickname.move(20, 125)
        self.nickname.resize(200, 40)

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

        self.add_btn.clicked.connect(self.add_click)

        self.setGeometry(300, 100, 350, 180)
        self.setWindowTitle('친구 찾기')
        self.show()

    def search_click(self):
        ID = self.input_search_ID.text()

        mysocket.sendMsg(s, '3', key)
        mysocket.sendMsg(s, ID, key)
        string = mysocket.getMsg(s, key)

        self.add_btn.setVisible(False)

        if string == 'not Find!' or string == 'not Find! ':
            QMessageBox.warning(self, '친구 찾기', '존재하지 않는 ID 입니다.')
            self.nickname.setText('존재하지 않는 ID 입니다.')

        elif ID == user_info['account']:
            string2 = mysocket.getMsg(s, key)
            self.nickname.setText('ID : ' + string + '\n닉네임 : ' + string2)

        elif friend_list.__contains__(ID) == False:
            string2 = mysocket.getMsg(s, key)
            self.nickname.setText('ID : ' + string + '\n닉네임 : ' + string2)
            self.add_btn.setVisible(True)
        else:
            QMessageBox.warning(self, '친구 찾기', '이미 추가되어 있는 사용자 입니다.')
            self.nickname.setText(self.input_search_ID.text()+' 님은\n이미 추가된 사용자 입니다.')

    def add_click(self):
        mysocket.sendMsg(s, '4', key)
        mysocket.sendMsg(s, self.input_search_ID.text(), key)

        friend_list.append(self.input_search_ID.text())

        QMessageBox.information(self, '친구 추가', '추가되었습니다.')

        self.add_btn.setVisible(False)
        self.nickname.setText(self.input_search_ID.text() + ' 님은\n이미 추가된 사용자 입니다.')

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
    ex = Login()
    ex.run()
    sys.exit(app.exec_())