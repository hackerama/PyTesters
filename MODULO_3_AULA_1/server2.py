#!/usr/bin/python
#!-*- coding: utf-8 -*-

import socket
import threading

bind_ip = '192.168.0.32'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port)) #configura/binda o ip e a porta para receber a conexão

server.listen(5) # começa a escuta
print "[+]Escuta ativa: %s:%s " % (bind_ip,bind_port)

#Começa a thread para tratamento de clientes

def handle_client(client_socket):
        request = client_socket.recv(1024)  #exibe o que o cliente enviar, a request
        print "[+]Recebido: %s" % request
        client_socket.send("ACK!")
       # client_socket.close()

while True:
        client,addr = server.accept()
        print "[+] Conexão autorizada de %s:%d" % (addr[0], addr[1])
        t = threading.Thread(target=handle_client, args=(client,))
        t.start()
