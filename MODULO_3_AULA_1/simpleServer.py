#/usr/bin/python

import socket

# cria o objeto socket
s = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
#Permite que eu reuse o endereco bindado apos o server crashar imediatamente
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 8000
bindip = '192.168.0.25'
# binda, abre uma porta em determinada interface para comecar a ouvir
s.bind((bindip, port))

#comeca a ouvir, o argumento refere-se ao numero de clientes que ele suporta
s.listen(5)

print '\nEsperando por um cliente na porta %d:' % port 

#aceita a conexao
(client, (ip, port)) = s.accept() #cria o objeto socket na variavel client

print 'Conexao recebida: %s' % ip

#envias dados para o cliente utilizando o objeto socket criado.
client.send("Bem vindo ao Server\n")

'''
while True:
    data = client.recv(2048)
    print data

'''
#defino uma variavel data com um valor qualquer
data  = 'dummy'

# o loop abaixo cria a funcao de ECHO no server:
while len(data):
    data = client.recv(2048) #recebe os dados do cliente
    print "Dados recebidos", data #imprime os dados
    client.send(data) #envia os dados de volta apra o cliente

print "Encerrando conexao" 
client.close()
print "Encerrando server"
s.close()

