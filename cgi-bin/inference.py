#!/usr/bin/python3
# -*- coding:utf-8 -*-
import subprocess


python_code1 = '../face_recognition_on_coral/face_recording_with_training'
python_code2 = '../face_recognition_on_coral/face_detection_recognition_sklearn.py'


print('Content-type: text/html; charset=UTF-8\r\n')
print("<link rel='stylesheet' href='../style.css'>")
print(
    "<h1 id='h1' class='learning'>学習中</h1><div class='loader'></div>", flush=True)

popen1 = subprocess.Popen(python_code1.split())
popen1.wait()
# print("<style type='text/css'>.learning,.loader{display:none}</style>", flush=True)
print("<script>document.getElementById('h1').innerHTML='推論中'</script>", flush=True)
# print("<h1>学習終了</h1>", flush=True)


cmd = "python3 cgi-bin/sleep.py"
popen2 = subprocess.Popen(cmd.split())
popen2.wait()

