import socket
import threading
import sqlite3
import datetime

HEADER = 64 #hvor lang strengen der bliver sendt er
PORT = 5050 #porten der åbnes til kommunikation mellem client og server
SERVER = socket.gethostbyname("192.168.137.125") #ændre IP addressen til at være ens Raspberry PI
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def logLukData(msg):
    sqlConn = sqlite3.connect('lukData.db')
    curs = sqlConn.cursor()
    curs.execute("INSERT INTO lukTable VALUES(datetime(), (?))", (msg))
    sqlConn.commit()
    sqlConn.close()

def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msgLength = conn.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            print(type(msg))
            logLukData(msg)

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} ")


print("[STARTING] Server is starting...")
start()