#/usr/bin/python

#Non-Blocking Multiplexed Echo Server

import socket, select

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 8004

tcpSocket.bind(("0.0.0.0", port))

tcpSocket.listen(10)

print "[+] Esperando por uma conexao na porta:", port

holeinsock = []


while True:

        read, write, ex = select.select([tcpSocket] + holeinsock, [], [])
        for s in read:
            if s is tcpSocket:
                (client, (ip, port)) = tcpSocket.accept()
                print "Conexao recebida do IP %s na porta %s" %(ip, port)

                print "Iniciando ECHO output"
                holeinsock.append(client)

            else:
                data = s.recv(16)
                if data == "":
                    holeinsock.remove(s)
                    print "Fechando conexao..."
                else:
                    print "Recebido isto IP %s na porta %s: %s " % (ip, port, data)
                    client.send("Cliente, voce enviou isto para o servidor: " + data)

