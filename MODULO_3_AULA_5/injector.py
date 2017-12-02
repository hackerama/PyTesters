#/usr/bin/python

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

#Enquanto no sniffing, utilizamos o receive from, aqui utilizamos o bind
#na interface especifica, nesse caso eth0, utilizando o ethernet protocol 0x0800
rawSocket.bind(("eth0", socket.htons(0x0800)))

#Criamos entao um ethernet packet
#O pacote nada mais eh que o Ethernet header, com 14 bytes
#Os 6 primeiros sao o Destination IP, os 6 seguintes sao o Source IP
#e os 2 ultimos sao o ether type

packet = struct.pack("!6s6s2s", '\xff\xff\xff\xff\xff\xff', '\\\xc9\xd3D{\xe4', '\x08\x00')

print "PACOTE :" , packet,  "\n"
print "TAMANHO DO PACOTE: " , len(packet) , "\n"

# envia o pacote para a rede
# tcpdump -i eth0 -vv -XX "not port 22"
rawSocket.send(packet + "Ate mais e obrigado pelos peixes")

