# @author: Sonu Gupta
# @purpose: Simple Python chat application. This file acts as a client, 
#           which initiates the connection and sends the message.
#
# @todo: Support for non-blocking socket


import sys
import socket

# Hardcoded data for ip/hostname and port of listening Server

host = '127.0.0.1'
port = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

print('Write \'$\' to exit')

while True:
     # 'end' parameter is used to specify the line end character. 
     # We will set end option to nothing and this will remove default \n or end of line or space.

    print('CLIENT: ', end="")
    clnData = input()
    sock.sendall(clnData.encode())
    if(clnData == '$'):
        break;

    data = sock.recv(1024)
    if(data.decode() == '$'):
        break
    else:
        print('SERVER: ', data.decode())

sock.close()



