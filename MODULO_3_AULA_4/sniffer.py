#!/usr/bin/python

import socket 
import struct
import binascii

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

pkt = rawSocket.recvfrom(2048)

#os primeiros 14 bytes sao o cabecalho ethernet (ethernet header)
ethernetHeader = pkt[0][0:14]

#Os primeiros 6 bytes sao o destination mac address
#Os proximos 6 sao o source mac address
#Os ultimos 2 bytes sao o ether type (0800) IP ; ver /usr/include/linux/if_ether.h
eth_hdr = struct.unpack("6s6s2s", ethernetHeader)
print "eth_hdr = " , eth_hdr

print binascii.hexlify(eth_hdr[0])
print binascii.hexlify(eth_hdr[1])
print binascii.hexlify(eth_hdr[2])

ipHeader = pkt[0][14:34]
ip_hdr = struct.unpack("12s4s4s", ipHeader)
print "ip_hdr = " , ip_hdr

print "Source IP address: " + socket.inet_ntoa(ip_hdr[1])

print "Destination IP address: " + socket.inet_ntoa(ip_hdr[2])

tcpHeader = pkt[0][34:54]

tcp_hdr = struct.unpack("!HH16s", tcpHeader)

print tcp_hdr


