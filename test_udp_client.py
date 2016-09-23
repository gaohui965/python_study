#!/usr/bin/env python

from socket import *

# Define server ip adrress and port.
HOST = 'localhost'
PORT = 8899
BUFSIZE = 1024
ADD = (HOST, PORT)

# Create the udp connect.
udp_client_sock = socket(AF_INET, SOCK_DGRAM)

while True: 
    # Send the udp message.
    send_message_data = raw_input('> ')
    if not send_message_data:
        break
    udp_client_sock.sendto(send_message_data, ADDR)

    # Receive the udp message.
    recv_message_data, ADDR = udp_client_sock.recvfrom(BUFSIZE)
    if not recv_message_data:
        break
    print data

# Close the udp connect.
udp_client_sock.close()
