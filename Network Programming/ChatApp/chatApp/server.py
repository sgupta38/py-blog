# @author: Sonu Gupta
# @purpose: Simple Python chat application. This file acts as a 'Server', 
#           which listens for client.
#

import time
import sys
import socket
from threading import Thread
import threading

# Hardcoded data for ip/hostname and port
host = '127.0.0.1'
port = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1. Create Socket

sock.bind((host, port)) #2. Bind Socket
sock.listen()   # 3. Listen for incomming connections
conn, addr = sock.accept()  # 4. accept the connection and return the new socket object and tuple(host, port) which holds address of client
print('Connected by', addr)
print('Write \'$\' to exit')

def recvd(conn):
    try:
        while True:
            data = conn.recv(1024)
            if data.decode() == 'bye' or data.decode() == 'BYE':
                conn.close()
                return True
            else:
                print('\nCLIENT: ', data.decode())
    except:
        print('Connection is closed.')
        return True

def sendd(conn):
    try:
        while True:
            print('SERVER: ', end="")   # To show the cursor infront of 'SERVER ' token, use end=""
            srvData = input()
            if srvData == "bye" or srvData == "BYE":
                conn.close()
                return True
            else:
                conn.sendall(srvData.encode())
    except:
         print('Connection is closed.')
         return True;

        
# Ctrl+C terminates the main thread, but because your threads aren't in daemon mode, they keep running,
# and that keeps the process alive. We can make them daemons.

try:
    # recv thread
    t1 = threading.Thread(target=recvd, args=(conn,))
    t1.daemon = True;
    t1.start()

    #send thread
    t2 = threading.Thread(target=sendd, args=(conn,))
    t2.daemon = True;
    t2.start()
except:
    print('Exception occured 1')
    exit(1)


if(t1.join() or t2.join()):
    sys.exit()

