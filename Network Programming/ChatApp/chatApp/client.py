# @author: Sonu Gupta
# @purpose: Simple Python chat application. This file acts as a client, 
#           which initiates the connection and sends the message.
#

import time
import sys
import socket
import threading
from threading import Thread

# Hardcoded data for ip/hostname and port of listening Server

host = '127.0.0.1'
port = 65432

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))

print('Write \'$\' to exit')

def recvd(conn):
    try:
        while True:
            data = conn.recv(1024)
            if data.decode() == 'bye' or data.decode == 'BYE':
                conn.close()
                return True
            else:
                print('\nSERVER: ', data.decode())
                data=''
    except:
        print('Connection is closed')
        return True


def sendd(conn):
    try:
        while True:
            print('CLIENT: ', end="")   # To show the cursor infront of 'SERVER ' token, use end=""
            srvData = input()
            if srvData == "bye" or srvData == "BYE":
                conn.close()
                return True
            else:
                conn.sendall(srvData.encode())
                srvData=''
    except:
        print('Connection is closed')
        return True

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
    print('Some exception occured 1')
    sys.exit(1)

if(t1.join() or t2.join()):
    sys.exit()


