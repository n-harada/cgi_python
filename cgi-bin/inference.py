#!/usr/local/bin/python3
# -*- coding:utf-8 -*-


print('Content-type: text/html; charset=UTF-8\r\n')
print("<link rel='stylesheet' href='../style.css'>")
# print("<h1>学習中...</h1><div class='loader'>Loading...</div>", flush=True)
print(
    "<h1 class='learning'>学習中...</h1><div class='loader'></div>", flush=True)

import subprocess
cmd = "python cgi-bin/sleep.py"
# subprocess.run(cmd.split() ,check=True)
popen1 = subprocess.Popen(cmd.split())
popen1.wait()
print("<style type='text/css'>.learning,.loader{display:none}</style>", flush=True)
print("<h1>学習終了</h1>", flush=True)
cmd = "python cgi-bin/sleep.py"
popen2 = subprocess.Popen(cmd.split())
popen2.wait()
# print('<p>Hello, World!</p>', flush=True)
