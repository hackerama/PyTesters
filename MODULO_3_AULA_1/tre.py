#/usr/bin/python

import threading
import time

def dosome(i):
    print "Fazendo alguma coisa %d" % i
    time.sleep(5)
    print "Terminando o que estava fazendo %d" % i

for i in range (1,10):
    t = threading.Thread(target=dosome, args=(i,))
    t.start()
