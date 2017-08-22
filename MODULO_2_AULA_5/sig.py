#/usr/bin/python

import signal

def ctrl_chandler(signum,frm):
    print "Haha! Voce nao pode me fechar"

print "Installing signal handler" 

signal.signal(signal.SIGINT, ctrl_chandler)

print "Done"

while True:
    pass
