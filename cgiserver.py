#!/usr/bin/python3
# -*- coding: utf-8 -*-


import http.server
import webbrowser

server_address = ("", 8001)
handler_class = http.server.CGIHTTPRequestHandler #1 ハンドラを設定
server = http.server.HTTPServer(server_address, handler_class)
webbrowser.open("http://127.0.0.1:8001")
server.serve_forever()


# http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler)