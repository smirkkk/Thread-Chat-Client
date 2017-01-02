import socket
import threading

HOST = "127.0.0.1"
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def sendMsg():
    while True:
        data = input()
        s.sendall(str.encode(data))
        print("me : "+data)
    s.close()


def getMsg():
    while True:
        data = s.recv(1024)
        data = data.decode("utf-8")
        print("opponent : "+data)
    s.close()


threading._start_new_thread(sendMsg, ())
threading._start_new_thread(getMsg, ())

while True:
    pass