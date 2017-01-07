import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QLabel, QVBoxLayout, QTabWidget, QMainWindow, QScrollArea
import socket
import myfile
import mysocket
import mysign
import threading

HOST = "127.0.0.1"
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
key = 23
username = ''
account = ''
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
        singup_btn.move(20, 130)
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
            QMessageBox.warning(self, 'Awwww!', '아이디 혹은 비밀번호가 비어 있습니다.')
        elif result == 3:
            QMessageBox.warning(self, 'Awwww!', '아이디 혹은 비밀번호가 일치하지 않습니다')
        else:
            QMessageBox.information(self, '', result + '님, 반갑습니다.')

            account = ID
            username = result

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
            QMessageBox.warning(self, 'Awwww!', '아이디는 5글자에서 20글자 까지만 가능합니다.')
            self.inputID.setText("")
            return
        elif len(ID) > 5 or len(ID) < 20:

            string = mysign.overlap(ID, s, key)

            if string == 'success':
                QMessageBox.information(self, '', '사용 가능한 아이디 입니다')
                self.i = 1

            else:
                QMessageBox.warning(self, 'Awwww!', '이미 존재하는 아이디 입니다.')
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
            QMessageBox.warning(self, 'Awwww!', '이름을 확인 해주세요')
            return
        else:
            if self.i == 0:
                QMessageBox.warning(self, 'Awwww!', '아이디 중복 확인을 해주세요.')
                return
            elif self.i == 1:
                if len(PW) < 5 or len(PW) > 20:
                    QMessageBox.warning(self, 'Awwww!', '비밀번호는 5글자에서 20글자 까지만 가능합니다.')
                    self.inputPW.setText("")
                    return
                elif len(PW) > 5 or len(PW) < 20:
                    if PW != PW2:
                        QMessageBox.warning(self, 'Awwww!', '두 비밀번호 값이 일치하지 않습니다.')
                        self.inputPW2.setText("")
                        return
                    elif PW == PW2:
                        string = mysign.signup(NAME, ID, PW, s, key)

            if string == 'success':
                QMessageBox.information(self, '', '회원가입 성공')
                self.tmp = Login()
                self.hide()
                self.tmp.loginUi()
            else:
                QMessageBox.warning(self, 'Awwww!', '회원가입 실패')


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

        self.tabs.addTab(self.tab1, "친구")
        self.tabs.addTab(self.tab2, "채팅")

        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.pushButton2 = QPushButton("TQ")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.layout.addWidget(self.pushButton2)
        self.tab1.setLayout(self.tab1.layout)

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
        self.tmp = Chatting()
        self.tmp.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.run()
    sys.exit(app.exec_())