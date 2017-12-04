# CAPTURA DE PACOTES COM SCAPY

    $ sudo scapy

<h3>LISTAR PROTOCOLOS</h3>
    >>> ls()

<h3>CHECAR CONFIGURAÇÕES</h3>
    >>> conf

<h3> LISTAR AS OPÇÕES DE COMANDO </h3>

    >> lsc()

<h3> SNIFFAR PACOTES DA REDE </h3>

    >>> pkts = sniff(iface="eth0", count=3)
    >>> pkts #ve os pacotes capturados
    >>> pkts[0] #ve os pacotes um a um
    >>> pkts[0].show() #ve os pacotes de forma organizada.

<h3> DUMP DE PACOTES EM HEX </h3>

    >>> hexdump(pkts[0])

    0000   01 00 5E 7F FF FA 6C B5  6B 0C 6C DD 08 00 45 00   ..^...l.k.l...E.
    0010   01 4A DE AD 00 00 04 11  26 52 C0 A8 00 01 EF FF   .J......&R......
    0020   FF FA 07 6D 07 6C 01 36  3B C8 4E 4F 54 49 46 59   ...m.l.6;.NOTIFY
    0030   20 2A 20 48 54 54 50 2F  31 2E 31 0D 0A 48 4F 53    * HTTP/1.1..HOS
    0040   54 3A 20 32 33 39 2E 32  35 35 2E 32 35 35 2E 32   T: 239.255.255.2
    0050   35 30 3A 31 39 30 30 0D  0A 43 61 63 68 65 2D 43   50:1900..Cache-C
    0060   6F 6E 74 72 6F 6C 3A 20  6D 61 78 2D 61 67 65 3D   ontrol: max-age=
    0070   31 39 30 30 0D 0A 4C 6F  63 61 74 69 6F 6E 3A 20   1900..Location: 
    0080   68 74 74 70 3A 2F 2F 31  39 32 2E 31 36 38 2E 30   http://192.168.0
    0090   2E 31 3A 38 30 39 30 2F  52 6F 6F 74 44 65 76 69   .1:8090/RootDevi
    00a0   63 65 2E 78 6D 6C 0D 0A  4E 54 3A 20 75 75 69 64   ce.xml..NT: uuid
    00b0   3A 75 70 6E 70 2D 49 6E  74 65 72 6E 65 74 47 61   :upnp-InternetGa
    00c0   74 65 77 61 79 44 65 76  69 63 65 2D 31 5F 30 2D   tewayDevice-1_0-
    00d0   36 63 62 35 36 62 30 63  36 63 64 64 0D 0A 55 53   6cb56b0c6cdd..US
    00e0   4E 3A 20 75 75 69 64 3A  75 70 6E 70 2D 49 6E 74   N: uuid:upnp-Int
    00f0   65 72 6E 65 74 47 61 74  65 77 61 79 44 65 76 69   ernetGatewayDevi
    0100   63 65 2D 31 5F 30 2D 36  63 62 35 36 62 30 63 36   ce-1_0-6cb56b0c6
    0110   63 64 64 0D 0A 4E 54 53  3A 20 73 73 64 70 3A 61   cdd..NTS: ssdp:a
    0120   6C 69 76 65 0D 0A 53 65  72 76 65 72 3A 20 55 50   live..Server: UP
    0130   6E 50 2F 31 2E 30 20 55  50 6E 50 2F 31 2E 30 20   nP/1.0 UPnP/1.0 
    0140   55 50 6E 50 2D 44 65 76  69 63 65 2D 48 6F 73 74   UPnP-Device-Host
    0150   2F 31 2E 30 0D 0A 0D 0A                            /1.0....

<h3> LER E ESCREVER ARQUIVOS PCAP </h3>

    >>> wrpcap("demo.pcap", pkts) #write pcap file

    >>> read_pkts = rdpcap("demo.pcap") #le os arquivos

<h3> APLICANDO FILTROS BPF (Berkeley Packet Filter) </h3>

    #requests icmp
    >>> pkts = sniff(iface="eth0", filter ="icmp", count=3)

#resposta de um ping observe no pkts[0], o type eh uma echo-request e no pkts[1] eh uma echo-reply

    >>> pkts[0]
    >>> pkts[0].show()

    ###[ Ethernet ]### 
      dst= 6c:b5:6b:0c:6c:dd
      src= 08:00:27:49:f0:fa
      type= IPv4
    ###[ IP ]### 
         version= 4L
         ihl= 5L
         tos= 0x0
         len= 84
         id= 5442
         flags= DF
         frag= 0L
         ttl= 64
         proto= icmp
         chksum= 0x1e5a
         src= 192.168.0.22
         dst= 186.202.139.132
         \options\
    ###[ ICMP ]### 
            type= echo-request
            code= 0
            chksum= 0x37bd
            id= 0x95f
            seq= 0x1
    ###[ Raw ]### 
               load= 'L\x8f$Z\x00\x00\x00\x00\x7f&\x08\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

    >>> pkts[1].show()

    ###[ Ethernet ]### 
      dst= 08:00:27:49:f0:fa
      src= 6c:b5:6b:0c:6c:dd
      type= IPv4
    ###[ IP ]### 
         version= 4L
         ihl= 5L
         tos= 0x0
         len= 84
         id= 36239
         flags= 
         frag= 0L
         ttl= 48
         proto= icmp
         chksum= 0xf60c
         src= 186.202.139.132
         dst= 192.168.0.22
         \options\
    ###[ ICMP ]### 
            type= echo-reply
            code= 0
            chksum= 0x3fbd
            id= 0x95f
            seq= 0x1
    ###[ Raw ]### 
               load= 'L\x8f$Z\x00\x00\x00\x00\x7f&\x08\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

