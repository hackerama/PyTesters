#!usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = '192.168.0.17'
port = 8000

s.connect((ip, port))
while True:

    userInput = raw_input("Envie uma mensagem para o servidor :")
    s.send(userInput)
    print s.recv(2048)
    
s.close()

