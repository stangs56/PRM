import queue

class ConnectedClient:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

        self.messages = queue.Queue()
        self.requests = queue.Queue()

    def addMessage(self, msg):
        self.messgaes.put(msg)

    def sendRequest(self, req):
        self.requests.put(req)
        req = req.encode()
        self.conn.send(len(req).to_bytes(4, 'big'))
        self.conn.send(req)

    def getMsgResponse(self):
        return (self.requests.get(), self.messages.get())