<h3> SNIFFAR EM TEMPO REAL UTILIZANDO A FUNCAO LAMBDA </h3>

#novamente capturando requests ICMP em um ping

    >>> pkts = sniff(iface="eth0", filter ="icmp", count=30, prn=lambda x: x.summary())
    Ether / IP / ICMP 192.168.0.22 > 186.202.139.132 echo-request 0 / Raw
    Ether / IP / ICMP 186.202.139.132 > 192.168.0.22 echo-reply 0 / Raw
    Ether / IP / ICMP 192.168.0.22 > 186.202.139.132 echo-request 0 / Raw
    Ether / IP / ICMP 186.202.139.132 > 192.168.0.22 echo-reply 0 / Raw
    Ether / IP / ICMP 192.168.0.22 > 186.202.139.132 echo-request 0 / Raw
    Ether / IP / ICMP 186.202.139.132 > 192.168.0.22 echo-reply 0 / Raw
    Ether / IP / ICMP 192.168.0.22 > 186.202.139.132 echo-request 0 / Raw
    Ether / IP / ICMP 186.202.139.132 > 192.168.0.22 echo-reply 0 / Raw
    Ether / IP / ICMP 192.168.0.22 > 186.202.139.132 echo-request 0 / Raw
    Ether / IP / ICMP 186.202.139.132 > 192.168.0.22 echo-reply 0 / Raw
    Ether / IP / ICMP 192.168.0.22 > 186.202.139.132 echo-request 0 / Raw
    Ether / IP / ICMP 186.202.139.132 > 192.168.0.22 echo-reply 0 / Raw
    Ether / IP / ICMP 192.168.0.22 > 186.202.139.132 echo-request 0 / Raw
    Ether / IP / ICMP 186.202.139.132 > 192.168.0.22 echo-reply 0 / Raw

#para capturar todo o pacote

    >>> pkts = sniff(iface="eth0", filter ="icmp", count=30, prn=lambda x: x.summary())

<h3> EXPORTAR PACOTES CAPTURADOS COMO STRINGS </h3>

    >>> icmp_str = str(pkts[0])

    >>> icmp_str
    'l\xb5k\x0cl\xdd\x08\x00\'I\xf0\xfa\x08\x00E\x00\x00Ty\xa6@\x00@\x01\xb9\xf5\xc0\xa8\x00\x16\xba\xca\x8b\x84\x08\x00\xc7\'\t\xd5\x00\x01\xd0\x92$Z\x00\x00\x00\x00qB\x02\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

#para reconstruir

    >>> recon = Ether(icmp_str)
    >>> recon
    <Ether  dst=6c:b5:6b:0c:6c:dd src=08:00:27:49:f0:fa type=IPv4 |<IP  version=4L ihl=5L tos=0x0 len=84 id=31142 flags=DF frag=0L ttl=64 proto=icmp chksum=0xb9f5 src=192.168.0.22 dst=186.202.139.132 options=[] |<ICMP  type=echo-request code=0 chksum=0xc727 id=0x9d5 seq=0x1 |<Raw  load='\xd0\x92$Z\x00\x00\x00\x00qB\x02\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567' |>>>>


<h3> EXPORTAR PACOTES EM BASE 64 </h3>

    >>> export_object(icmp_str)
    eNprYApNytmazZNzl4NB3fPDLw4GVwaGkMplDgwOjDu/HljBILbrVHcLB8Nxdc6rDIwXJqlEMQBB
    oRMTiGIQEBQSFhEVE5eQlJKWkZWTV1BUUlZRVVPX0NTS1tHV0zcwNDI2MTUzL2TUAwBEKBkT

#para reconstruir

    >>> newPkt = import_object() #[ENTER]
    eNprYApNytmazZNzl4NB3fPDLw4GVwaGkMplDgwOjDu/HljBILbrVHcLB8Nxdc6rDIwXJqlEMQBB
    oRMTiGIQEBQSFhEVE5eQlJKWkZWTV1BUUlZRVVPX0NTS1tHV0zcwNDI2MTUzL2TUAwBEKBkT

    #[CTRL + D]
    >>> newPkt
    'l\xb5k\x0cl\xdd\x08\x00\'I\xf0\xfa\x08\x00E\x00\x00Ty\xa6@\x00@\x01\xb9\xf5\xc0\xa8\x00\x16\xba\xca\x8b\x84\x08\x00\xc7\'\t\xd5\x00\x01\xd0\x92$Z\x00\x00\x00\x00qB\x02\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'

    >>> Ether(newPkt)
    <Ether  dst=6c:b5:6b:0c:6c:dd src=08:00:27:49:f0:fa type=IPv4 |<IP  version=4L ihl=5L tos=0x0 len=84 id=31142 flags=DF frag=0L ttl=64 proto=icmp chksum=0xb9f5 src=192.168.0.22 dst=186.202.139.132 options=[] |<ICMP  type=echo-request code=0 chksum=0xc727 id=0x9d5 seq=0x1 |<Raw  load='\xd0\x92$Z\x00\x00\x00\x00qB\x02\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567' |>>>>
