# Requisicoes ARP com o Scapy

        >>> from scapy.all import *
        >>> pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst='192.168.0.1', hwdst="ff:ff:ff:ff:ff:ff")
        >>> pkt.show()
        ###[ Ethernet ]### 
          dst       = ff:ff:ff:ff:ff:ff
          src       = 08:00:27:49:f0:fa
          type      = ARP
        ###[ ARP ]### 
             hwtype    = 0x1
             ptype     = IPv4
             hwlen     = 6
             plen      = 4
             op        = who-has
             hwsrc     = 08:00:27:49:f0:fa
             psrc      = 192.168.0.27
             hwdst     = ff:ff:ff:ff:ff:ff
             pdst      = 192.168.0.1

        >>> srp1(pkt)
        Begin emission:
        Finished to send 1 packets.
        *
        Received 1 packets, got 1 answers, remaining 0 packets
        <Ether      dst=08:00:27:49:f0:fa src=6c:b5:6b:0c:6c:dd type=ARP |<ARP  hwtype=0x1 ptype=IPv4 hwlen=6 plen=4 op=is-at hwsrc=6c:b5:6b:0c:6c:dd psrc=192.168.0.1 hwdst=08:00:27:49:f0:fa pdst=192.168.0.27 |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>
        >>> 

