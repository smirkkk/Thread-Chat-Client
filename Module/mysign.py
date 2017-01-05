import socket
import mysocket

def login(ID, PW, s, key):
    if ID == '' or PW == '':
        return 1

    else:
        mysocket.sendMsg(s, '0', key)
        mysocket.sendMsg(s, ID, key)
        mysocket.sendMsg(s, PW, key)

        string = mysocket.getMsg(s, key)

        if string == 'success':
            return 2

        else:
            return 3

def signup(Name, ID, PW, s, key):
    mysocket.sendMsg(s, '1', key)
    mysocket.sendMsg(s, Name, key)
    mysocket.sendMsg(s, ID, key)
    mysocket.sendMsg(s, PW, key)

    result = mysocket.getMsg(s, key)

    return result

def overlap(ID, s, key):
    mysocket.sendMsg(s, '99', 0)
    mysocket.sendMsg(s, ID, 0)
    result = mysocket.getMsg(s, 0)

    return result