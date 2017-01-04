import socket
import threading
import mysocket

HOST = '127.0.0.1'
PORT = 6974
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print(addr)

def sendMsg():
    while True:
        data = input()
        data = data.encode("utf-8")
        conn.send(data)
    conn.close()


def getMsg():
    while True:
        data = conn.recv(1024)
        if data == None:
            break
        else:
            data = data.decode("utf-8", "ignore")
            data = mysocket.cryption(data, 0)
            print(data)
    conn.close()


threading._start_new_thread(sendMsg, ())
threading._start_new_thread(getMsg, ())

while True:
    pass