#/usr/bin/python 
#-*-coding:utf-8-*-

import signal
import socket 
import sys
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "Conexao recebida: %s" % request
    client_socket.send("ACK\n")
    client_socket.close()


#Handler que ira gerenciar o sinal
#Recebe o sinal e trata ele, no exemplo, ele fecha o programa
def SigalarmHandler(signal, frame): 
        print "Alarme de desligamento recebido" 
        sys.exit(0)
        
bind_ip = "192.168.0.15"
bind_port  = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((bind_ip, bind_port))
s.listen(5)
print "%s: Escutando na porta %d." % (bind_ip, bind_port)

#Cria o signal (Objeto) de alarme, com um contador para executar
# determianda tarefa a ser tratada na funcao SigalarmHandler()
signal.signal(signal.SIGALRM, SigalarmHandler)
# Seta o tempo do contador do sinal de alarme. 
signal.alarm(15)

while True:
    client, addr = s.accept()
    print "[+] Conexão autorizada de %s:%d" % (addr[0], addr[1])
    t = threading.Thread(target=handle_client, args=(client,))
    t.start()
    

