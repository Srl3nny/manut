#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import subprocess
DIR = '/tmp/recebe/script.sh'
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X\n'
arq = open(DIR, 'w')
while 1:
    dados = tcp.recv(1024)
    if not dados:
        break
    arq.write(dados)
arq.close()
tcp.close()
subprocess.call(DIR, shell=True)
