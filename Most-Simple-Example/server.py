import socket
import threading
import mysocket

HOST = '127.0.0.1'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print(addr)


def sendmsg():
    while True:
        data = input()
        data = data.encode("utf-8")
        conn.send(data)
    conn.close()


def getmsg():
    while True:
        data = conn.recv(1024)

        if data is None:
            break
        else:
            data = data.decode("utf-8", "ignore")
            data = mysocket.cryption(data, 0)
            print(data)
    conn.close()


threading._start_new_thread(sendmsg, ())
threading._start_new_thread(getmsg, ())

while True:
    pass
