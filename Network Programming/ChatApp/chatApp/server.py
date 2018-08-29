# @author: Sonu Gupta
# @purpose: Simple Python chat application. This file acts as a 'Server', 
#           which listens for client.
#
# @todo: Support for non-blocking socket

import sys
import socket

# Hardcoded data for ip/hostname and port
host = '127.0.0.1'
port = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1. Create Socket

sock.bind((host, port)) #2. Bind Socket
sock.listen()   # 3. Listen for incomming connections
conn, addr = sock.accept()  # 4. accept the connection and return the new socket object and tuple(host, port) which holds address of client
print('Connected by', addr)
print('Write \'$\' to exit')

while True:
    data = conn.recv(1024)
    if data.decode() == '$':
        print('Connection aborted by client')
        break
    else:
     print('CLIENT: ', data.decode())

     # 'end' parameter is used to specify the line end character. 
     # We will set end option to nothing and this will remove default \n or end of line or space.

     print('SERVER: ', end="")   # To show the cursor infront of 'SERVER ' token, use end=""
     srvData = input()
     conn.sendall(srvData.encode())

sock.close()