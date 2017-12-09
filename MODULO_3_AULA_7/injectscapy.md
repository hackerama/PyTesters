# INJECAO DE PACOTES COM SCAPY

<h3> CRIAR PACOTE </H3>

    pkt = IP(dst="google.com")

<h3> ENVIAR PACOTE NA CAMADA 3 </h3>
    
    send(pkt)

<h3> ENVIAR PAYLOAD EM UMA REQUISICAO ICMP </h3>

    pkt = IP(dst="google.com")/ICMP()/"WakaWaka"

<h3> ENVIAR PACOTES NA CAMADA 2 </h3> 

SENDP - Envia pacotes na camada 2. Precisa especificar a interface.
Constuimos o Ethernet header manualmente. 

    sendp(Ether()/IP(dst="google.com")/ICMP()/"WakaWaka", iface="eth0")

Para criar um loop no envio:

    sendp(Ether()/IP(dst="google.com")/ICMP()/"WakaWaka", iface="eth0", loop=1)
    
Para setar um intervalo entre os envios:
  
    sendp(Ether()/IP(dst="google.com")/ICMP()/"WakaWaka", iface="eth0", loop=1, inter=1)

<h3>ENVIAR E RECEBER PACOTES COM AS FUNCOES SEND AND RECEIVE</h3>

<h4> Camada 3 </h4>

- sr()
Retornar os pacotes respondidos e nao respondidos:
     
    sr(IP(dst="google.com")/ICMP()/"WakaWaka")

Gravando as respostas em uma variavel:

    response, no_response = _ #underline significa o ultimo resultado
    
    response
    <Results: TCP:0 UDP:0 ICMP:1 Other:0>
    
    no_response
    <Unanswered: TCP:0 UDP:0 ICMP:0 Other:0>
   
    $ response[0]
    (<IP  frag=0 proto=icmp dst=172.217.19.206 |<ICMP  |<Raw  load='WakaWaka' |>>>, <IP  version=4L ihl=5L tos=0x0 len=36 id=0 flags= frag=0L ttl=47 proto=icmp chksum=0xa6f src=172.217.19.206 dst=192.168.0.27 options=[] |<ICMP  type=echo-reply code=0 chksum=0x7a7a id=0x0 seq=0x0 |<Raw  load='WakaWaka' |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>>)

- Enviando um pacote IP simples:
Ele vai enviar, e ficar aguardando eternamente por uma resposta, pois eh um pacote simples sem nenhuma requisicao especifica. 

        sr(IP(dst="google.com"), timeout = 3)
        Begin emission:
        .Finished to send 1 packets.

        Received 1 packets, got 0 answers, remaining 1 packets
        (<Results: TCP:0 UDP:0 ICMP:0 Other:0>, <Unanswered: TCP:0 UDP:0 ICMP:0 Other:1>)

Observe que agora o pacote foi listado como nao respondido.  

- sr1() 
Retorna apenas os pacotes respondidos ou enviados. Espera por uma unica resposta.
    
       sr1(IP(dst="google.com")/ICMP()/"WakaWaka")

<h4> Camada 2 </h4>

- srp()

- srp1()

        pkt = srp1(Ether()/IP(dst="google.com",ttl=22)/ICMP()/"WakaWaka")i



<h3> MUDANDO AS CONFIGURACOES DE ROTEAMENTO </h3>

Mostrar as configuracoes das routing tables:

    >>> conf.route
    Network         Netmask         Gateway         Iface           Output IP
    127.0.0.0       255.0.0.0       0.0.0.0         lo              127.0.0.1      
    0.0.0.0         0.0.0.0         192.168.0.1     eth0            192.168.0.27   
    192.168.0.0     255.255.255.0   0.0.0.0         eth0            192.168.0.27   

Adicionar um route:

    >>> conf.route.add(host="192.168.0.10", gw="192.168.0.99")
    >>> conf.route
    Network         Netmask         Gateway         Iface           Output IP
    127.0.0.0       255.0.0.0       0.0.0.0         lo              127.0.0.1      
    0.0.0.0         0.0.0.0         192.168.0.1     eth0            192.168.0.27   
    192.168.0.0     255.255.255.0   0.0.0.0         eth0            192.168.0.27   
    192.168.0.10    255.255.255.255 192.168.0.99    eth0            192.168.0.27   

Adicionar um route para toda a rede:

    >>> conf.route.add(net="192.168.10.1/8", gw="192.168.0.100")
    >>> conf.route
    Network         Netmask         Gateway         Iface           Output IP
    127.0.0.0       255.0.0.0       0.0.0.0         lo              127.0.0.1      
    0.0.0.0         0.0.0.0         192.168.0.1     eth0            192.168.0.27   
    192.168.0.0     255.255.255.0   0.0.0.0         eth0            192.168.0.27   
    192.168.0.10    255.255.255.255 192.168.0.99    eth0            192.168.0.27   
    192.168.10.1    255.0.0.0       192.168.0.100   eth0            192.168.0.27

Retornar as configuracoes originais:

    >>> conf.route.resync()
    >>> conf.route
    Network         Netmask         Gateway         Iface           Output IP
    127.0.0.0       255.0.0.0       0.0.0.0         lo              127.0.0.1      
    0.0.0.0         0.0.0.0         192.168.0.1     eth0            192.168.0.27   
    192.168.0.0     255.255.255.0   0.0.0.0         eth0            192.168.0.27 
