# ANALIZANDO RESPOSTAS DE REQUISICOES WEB

<h3> CONSULTAR UMA URL ESPECIFICA </h3>

        >>> import urllib
        >>> httpResponse = urllib.urlopen("http://localhost")
  
<h3> CONSULTAR O RESPONSE CODE </h3>

        >>> httpResponse.code
        200

<h3> LER A RESPOSTA </h3>

        >>> httpResponse.read()
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<html>\n <head>\n  <title>Index of /</title>\n </head>\n <body>\n<h1>Index of /</h1>\n  <table>\n   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>\n   <tr><th colspan="5"><hr></th></tr>\n<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="cgi-bin/">cgi-bin/</a></td><td align="right">2017-12-18 16:53  </td><td align="right">  - </td><td>&nbsp;</td></tr>\n<tr><td valign="top"><img src="/icons/text.gif" alt="[TXT]"></td><td><a href="exploit.html">exploit.html</a></td><td align="right">2017-12-20 21:12  </td><td align="right">2.0K</td><td>&nbsp;</td></tr>\n<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="pycheecker/">pycheecker/</a></td><td align="right">2017-12-31 13:22  </td><td align="right">  - </td><td>&nbsp;</td></tr>\n<tr><td valign="top"><img src="/icons/binary.gif" alt="[   ]"></td><td><a href="server.exe">server.exe</a></td><td align="right">2017-12-20 20:11  </td><td align="right">352K</td><td>&nbsp;</td></tr>\n   <tr><th colspan="5"><hr></th></tr>\n</table>\n<address>Apache/2.4.25 (Debian) Server at localhost Port 80</address>\n</body></html>\n'

<h3> ALGUMAS OPCOES </h3>

        >>> dir(httpResponse)
        ['__doc__', '__init__', '__iter__', '__module__', '__repr__', 'close', 'code', 'fileno', 'fp', 'getcode', 'geturl', 'headers', 'info', 'next', 'read', 'readline', 'readlines', 'url']
        
        >>> dir(httpResponse.headers)
        ['__contains__', '__delitem__', '__doc__', '__getitem__', '__init__', '__iter__', '__len__', '__module__', '__setitem__', '__str__', 'addcontinue', 'addheader', 'dict', 'encodingheader', 'fp', 'get', 'getaddr', 'getaddrlist', 'getallmatchingheaders', 'getdate', 'getdate_tz', 'getencoding', 'getfirstmatchingheader', 'getheader', 'getheaders', 'getmaintype', 'getparam', 'getparamnames', 'getplist', 'getrawheader', 'getsubtype', 'gettype', 'has_key', 'headers', 'iscomment', 'isheader', 'islast', 'items', 'keys', 'maintype', 'parseplist', 'parsetype', 'plist', 'plisttext', 'readheaders', 'rewindbody', 'seekable', 'setdefault', 'startofbody', 'startofheaders', 'status', 'subtype', 'type', 'typeheader', 'unixfrom', 'values']
         

<h3> CHECANDO A URL </h3> 

        >>> httpResponse.url
        'http://localhost'                       
        
        >>> httpResponse.geturl()
        'http://localhost'

        >>> httpResponse.headers.items()
        # o primeiro valor de cada tupla e chamado de header e o segundo de value
        [('content-length', '1351'), ('vary', 'Accept-Encoding'), ('server', 'Apache/2.4.25 (Debian)'), ('connection', 'close'), ('date', 'Tue, 02 Jan 2018 18:18:03 GMT'), ('content-type', 'text/html;charset=UTF-8')]


        >>> httpResponse.headers.keys()
        ['content-length', 'vary', 'server', 'connection', 'date', 'content-type']


<h3> PRINTANDO CABECALHOS </h3>

        >>> for header, value in httpResponse.headers.items():
        ...     print header + ' : ' + value
        ...
        content-length : 1351
        vary : Accept-Encoding
        server : Apache/2.4.25 (Debian)
        connection : close
        date : Tue, 02 Jan 2018 22:40:50 GMT
        content-type : text/html;charset=UTF-8


