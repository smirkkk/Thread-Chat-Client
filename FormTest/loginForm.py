import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QLabel
import socket
import mysocket
import mysign
import threading

HOST = "127.0.0.1"
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


## close add need
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

        test_btn = QPushButton('테스트', self)

        test_btn.resize(test_btn.sizeHint())
        test_btn.resize(100, 20)
        test_btn.move(265, 100)

        test_btn.clicked.connect(self.move_to_login)

        self.show()

    def check_btn_click(self):
        ID = self.inputID.text()  # 길이 조건이 맞을때 버튼 활성화    #길이체크

        if len(ID) < 5 or len(ID) > 20:
            QMessageBox.warning(self, 'Awwww!', '아이디는 5글자에서 20글자 까지만 가능합니다.')
            self.inputID.setText("")
            return
        elif len(ID) > 5 or len(ID) < 20:

            string = mysign.overlap(ID, s, 0)

            if string == 'success':
                QMessageBox.information(self, '', '사용 가능한 아이디 입니다')
                self.i = 1

            else:
                QMessageBox.warning(btn, 'Awwww!', '이미 존재하는 아이디 입니다.')
                self.inputID.setText("")

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
                    QMessageBox.warning(self, 'Awwww!', '아이디 중복 확인을 해주세요.')
                    self.inputPW.setText("")
                    return
                elif len(PW) > 5 or len(PW) < 20:
                    if PW != PW2:
                        QMessageBox.warning(self, 'Awwww!', '두 비밀번호 값이 일치하지 않습니다.')
                        self.inputPW2.setText("")
                        return
                    elif PW == PW2:
                        string = mysign.signup(NAME, ID, PW, s, 0)

            if string == 'success':
                QMessageBox.information(self, '', '회원가입 성공')
                move_to_login()
            else:
                QMessageBox.warning(self, 'Awwww!', '회원가입 실패')

    def move_to_login(self):
        self.tmp = Login()
        self.hide()
        self.tmp.loginUi()


class Chattin(QWidget):
    pass


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

    def login_click(btn):
        string = ''
        ID = btn.inputID.text()
        passwd = btn.inputPW.text()

        result = mysign.login(ID, passwd, s, 0)

        if result == 1:
            QMessageBox.warning(btn, 'Awwww!', '아이디 혹은 비밀번호가 비어 있습니다.')
        elif result == 2:
            QMessageBox.information(btn, '', '로그인 성공')
            pass
            # 다음 폼으로 넘기기
        elif result == 3:
            QMessageBox.warning(btn, 'Awwww!', '아이디 혹은 비밀번호 일치하지 않습니다')

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