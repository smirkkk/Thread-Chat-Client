import socket

def sendMsg(socket,string, key):
    string = cryption(string, key)
    socket.sendall(str.encode(string+chr(0)))

def getMsg(socket, key):
    string=''

    while True:
        data = socket.recv(1)
        data=data.decode("utf-8")

        if data == chr(0):
            break
        string+=data

    string = cryption(string, key)
    return string


def cryption(string, key):
    trash = ''
    tmp = ''

    for x in range(len(string)):
        tmp = ord(string[x])
        tmp ^= key
        trash += chr(tmp)

    return trash
