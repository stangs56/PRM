import socket

class Client:
    def __init__(self, ip = '127.0.0.1', port = 50405):
        self.ip = ip
        self.port = port

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))

        while True:
            length = int.from_bytes(self.s.recv(4), 'big')
            msg = ''

            while(len(msg) != length):
                msg = msg + self.s.recv(length)

            resp = self.processMessage(msg).encode()

            self.s.send(len(resp).to_bytes(4, 'big'))
            self.s.send(resp)

    def processMessage(self, msg):
        pass
