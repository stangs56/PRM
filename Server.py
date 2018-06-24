import socket
import select

from threading import Thread

from ConnectedClient import *

class Server:
    def __init__(self, ip = '', port = 50405):
        self.ip = ip
        self.port = port
        self.connections = []
        self.clients = {}

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ip, self.port))
        s.listen()

        self.readLoopThread = Thread(target = self.readLoop)
        self.readLoopThread.start()
        self.readLoopThread.run()

        while True:
            conn, addr = s.accept()
            conn.setblocking(0)
            self.connections.append(conn)
            self.clients[addr] = (ConnectedClient(conn, addr))

    def readLoop(self):
        while True:
            r, w, e = select.select(self.connections, [], [], 60)
            for rs in r:
                length = int.from_bytes(rs.recv(4), 'big')
                msg = ''

                while(len(msg) != length):
                    msg = msg + rs.recv(length)

                self.clients[rs.getpeername()].addMessage(msg.decode())
