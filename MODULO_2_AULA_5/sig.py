#/usr/bin/python

# Explica como manuasear sinais utilizando a biblioteca signal. 
# Consultar lista de sinais: $ man 7 signal
# No exemplo abaixo ele utiliza o SINAL SIGINT, responsavel pela
# Interrupcao do programa com Ctrl+C.  

import signal

# Funcao que ira dizer o que fazer com o SINAL de Ctrl+C quando recevermos
def ctrl_chandler(signum,frm):
    print "Haha! Voce nao pode me fechar"

print "Installing signal handler" 

# cria o objeto que ira chamar a funcao para tratar do sinal 
# quando receber-lo
signal.signal(signal.SIGINT, ctrl_chandler)

print "Done"

while True: #cria um loop para evitar que o programa feche
    pass
