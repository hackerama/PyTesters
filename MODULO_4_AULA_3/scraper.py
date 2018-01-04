#/usr/bin/python

from bs4 import BeautifulSoup
import urllib

httpResponse = urllib.urlopen('https://www.centraldeconcursos.com.br/aprovados/camara-municipal-de-osasco-sp_96.html')

print '[+] HTTP Response Status Code: {}'.format(httpResponse.code)

html = httpResponse.read()

bt = BeautifulSoup(html, "lxml")


aprov = bt.find_all('div', 'um')

#solucao 2 > Passando os atributos como um dicionario
#aprov = bt.find_all('div', { 'class' : 'um'})

print '[L I S T A  D E   A P R O V A D O S]\n'

for item in aprov:
    work = item.contents[0]
    print work

