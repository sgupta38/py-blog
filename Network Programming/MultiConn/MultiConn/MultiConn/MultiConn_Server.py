import sys
import selectors
import socket
import types

sel = selectors.DefaultSelector()

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            print('RECEIVED ', recv_data)
            data.outb += recv_data
        else:
            print('Closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('SENDING: ', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]

if len(sys.argv) !=3:
    print('usage:', sys.argv[0], '<host><port>')
    sys.exit(1)


HOST, PORT = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print('Listening on port ', (HOST, PORT))
lsock.setblocking(False) #Calls made to this socket will no longer block. 
sel.register(lsock, selectors.EVENT_READ, data=None)

#try:
#Event loop
while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)
#except:
    #print('Caught keyboard interrupt, Exiting')
#finally:
 #       sel.close()




