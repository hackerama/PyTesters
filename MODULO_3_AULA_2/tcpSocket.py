#!/usr/bin/python
# Intrucoes de uso da biblioteca SocketServer para criar um servidor

import SocketServer

class echoHandler(SocketServer.BaseRequestHandler):
    def handler(self):
        print 'conexao recebida de: ', self.client_address
        data = 'dummy'

        while len(data):
            data = self.request.recv(1024)
            print data
            self.request.send(data)

        print "client left" 

serverAddr = ("192.168.0.17", 9000)

server = SocketServer.TCPServer(serverAddr, echoHandler)

server.serve_forever()
