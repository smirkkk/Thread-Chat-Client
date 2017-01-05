import socket
import mysocket

def login(ID, passwd, s):
    if ID == '' or passwd == '':
        QMessageBox.warning(btn, 'Awwww!', '아이디 혹은 비밀번호가 비어 있습니다.')

    else:
        mysocket.sendMsg(s, '0', 0)
        mysocket.sendMsg(s, ID, 0)
        mysocket.sendMsg(s, passwd, 0)
        """
        string = mysocket.getMsg(s, 0)

        if string == 'success':
            QMessageBox.warning(btn, 'Awwww!', string)
        else:
            QMessageBox.warning(btn, 'Awwww!', string)
        """