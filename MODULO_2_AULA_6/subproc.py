#/usr/bin/python

import subprocess

#subprocess.call ==> executa um shell command e retorna a saida.
call = subprocess.call(['ls', '-la']) #retorna o output automaticamente na tala. 

print "\nTipo do Objeto: ", type(call) # retorna um inteiro. 

#subprocess.check_output ==> checa a saida e retorna um inteiro
check = subprocess.check_output(['ls', "-la"]) 

print check
print "Tipo do Objeto: ", type(check) # retorna ums string

#subprocess.PIPE ==> Gerencia as saidas e entradas padrao.
handle = subprocess.Popen(['ls', '-la'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

print handle.stdout.read() # le o standart output
print "Tipo do Objeto: ", type(handle) # retorna uma classe

