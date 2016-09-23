#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 8899
BUFSIZE = 1024
ADDR = (HOST, PORT)

# Create udp server socket and bind it.
udp_server_sock = socket(AF_INET, SOCK_DGRAM)
udp_server_sock.bind(ADDR)

while True:
    print("Waiting for message...")
    # Receive message from client.
    recv_message_data, client_addr = udp_server_sock.recvfrom(BUFSIZE)
    # Send message to client.
    udp_server_sock.sendto('[%s] %s' % (ctime(), recv_message_data), addr)
    print("...Received from and returned to: ", addr)

# Close upd socket.
upd_server_sock.close()
