import socket
import threading

HOST = "127.0.0.1"
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def sendmsg():
    while True:
        data = input()
        s.sendall(str.encode(data))
    s.close()


def getmsg():
    while True:
        data = s.recv(1024)
        data = data.decode("utf-8")
        print(data)
    s.close()


threading._start_new_thread(sendmsg, ())
threading._start_new_thread(getmsg, ())

while True:
    pass
