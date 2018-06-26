import socket
import select

from threading import Thread, Event

from ConnectedClient import *

class Server:
    def __init__(self, ip = '', port = 50405):
        self.ip = ip
        self.port = port
        self.connections = []
        self.clients = {}
        self.waitForConnect = Event()

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ip, self.port))
        self.s.listen()

        self.readLoopThread = Thread(target = self.readLoop)
        self.readLoopThread.start()

        while True:
            conn, addr = self.s.accept()
            conn.setblocking(0)
            self.connections.append(conn)
            self.clients[addr] = (ConnectedClient(conn, addr))
            self.waitForConnect.set()

    def readLoop(self):
        while True:
            if len(self.connections) == 0:
                self.waitForConnect.clear()

            self.waitForConnect.wait()

            r, w, e = select.select(self.connections, self.connections, [], 60)
            for rs in r:
                length = int.from_bytes(rs.recv(4), 'big')
                msg = ''

                while(len(msg) != length):
                    msg = msg + rs.recv(length - len(msg))

                self.clients[rs.getpeername()].addMessage(msg)

            #remove connections that are not able to be written
            for ws in set(self.connections) - set(w):
                self.connections.remove(ws)
                del(self.clients[ws.getpeername()])
                ws.close()
