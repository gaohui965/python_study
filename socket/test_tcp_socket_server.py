#!/usr/bin/env python

from SocketServer import (TCPServer as TCP,
     StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 8899
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handler(self):
        print("...Conneted from: ", self.client_address)
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline())

tcp_server = TCP(ADDR, MyRequestHandler)

print("Waiting for connection...")
tcp_server.serve_forever()
