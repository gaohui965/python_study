#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 8899
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    # Create a socket and connect the sercer.
    tcp_client_sock = socket(AF_INET, SOCK_STREAM)
    tcp_client_sock.connect(ADDR)

    # Send message to server.
    send_message_data = raw_input('> ')
    if not send_message_data:
        break
    tcp_client_sock.send('%s\r\n' % send_message_data)
    
    # Receive the message and print it.
    recv_message_data = tcp_client_sock.recv(BUFSIZE)
    if not recv_message_data:
        break
    print data.strip()

    # Close tcp socket.
    tcp_client_sock.close()
