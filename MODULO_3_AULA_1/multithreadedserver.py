#!usr/bin/python 

import socket
import thread
import sys

def clientHandler(clientSock):
    client_data = clientSock.recv(2048)
    if client_data:
        clientSock.send(client_data)
       # clientSock.close()
    else:
       pass
       # clientSock.close()
       # return 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.32', int(sys.argv[1])))
s.listen(10)


while True:
    clientSock, addr = s.accept()

    #comeca uma nova thread
    print '\nComecando uma nova thread'
    thread.start_new_thread(clientHandler, (clientSock,))
     
