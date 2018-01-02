# ANALIZANDO RESPOSTAS DE REQUISICOES WEB

<h3> CONSULTAR UMA URL ESPECIFICA </h3>

        >>> import urllib
        >>> httpResponse = urllib.urlopen("http://localhost")
  
<h3> CONSULTAR O RESPONSE CODE </h3>

        >>> httpResponse.code
        200

<h3> LER A RESPOSTA </h3>

        >>> httpResponse.read()
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<html>\n <head>\n  <title>Index of /</title>\n </head>\n <body>\n<h1>Index of /</h1>\n  <table>\n       <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=    S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>\n   <tr><th colspan="5"><hr></th></tr>\n<tr><td valign="top"><img src="/icons/folder.gif" alt="    [DIR]"></td><td><a href="cgi-bin/">cgi-bin/</a></td><td align="right">2017-12-18 16:53  </td><td align="right">  - </td><td>&nbsp;</td></tr>\n<tr><td valign="top"><    img src="/icons/text.gif" alt="[TXT]"></td><td><a href="exploit.html">exploit.html</a></td><td align="right">2017-12-20 21:12  </td><td align="right">2.0K</td><td>&    nbsp;</td></tr>\n<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="pycheecker/">pycheecker/</a></td><td align="right">2017-12-31 13:22      </td><td align="right">  - </td><td>&nbsp;</td></tr>\n<tr><td valign="top"><img src="/icons/binary.gif" alt="[   ]"></td><td><a href="server.exe">server.exe</a></    td><td align="right">2017-12-20 20:11  </td><td align="right">352K</td><td>&nbsp;</td></tr>\n   <tr><th colspan="5"><hr></th></tr>\n</table>\n<address>Apache/2.4.25     (Debian) Server at localhost Port 80</address>\n</body></html>\n'
        
