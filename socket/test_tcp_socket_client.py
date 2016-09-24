#!/usr/bin/env python

from socket import *
import sys

HOST = '127.0.0.1'
PORT = 8899
BUFSIZE = 1024

args_count = len(sys.argv) - 1
if args_count == 0:
    server_host = HOST
    server_port = PORT
elif args_count == 1:
    server_host = sys.argv[1]
    server_port = PORT
elif args_count == 2:
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
else:
    print("Too must arguments!")
    exit(1)

server_addr = (server_host, server_port)
print server_addr

while True:
    # Create a socket and connect the sercer.
    tcp_client_sock = socket(AF_INET, SOCK_STREAM)
    tcp_client_sock.connect(server_addr)

    # Send message to server.
    send_message_data = raw_input('> ')
    if not send_message_data:
        break
    tcp_client_sock.send('%s\r\n' % send_message_data)
    
    # Receive the message and print it.
    recv_message_data = tcp_client_sock.recv(BUFSIZE)
    if not recv_message_data:
        break
    print recv_message_data.strip()

    # Close tcp socket.
    tcp_client_sock.close()
