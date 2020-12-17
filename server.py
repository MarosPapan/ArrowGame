import socket
from _thread import *
import sys

server = "192.168.0.108"
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("waiting for connected, server started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(128,600-90),(500,600-90)]

def thread_client(conn, player, player2):
    conn.send(str.encode(make_pos(pos[player])))#!!!here is also maybe mystake becouse i have 2 class of player ok
    conn.send(str.encode(make_pos(pos[player2])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            pos[player2] = data

            if not data:
                print("disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received:", data)
                print("Sending:", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to", addr)
    start_new_thread(thread_client, (conn, currentPlayer))
    currentPlayer += 1