#!/usr/bin/python
"""
        Criando um HTTP Server simples
"""

import SocketServer
import SimpleHTTPServer

httpServer = SocketServer.TCPServer(('', 10001), SimpleHTTPServer.SimpleHTTPRequestHandler)

httpServer.serve_forever()
