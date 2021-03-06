#
#   @author: Sonu Gupta
#
#   #purpose: Echo Server example.


import socket

HOST = "127.0.0.1"
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # bind takes one argument
    s.listen()

    conn, addr = s.accept()  # returns a new socket object representing the connection and a "tuple" holding the address of the client. 
    with conn:
        print('Connected By', addr)
        while True:
            data = conn.recv(1024)

            if not data:
                break;
            print('Data Received is ', data)
            conn.sendall(data)