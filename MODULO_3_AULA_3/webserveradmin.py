#!/usr/bin/python
"""
        Criando um HTTP Server que manuseia determinado path 
"""

import SocketServer
import SimpleHTTPServer

class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    #classe que cria um handler para filtrar um determinado path (/admin)
    
    def do_GET(self):
        if self.path == '/admin':
            self.wfile.write("Esta pagina so pode ser acessada por admins! Seus dados foram gravados\n")
            self.wfile.write(self.headers)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpServer = SocketServer.TCPServer(('', 10000), HttpRequestHandler)

httpServer.serve_forever()
